import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import Navbar from "../components/layout/Navbar";

import {
  getReport,
  getReports,
} from "../api/report";

import type { Report as ReportType } from "../api/report";


function formatContent(
  value: string | string[] | undefined
): string {
  if (!value) {
    return "Not available";
  }

  if (Array.isArray(value)) {
    return value.join(", ");
  }

  return value;
}


export default function Report() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [report, setReport] =
    useState<ReportType | null>(null);

  const [reports, setReports] =
    useState<ReportType[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");


  useEffect(() => {
    async function loadReportData() {
      try {
        setLoading(true);
        setError("");

        /*
          If URL is:

          /reports/14

          Fetch the report for interview 14.
        */

        if (id) {
          console.log(
            `Loading report for interview ${id}`
          );

          const data = await getReport(id);

          console.log(
            "========== REPORT RESPONSE =========="
          );

          console.log(data);

          console.log(
            "====================================="
          );

          setReport(data);

          return;
        }

        /*
          If URL is:

          /reports

          Try loading report history.

          Your backend currently does not have
          GET /reports, so getReports() may
          return an empty array.
        */

        const data = await getReports();

        setReports(data);

      } catch (err: any) {
        console.error(
          "Failed to load report:",
          err
        );

        if (err.response?.status === 404) {
          setError(
            "Report not found for this interview."
          );
        } else if (err.response?.status === 401) {
          setError(
            "Your session has expired. Please log in again."
          );
        } else if (err.response?.status === 500) {
          setError(
            "Unable to generate the interview report. Please check the backend logs."
          );
        } else {
          setError(
            err.response?.data?.detail ||
              "Unable to load the interview report."
          );
        }

      } finally {
        setLoading(false);
      }
    }

    loadReportData();

  }, [id]);


  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-slate-100">

        <div className="text-center">

          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-slate-300 border-t-indigo-600" />

          <h2 className="mt-6 text-xl font-semibold text-slate-800">
            Generating Your AI Interview Report...
          </h2>

          <p className="mt-2 text-slate-500">
            Analyzing your technical performance,
            communication, confidence, and overall interview.
          </p>

        </div>

      </div>
    );
  }


  if (error) {
    return (
      <div className="min-h-screen bg-slate-100">

        <Navbar />

        <div className="mx-auto max-w-3xl px-6 py-20">

          <div className="rounded-3xl bg-white p-10 text-center shadow-lg">

            <div className="text-5xl">
              ⚠️
            </div>

            <h1 className="mt-5 text-3xl font-bold text-slate-900">
              Unable to Load Report
            </h1>

            <p className="mt-4 text-slate-500">
              {error}
            </p>

            <div className="mt-8 flex justify-center gap-4">

              <button
                onClick={() =>
                  window.location.reload()
                }
                className="rounded-xl bg-indigo-600 px-6 py-3 font-medium text-white transition hover:bg-indigo-700"
              >
                Retry
              </button>

              <button
                onClick={() =>
                  navigate("/dashboard")
                }
                className="rounded-xl border border-slate-300 px-6 py-3 font-medium text-slate-700 transition hover:bg-slate-50"
              >
                Dashboard
              </button>

            </div>

          </div>

        </div>

      </div>
    );
  }


  /*
    SINGLE INTERVIEW REPORT

    URL example:
    /reports/14
  */

  if (id && report) {
    return (
      <div className="min-h-screen bg-slate-100">

        <Navbar />

        <main className="mx-auto max-w-7xl px-6 py-10 lg:px-8">

          {/* Header */}

          <div className="flex flex-col justify-between gap-6 md:flex-row md:items-center">

            <div>

              <p className="text-sm font-semibold uppercase tracking-widest text-indigo-600">
                AI Performance Analysis
              </p>

              <h1 className="mt-2 text-4xl font-bold text-slate-900">
                Interview Report
              </h1>

              <p className="mt-2 text-slate-500">
                Detailed analysis of your interview performance.
              </p>

            </div>

            <button
              onClick={() =>
                navigate("/dashboard")
              }
              className="rounded-xl border border-slate-300 bg-white px-6 py-3 font-medium text-slate-700 shadow-sm transition hover:bg-slate-50"
            >
              Back to Dashboard
            </button>

          </div>


          {/* Overall Score */}

          <section className="mt-10 rounded-3xl bg-gradient-to-r from-indigo-600 to-blue-600 p-8 text-white shadow-xl">

            <div className="flex flex-col justify-between gap-8 md:flex-row md:items-center">

              <div>

                <p className="text-sm font-medium uppercase tracking-widest text-indigo-100">
                  Overall Performance
                </p>

                <h2 className="mt-3 text-4xl font-bold">
                  Interview Completed 🎉
                </h2>

                <p className="mt-3 max-w-2xl text-indigo-100">
                  Your interview responses have been analyzed across
                  technical ability, communication, and confidence.
                </p>

              </div>

              <div className="flex h-36 w-36 shrink-0 items-center justify-center rounded-full bg-white/20 backdrop-blur">

                <div className="text-center">

                  <p className="text-5xl font-bold">
                    {Math.round(
                      report.overall_score ?? 0
                    )}
                  </p>

                  <p className="mt-1 text-sm text-indigo-100">
                    Overall Score
                  </p>

                </div>

              </div>

            </div>

          </section>


          {/* Score Cards */}

          <section className="mt-8 grid gap-6 md:grid-cols-3">

            <div className="rounded-3xl bg-white p-7 shadow-lg">

              <p className="text-sm font-medium text-slate-500">
                Technical Score
              </p>

              <h3 className="mt-3 text-4xl font-bold text-emerald-600">
                {Math.round(
                  report.technical_score ?? 0
                )}%
              </h3>

              <div className="mt-5 h-2 overflow-hidden rounded-full bg-slate-100">

                <div
                  className="h-full rounded-full bg-emerald-500"
                  style={{
                    width: `${Math.min(
                      report.technical_score ?? 0,
                      100
                    )}%`,
                  }}
                />

              </div>

            </div>


            <div className="rounded-3xl bg-white p-7 shadow-lg">

              <p className="text-sm font-medium text-slate-500">
                Communication Score
              </p>

              <h3 className="mt-3 text-4xl font-bold text-blue-600">
                {Math.round(
                  report.communication_score ?? 0
                )}%
              </h3>

              <div className="mt-5 h-2 overflow-hidden rounded-full bg-slate-100">

                <div
                  className="h-full rounded-full bg-blue-500"
                  style={{
                    width: `${Math.min(
                      report.communication_score ?? 0,
                      100
                    )}%`,
                  }}
                />

              </div>

            </div>


            <div className="rounded-3xl bg-white p-7 shadow-lg">

              <p className="text-sm font-medium text-slate-500">
                Confidence Score
              </p>

              <h3 className="mt-3 text-4xl font-bold text-violet-600">
                {Math.round(
                  report.confidence_score ?? 0
                )}%
              </h3>

              <div className="mt-5 h-2 overflow-hidden rounded-full bg-slate-100">

                <div
                  className="h-full rounded-full bg-violet-500"
                  style={{
                    width: `${Math.min(
                      report.confidence_score ?? 0,
                      100
                    )}%`,
                  }}
                />

              </div>

            </div>

          </section>


          {/* Summary */}

          <section className="mt-8 rounded-3xl bg-white p-8 shadow-lg">

            <h2 className="text-2xl font-bold text-slate-900">
              AI Summary
            </h2>

            <p className="mt-4 leading-8 text-slate-600">
              {report.summary ||
                "No summary available."}
            </p>

          </section>


          {/* Strengths and Weaknesses */}

          <section className="mt-8 grid gap-8 lg:grid-cols-2">

            <div className="rounded-3xl bg-emerald-50 p-8">

              <h2 className="text-2xl font-bold text-emerald-800">
                Strengths
              </h2>

              <p className="mt-4 whitespace-pre-line leading-8 text-emerald-900">
                {formatContent(
                  report.strengths
                )}
              </p>

            </div>


            <div className="rounded-3xl bg-rose-50 p-8">

              <h2 className="text-2xl font-bold text-rose-800">
                Areas for Improvement
              </h2>

              <p className="mt-4 whitespace-pre-line leading-8 text-rose-900">
                {formatContent(
                  report.weaknesses
                )}
              </p>

            </div>

          </section>


          {/* Recommendations */}

          <section className="mt-8 rounded-3xl bg-indigo-50 p-8">

            <h2 className="text-2xl font-bold text-indigo-900">
              Recommendations
            </h2>

            <p className="mt-4 whitespace-pre-line leading-8 text-indigo-900">
              {formatContent(
                report.recommendations
              )}
            </p>

          </section>


          {/* Learning Roadmap */}

          <section className="mt-8 rounded-3xl bg-white p-8 shadow-lg">

            <h2 className="text-2xl font-bold text-slate-900">
              Personalized Learning Roadmap
            </h2>

            <p className="mt-4 whitespace-pre-line leading-8 text-slate-600">
              {formatContent(
                report.learning_roadmap
              )}
            </p>

          </section>


          {/* Hiring Recommendation */}

          <section className="mt-8 rounded-3xl bg-slate-900 p-8 text-white shadow-xl">

            <p className="text-sm font-medium uppercase tracking-widest text-slate-400">
              Final AI Assessment
            </p>

            <h2 className="mt-3 text-3xl font-bold">
              Hiring Recommendation
            </h2>

            <p className="mt-5 text-xl font-semibold text-indigo-300">
              {report.hiring_recommendation ||
                "Not available"}
            </p>

          </section>


          {/* Actions */}

          <section className="mt-10 flex flex-wrap justify-center gap-4 pb-10">

            <button
              onClick={() =>
                navigate("/interviews/create")
              }
              className="rounded-xl bg-indigo-600 px-7 py-3 font-medium text-white transition hover:bg-indigo-700"
            >
              Start Another Interview
            </button>

            <button
              onClick={() =>
                navigate("/dashboard")
              }
              className="rounded-xl border border-slate-300 bg-white px-7 py-3 font-medium text-slate-700 transition hover:bg-slate-50"
            >
              Back to Dashboard
            </button>

          </section>

        </main>

      </div>
    );
  }


  /*
    REPORT HISTORY

    URL:
    /reports
  */

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto max-w-7xl px-8 py-8">

        <h1 className="text-4xl font-bold text-slate-900">
          Interview Reports
        </h1>

        <p className="mt-2 text-slate-500">
          Review your interview performance.
        </p>

        {reports.length === 0 ? (

          <div className="mt-10 rounded-3xl bg-white p-12 text-center shadow-lg">

            <h2 className="text-2xl font-bold text-slate-900">
              No Reports Yet
            </h2>

            <p className="mt-3 text-slate-500">
              Complete an interview to generate your first AI performance report.
            </p>

            <button
              onClick={() =>
                navigate("/interviews/create")
              }
              className="mt-7 rounded-xl bg-indigo-600 px-7 py-3 font-medium text-white transition hover:bg-indigo-700"
            >
              Start Interview
            </button>

          </div>

        ) : (

          <div className="mt-8 grid gap-6">

            {reports.map((item) => (

              <button
                key={
                  item.id ??
                  item.interview_id
                }
                onClick={() =>
                  navigate(
                    `/reports/${item.interview_id}`
                  )
                }
                className="rounded-3xl bg-white p-8 text-left shadow-lg transition hover:-translate-y-1 hover:shadow-xl"
              >

                <div className="flex items-center justify-between">

                  <div>

                    <p className="text-sm font-medium uppercase tracking-wider text-indigo-600">
                      Interview #{item.interview_id}
                    </p>

                    <h2 className="mt-2 text-2xl font-bold text-slate-900">
                      Interview Report
                    </h2>

                  </div>

                  <div className="rounded-full bg-indigo-100 px-5 py-3 text-xl font-bold text-indigo-700">
                    {Math.round(
                      item.overall_score ?? 0
                    )}%
                  </div>

                </div>

              </button>

            ))}

          </div>

        )}

      </div>

    </div>
  );
}