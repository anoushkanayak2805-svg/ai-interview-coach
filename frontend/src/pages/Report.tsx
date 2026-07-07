import { useEffect, useState } from "react";
import Navbar from "../components/layout/Navbar";
import { getReports, Report } from "../api/report";

export default function ReportPage() {

  const [reports, setReports] =
    useState<Report[]>([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    async function loadReports() {

      try {

        const data = await getReports();

        setReports(data);

      } catch (err) {

        console.error(err);

      } finally {

        setLoading(false);

      }

    }

    loadReports();

  }, []);

  if (loading) {

    return (
      <div className="flex min-h-screen items-center justify-center">
        Loading Reports...
      </div>
    );

  }

  return (

    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto max-w-7xl px-8 py-8">

        <h1 className="text-4xl font-bold">
          Interview Reports
        </h1>

        <p className="mt-2 text-gray-500">
          Review your interview performance.
        </p>

        <div className="mt-8 space-y-6">

          {reports.map((report) => (

            <div
              key={report.id}
              className="rounded-3xl bg-white p-8 shadow-lg"
            >

              <div className="flex items-center justify-between">

                <div>

                  <h2 className="text-2xl font-bold">

                    {report.company}

                  </h2>

                  <p className="text-gray-500">

                    {report.role}

                  </p>

                </div>

                <div className="rounded-full bg-indigo-100 px-5 py-2 text-xl font-bold text-indigo-700">

                  {report.overall_score}%

                </div>

              </div>

              <div className="mt-8 grid grid-cols-2 gap-6">

                <div>

                  <p className="text-sm text-gray-500">

                    Technical

                  </p>

                  <h3 className="text-2xl font-bold">

                    {report.technical_score}%

                  </h3>

                </div>

                <div>

                  <p className="text-sm text-gray-500">

                    Communication

                  </p>

                  <h3 className="text-2xl font-bold">

                    {report.communication_score}%

                  </h3>

                </div>

              </div>

              <div className="mt-8 rounded-2xl bg-slate-100 p-6">

                <h3 className="font-semibold">

                  AI Feedback

                </h3>

                <p className="mt-3 text-gray-600">

                  {report.feedback}

                </p>

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>

  );

}