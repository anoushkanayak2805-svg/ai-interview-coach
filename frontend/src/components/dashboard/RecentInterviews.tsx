import { useNavigate } from "react-router-dom";

import type {
  DashboardInterview,
  DashboardReport,
} from "../../api/dashboard";


interface RecentInterviewsProps {
  interviews: DashboardInterview[];
  reports: DashboardReport[];
}


export default function RecentInterviews({
  interviews,
  reports,
}: RecentInterviewsProps) {

  const navigate = useNavigate();


  /*
    Show only the latest 5 interviews.
  */

  const recentInterviews =
    interviews.slice(0, 5);


  /*
    Find the report belonging to an interview.
  */

  function getReportForInterview(
    interviewId: number
  ) {
    return reports.find(
      (report) =>
        report.interview_id === interviewId
    );
  }


  /*
    Score badge color based on performance.
  */

  function getScoreColor(
    score: number
  ) {

    if (score >= 80) {
      return "bg-green-100 text-green-700";
    }

    if (score >= 60) {
      return "bg-yellow-100 text-yellow-700";
    }

    return "bg-red-100 text-red-700";
  }


  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <div className="mb-8 flex items-center justify-between">

        <h2 className="text-2xl font-bold">
          Recent Interviews
        </h2>

        <button
          onClick={() =>
            navigate("/reports")
          }
          className="text-indigo-600 hover:underline"
        >
          View History
        </button>

      </div>


      {recentInterviews.length === 0 ? (

        <div className="rounded-2xl bg-slate-50 p-8 text-center">

          <h3 className="text-lg font-semibold text-slate-800">
            No interviews yet
          </h3>

          <p className="mt-2 text-sm text-slate-500">
            Start your first AI interview to see your progress here.
          </p>

          <button
            onClick={() =>
              navigate("/interviews/create")
            }
            className="mt-5 rounded-xl bg-indigo-600 px-5 py-3 text-white transition hover:bg-indigo-700"
          >
            Start Interview
          </button>

        </div>

      ) : (

        <div className="space-y-5">

          {recentInterviews.map(
            (interview) => {

              const report =
                getReportForInterview(
                  interview.id
                );

              const score =
                report
                  ? Math.round(
                      Number(
                        report.overall_score
                      )
                    )
                  : null;


              return (
                <div
                  key={interview.id}
                  className="flex flex-col gap-4 rounded-2xl border border-slate-200 p-5 transition hover:-translate-y-1 hover:shadow-md sm:flex-row sm:items-center sm:justify-between"
                >

                  <div>

                    <h3 className="font-semibold text-slate-900">
                      {
                        interview.company ||
                        "Company not specified"
                      }
                    </h3>

                    <p className="mt-1 text-sm text-gray-500">
                      {
                        interview.role ||
                        "Role not specified"
                      }
                    </p>

                    <p className="mt-2 text-xs font-medium uppercase tracking-wide text-slate-400">
                      {
                        interview.status ||
                        "Unknown"
                      }
                    </p>

                  </div>


                  <div className="flex items-center gap-3">

                    {score !== null ? (

                      <>
                        <span
                          className={`rounded-full px-4 py-2 font-semibold ${getScoreColor(
                            score
                          )}`}
                        >
                          {score}%
                        </span>

                        <button
                          onClick={() =>
                            navigate(
                              `/reports/${interview.id}`
                            )
                          }
                          className="rounded-xl border border-indigo-200 px-4 py-2 text-sm font-semibold text-indigo-600 transition hover:bg-indigo-50"
                        >
                          View Report
                        </button>
                      </>

                    ) : (

                      <span className="rounded-full bg-slate-100 px-4 py-2 text-sm font-semibold text-slate-500">
                        No Report
                      </span>

                    )}

                  </div>

                </div>
              );

            }
          )}

        </div>

      )}

    </div>
  );
}