import {
  Sparkles,
  Target,
  TrendingUp,
  AlertTriangle,
} from "lucide-react";


interface AICoachCardProps {
  recommendedFocus?: string;

  weakTopics?: string[];

  targetCompany?: string;

  targetRole?: string;

  technicalScore?: number;

  communicationScore?: number;

  confidenceScore?: number;
}


export default function AICoachCard({
  recommendedFocus =
    "Complete an interview to receive personalized recommendations.",

  weakTopics = [],

  targetCompany = "your target company",

  targetRole = "Software Engineer",

  technicalScore = 0,

  communicationScore = 0,

  confidenceScore = 0,
}: AICoachCardProps) {


  /* ---------------------------------
     Find Weakest Interview Area
  ---------------------------------- */

  const scoreAreas = [
    {
      name: "Technical Skills",
      score: technicalScore,
    },

    {
      name: "Communication",
      score: communicationScore,
    },

    {
      name: "Confidence",
      score: confidenceScore,
    },
  ];


  const hasInterviewScores =
    scoreAreas.some(
      (item) => item.score > 0
    );


  const weakestArea =
    hasInterviewScores
      ? [...scoreAreas].sort(
          (a, b) => a.score - b.score
        )[0]
      : null;


  /* ---------------------------------
     Resume Weak Topics
  ---------------------------------- */

  const displayedWeakTopics =
    weakTopics.slice(0, 3);


  /* ---------------------------------
     Main Focus
  ---------------------------------- */

  const mainFocus =
    weakestArea?.name ??
    recommendedFocus;


  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">


      {/* ---------- Header ---------- */}

      <div className="flex items-center gap-3">

        <div className="rounded-xl bg-indigo-100 p-3">

          <Sparkles
            className="text-indigo-600"
            size={24}
          />

        </div>


        <div>

          <h2 className="text-2xl font-bold text-slate-900">
            AI Coach
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Personalized recommendations from your
            resume and interview performance.
          </p>

        </div>

      </div>


      {/* ---------- Primary Recommendation ---------- */}

      <div className="mt-6 rounded-2xl bg-indigo-50 p-6">

        <div className="flex items-center gap-2">

          <Target
            size={18}
            className="text-indigo-600"
          />

          <p className="font-semibold text-indigo-700">
            Recommended Focus
          </p>

        </div>


        <h3 className="mt-3 text-2xl font-bold text-slate-900">
          {mainFocus}
        </h3>


        <p className="mt-3 text-gray-600">

          Improve your{" "}

          <span className="font-semibold text-slate-800">
            {mainFocus}
          </span>

          {" "}before your next{" "}

          <span className="font-semibold text-indigo-700">
            {targetCompany}
          </span>

          {" "}{targetRole} interview.

        </p>


        {weakestArea && (

          <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 text-sm font-semibold text-indigo-700">

            <TrendingUp size={16} />

            Current score:{" "}

            {Math.round(
              weakestArea.score
            )}

            %

          </div>

        )}

      </div>


      {/* ---------- Resume Weak Topics ---------- */}

      {displayedWeakTopics.length > 0 && (

        <div className="mt-6">

          <div className="flex items-center gap-2">

            <AlertTriangle
              size={18}
              className="text-amber-600"
            />

            <h3 className="font-semibold text-slate-900">
              Resume-Based Improvement Areas
            </h3>

          </div>


          <div className="mt-4 space-y-3">

            {displayedWeakTopics.map(
              (topic, index) => (

                <div
                  key={`${topic}-${index}`}
                  className="rounded-xl border border-amber-100 bg-amber-50 p-4"
                >

                  <div className="flex items-start gap-3">

                    <span className="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-amber-100 text-xs font-bold text-amber-700">
                      {index + 1}
                    </span>

                    <p className="text-sm leading-6 text-slate-700">
                      {topic}
                    </p>

                  </div>

                </div>

              )
            )}

          </div>

        </div>

      )}


      {/* ---------- Performance Snapshot ---------- */}

      {hasInterviewScores && (

        <div className="mt-6">

          <h3 className="font-semibold text-slate-900">
            Latest Performance Snapshot
          </h3>


          <div className="mt-4 grid grid-cols-3 gap-3">

            <div className="rounded-xl bg-slate-50 p-4 text-center">

              <p className="text-xs text-slate-500">
                Technical
              </p>

              <p className="mt-1 text-xl font-bold text-slate-900">
                {Math.round(technicalScore)}%
              </p>

            </div>


            <div className="rounded-xl bg-slate-50 p-4 text-center">

              <p className="text-xs text-slate-500">
                Communication
              </p>

              <p className="mt-1 text-xl font-bold text-slate-900">
                {Math.round(communicationScore)}%
              </p>

            </div>


            <div className="rounded-xl bg-slate-50 p-4 text-center">

              <p className="text-xs text-slate-500">
                Confidence
              </p>

              <p className="mt-1 text-xl font-bold text-slate-900">
                {Math.round(confidenceScore)}%
              </p>

            </div>

          </div>

        </div>

      )}

    </div>
  );
}