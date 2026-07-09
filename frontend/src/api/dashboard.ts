import api from "./axios";

/* ---------- Types ---------- */

export interface DashboardInterview {
  id: number;
  title: string;
  company: string;
  role: string;
  interview_type: string;
  difficulty: string;
  status: string;
  created_at?: string;
}

export interface DashboardReport {
  id: number;
  interview_id: number;

  company: string;
  role: string;

  overall_score: number;
  technical_score: number;
  communication_score: number;
  confidence_score: number;

  summary?: string;
  strengths?: string;
  weaknesses?: string;
  recommendations?: string;
  learning_roadmap?: string;
  hiring_recommendation?: string;

  created_at?: string;
}

export interface DashboardData {
  interviews: DashboardInterview[];
  reports: DashboardReport[];

  stats: {
    totalInterviews: number;
    completedInterviews: number;
    averageScore: number;
    latestTechnicalScore: number;
    latestCommunicationScore: number;
    latestConfidenceScore: number;
  };

  latestReport: DashboardReport | null;

  recommendedFocus: string;
}


/* ---------- Empty Dashboard ---------- */

const emptyDashboard: DashboardData = {
  interviews: [],
  reports: [],

  stats: {
    totalInterviews: 0,
    completedInterviews: 0,
    averageScore: 0,
    latestTechnicalScore: 0,
    latestCommunicationScore: 0,
    latestConfidenceScore: 0,
  },

  latestReport: null,

  recommendedFocus:
    "Complete an interview to receive personalized recommendations.",
};


/* ---------- Calculate Overall Score ---------- */

function calculateOverallScore(
  report: DashboardReport
): number {
  const technical = Number(
    report.technical_score
  );

  const communication = Number(
    report.communication_score
  );

  const confidence = Number(
    report.confidence_score
  );

  const scores = [
    technical,
    communication,
    confidence,
  ].filter(
    (score) =>
      Number.isFinite(score) &&
      score >= 0
  );

  if (scores.length === 0) {
    return 0;
  }

  return Number(
    (
      scores.reduce(
        (total, score) =>
          total + score,
        0
      ) / scores.length
    ).toFixed(2)
  );
}


/* ---------- Dashboard API ---------- */

export async function getDashboard(): Promise<DashboardData> {
  try {
    /*
      Fetch interviews and reports together.

      A report request failure should not break
      the complete dashboard.
    */

    const interviewsPromise =
      api.get<DashboardInterview[]>(
        "/interviews"
      );

    const reportsPromise = api
      .get<DashboardReport[]>("/reports")
      .catch((error) => {
        console.error(
          "Failed to load dashboard reports:",
          error
        );

        return {
          data: [] as DashboardReport[],
        };
      });

    const [
      interviewsResponse,
      reportsResponse,
    ] = await Promise.all([
      interviewsPromise,
      reportsPromise,
    ]);


    const interviews =
      interviewsResponse.data ?? [];

    const rawReports =
      reportsResponse.data ?? [];


    /* ---------- Normalize Reports ---------- */

    /*
      Calculate overall score from the actual
      technical, communication, and confidence
      component scores.

      This prevents an old or inconsistent
      overall_score value from causing the
      dashboard to display incorrect results.
    */

    const normalizedReports: DashboardReport[] =
      rawReports.map((report) => ({
        ...report,

        overall_score:
          calculateOverallScore(report),
      }));


    /* ---------- Valid Reports ---------- */

    const validReports =
      normalizedReports.filter(
        (report) =>
          Number.isFinite(
            Number(report.overall_score)
          )
      );


    /* ---------- Report Interview IDs ---------- */

    const reportedInterviewIds = new Set(
      validReports.map(
        (report) =>
          report.interview_id
      )
    );


    /* ---------- Normalize Interview Status ---------- */

    const normalizedInterviews =
      interviews.map((interview) => ({
        ...interview,

        status:
          reportedInterviewIds.has(
            interview.id
          )
            ? "COMPLETED"
            : interview.status,
      }));


    /* ---------- Interview Statistics ---------- */

    const totalInterviews =
      normalizedInterviews.length;

    const completedInterviews =
      normalizedInterviews.filter(
        (interview) =>
          interview.status?.toUpperCase() ===
          "COMPLETED"
      ).length;


    /* ---------- Average Score ---------- */

    const averageScore =
      validReports.length > 0
        ? Math.round(
            validReports.reduce(
              (total, report) =>
                total +
                Number(
                  report.overall_score
                ),
              0
            ) / validReports.length
          )
        : 0;


    /* ---------- Latest Report ---------- */

    const sortedReports = [
      ...validReports,
    ].sort((a, b) => {
      /*
        Prefer created_at when available.

        If created_at is unavailable,
        use report ID as fallback.
      */

      if (
        a.created_at &&
        b.created_at
      ) {
        return (
          new Date(
            b.created_at
          ).getTime() -
          new Date(
            a.created_at
          ).getTime()
        );
      }

      return b.id - a.id;
    });


    const latestReport =
      sortedReports.length > 0
        ? sortedReports[0]
        : null;


    /* ---------- Recommended Focus ---------- */

    let recommendedFocus =
      "Complete an interview to receive personalized recommendations.";


    if (latestReport) {
      const scores = [
        {
          area: "Technical Skills",

          score: Number(
            latestReport
              .technical_score ?? 0
          ),
        },

        {
          area: "Communication",

          score: Number(
            latestReport
              .communication_score ?? 0
          ),
        },

        {
          area: "Confidence",

          score: Number(
            latestReport
              .confidence_score ?? 0
          ),
        },
      ];


      scores.sort(
        (a, b) =>
          a.score - b.score
      );


      recommendedFocus =
        scores[0].area;
    }


    /* ---------- Final Dashboard Data ---------- */

    return {
      interviews:
        normalizedInterviews,

      reports:
        validReports,

      stats: {
        totalInterviews,

        completedInterviews,

        averageScore,

        latestTechnicalScore:
          Number(
            latestReport
              ?.technical_score ?? 0
          ),

        latestCommunicationScore:
          Number(
            latestReport
              ?.communication_score ?? 0
          ),

        latestConfidenceScore:
          Number(
            latestReport
              ?.confidence_score ?? 0
          ),
      },

      latestReport,

      recommendedFocus,
    };

  } catch (error) {
    console.error(
      "Failed to load dashboard:",
      error
    );

    return {
      ...emptyDashboard,

      stats: {
        ...emptyDashboard.stats,
      },

      interviews: [],

      reports: [],
    };
  }
}