import Navbar from "../components/layout/Navbar";

export default function Analytics() {
  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto max-w-7xl px-8 py-8">

        <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-blue-600 p-8 text-white shadow-xl">

          <h1 className="text-4xl font-bold">
            Performance Analytics
          </h1>

          <p className="mt-3 text-indigo-100">
            Track your interview progress and identify improvement areas.
          </p>

        </div>

        {/* Score Cards */}

        <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">

          <div className="rounded-3xl bg-white p-8 shadow-lg">
            <p className="text-gray-500">Overall Score</p>
            <h2 className="mt-2 text-4xl font-bold text-indigo-600">
              84%
            </h2>
          </div>

          <div className="rounded-3xl bg-white p-8 shadow-lg">
            <p className="text-gray-500">Technical</p>
            <h2 className="mt-2 text-4xl font-bold text-green-600">
              88%
            </h2>
          </div>

          <div className="rounded-3xl bg-white p-8 shadow-lg">
            <p className="text-gray-500">Communication</p>
            <h2 className="mt-2 text-4xl font-bold text-blue-600">
              80%
            </h2>
          </div>

          <div className="rounded-3xl bg-white p-8 shadow-lg">
            <p className="text-gray-500">Interviews</p>
            <h2 className="mt-2 text-4xl font-bold text-orange-600">
              12
            </h2>
          </div>

        </div>

        {/* Strengths & Weaknesses */}

        <div className="mt-10 grid gap-8 lg:grid-cols-2">

          <div className="rounded-3xl bg-white p-8 shadow-lg">

            <h2 className="text-2xl font-bold">
              Strong Areas
            </h2>

            <div className="mt-6 flex flex-wrap gap-3">

              {["DBMS", "SQL", "React", "OOP"].map((item) => (
                <span
                  key={item}
                  className="rounded-full bg-green-100 px-4 py-2 text-green-700"
                >
                  {item}
                </span>
              ))}

            </div>

          </div>

          <div className="rounded-3xl bg-white p-8 shadow-lg">

            <h2 className="text-2xl font-bold">
              Needs Improvement
            </h2>

            <div className="mt-6 flex flex-wrap gap-3">

              {["Operating Systems", "System Design"].map((item) => (
                <span
                  key={item}
                  className="rounded-full bg-red-100 px-4 py-2 text-red-700"
                >
                  {item}
                </span>
              ))}

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}