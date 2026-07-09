import { useEffect, useState } from "react";

import Navbar from "../components/layout/Navbar";

import HeroBanner from "../components/dashboard/HeroBanner";
import StatsSection from "../components/dashboard/StatsSection";
import QuickActions from "../components/dashboard/QuickActions";
import RecentInterviews from "../components/dashboard/RecentInterviews";
import CandidateProfileCard from "../components/dashboard/CandidateProfileCard";
import GoalCard from "../components/dashboard/GoalCard";
import AICoachCard from "../components/dashboard/AICoachCard";

import {
  getDashboard,
  type DashboardData,
} from "../api/dashboard";

import {
  getMyResume,
  type ResumeResponse,
} from "../api/resume";


const initialDashboardData: DashboardData = {
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


export default function Dashboard() {
  /* ---------------------------------
     Dashboard State
  ---------------------------------- */

  const [dashboardData, setDashboardData] =
    useState<DashboardData>(
      initialDashboardData
    );


  /* ---------------------------------
     Resume State
  ---------------------------------- */

  const [resume, setResume] =
    useState<ResumeResponse | null>(
      null
    );


  /* ---------------------------------
     UI State
  ---------------------------------- */

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState<string | null>(null);


  /* ---------------------------------
     Load Dashboard + Resume
  ---------------------------------- */

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);

        setError(null);

        /*
          Load dashboard and resume
          simultaneously.
        */

        const [
          dashboardResult,
          resumeResult,
        ] = await Promise.allSettled([
          getDashboard(),
          getMyResume(),
        ]);


        /* ---------- Dashboard ---------- */

        if (
          dashboardResult.status ===
          "fulfilled"
        ) {
          setDashboardData(
            dashboardResult.value
          );
        } else {
          console.error(
            "Dashboard loading error:",
            dashboardResult.reason
          );

          setError(
            "Unable to load some dashboard data."
          );
        }


        /* ---------- Resume ---------- */

        if (
          resumeResult.status ===
          "fulfilled"
        ) {
          setResume(
            resumeResult.value
          );
        } else {
          console.log(
            "No resume available:",
            resumeResult.reason
          );

          setResume(null);
        }

      } catch (error) {
        console.error(
          "Dashboard loading error:",
          error
        );

        setError(
          "Unable to load dashboard data."
        );

      } finally {
        setLoading(false);
      }
    }

    loadDashboard();

  }, []);


  /* ---------------------------------
     Greeting
  ---------------------------------- */

  const hour =
    new Date().getHours();

  let greeting =
    "Good Evening";

  if (hour < 12) {
    greeting =
      "Good Morning";

  } else if (hour < 17) {
    greeting =
      "Good Afternoon";
  }


  /* ---------------------------------
     Dashboard Values
  ---------------------------------- */

  const interviewCount =
    dashboardData.stats.totalInterviews;


  const averageScore =
    dashboardData.stats.averageScore;


  /*
    Prefer latest report company because
    it represents the most recently completed
    interview.

    Fall back to newest interview.
  */

  const targetCompany =
    dashboardData.latestReport?.company ??
    dashboardData.interviews[0]?.company ??
    "Not Set";


  const targetRole =
    dashboardData.latestReport?.role ??
    dashboardData.interviews[0]?.role ??
    "Software Engineer";


  /*
    Practice streak backend logic
    can be added later.
  */

  const practiceStreak = 0;


  /* ---------------------------------
     Resume Intelligence Values
  ---------------------------------- */

  const resumeWeakTopics =
    resume?.analysis?.weak_topics ?? [];


  /* ---------------------------------
     Loading State
  ---------------------------------- */

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-100">

        <Navbar />

        <div className="flex min-h-[70vh] items-center justify-center">

          <div className="text-center">

            <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-slate-200 border-t-indigo-600" />

            <p className="mt-5 text-lg font-medium text-slate-600">
              Loading your dashboard...
            </p>

          </div>

        </div>

      </div>
    );
  }


  /* ---------------------------------
     Dashboard UI
  ---------------------------------- */

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />


      <main className="mx-auto max-w-7xl px-6 py-8 lg:px-8">


        {/* ---------- Greeting ---------- */}

        <section className="mb-8">

          <p className="text-sm font-medium uppercase tracking-widest text-indigo-600">
            Dashboard
          </p>

          <h1 className="mt-2 text-4xl font-bold text-slate-900">
            {greeting} 👋
          </h1>

          <p className="mt-2 text-lg text-slate-500">
            Welcome back! Continue preparing for your next dream job.
          </p>

        </section>


        {/* ---------- Error Message ---------- */}

        {error && (
          <div className="mb-8 rounded-2xl border border-red-200 bg-red-50 p-5 text-red-700">
            {error}
          </div>
        )}


        {/* ---------- Hero ---------- */}

        <HeroBanner />


        {/* ---------- Statistics ---------- */}

        <section className="mt-10">

          <StatsSection
            interviews={interviewCount}
            averageScore={averageScore}
            targetCompany={targetCompany}
            practiceStreak={practiceStreak}
          />

        </section>


        {/* ---------- Latest Performance ---------- */}

        {dashboardData.latestReport && (

          <section className="mt-10">

            <div className="rounded-3xl bg-white p-8 shadow-lg">

              <div className="flex flex-col justify-between gap-4 md:flex-row md:items-center">

                <div>

                  <p className="text-sm font-semibold uppercase tracking-wider text-indigo-600">
                    Latest Performance
                  </p>

                  <h2 className="mt-2 text-2xl font-bold text-slate-900">

                    {
                      dashboardData
                        .latestReport
                        .company
                    }

                    {" · "}

                    {
                      dashboardData
                        .latestReport
                        .role
                    }

                  </h2>

                </div>


                <div className="rounded-2xl bg-indigo-100 px-6 py-3 text-center">

                  <p className="text-sm font-medium text-indigo-600">
                    Overall Score
                  </p>

                  <p className="text-3xl font-bold text-indigo-700">

                    {
                      Math.round(
                        Number(
                          dashboardData
                            .latestReport
                            .overall_score
                        )
                      )
                    }

                    %

                  </p>

                </div>

              </div>


              {/* ---------- Scores ---------- */}

              <div className="mt-8 grid grid-cols-1 gap-5 md:grid-cols-3">

                <div className="rounded-2xl bg-slate-50 p-5">

                  <p className="text-sm text-slate-500">
                    Technical
                  </p>

                  <p className="mt-2 text-3xl font-bold text-slate-900">

                    {
                      Math.round(
                        dashboardData
                          .stats
                          .latestTechnicalScore
                      )
                    }

                    %

                  </p>

                </div>


                <div className="rounded-2xl bg-slate-50 p-5">

                  <p className="text-sm text-slate-500">
                    Communication
                  </p>

                  <p className="mt-2 text-3xl font-bold text-slate-900">

                    {
                      Math.round(
                        dashboardData
                          .stats
                          .latestCommunicationScore
                      )
                    }

                    %

                  </p>

                </div>


                <div className="rounded-2xl bg-slate-50 p-5">

                  <p className="text-sm text-slate-500">
                    Confidence
                  </p>

                  <p className="mt-2 text-3xl font-bold text-slate-900">

                    {
                      Math.round(
                        dashboardData
                          .stats
                          .latestConfidenceScore
                      )
                    }

                    %

                  </p>

                </div>

              </div>


              {/* ---------- Recommended Focus ---------- */}

              <div className="mt-6 rounded-2xl bg-amber-50 p-5">

                <p className="text-sm font-semibold text-amber-700">
                  Recommended Focus
                </p>

                <p className="mt-2 text-lg font-bold text-slate-900">

                  {
                    dashboardData
                      .recommendedFocus
                  }

                </p>

              </div>

            </div>

          </section>

        )}


        {/* ---------- Quick Actions ---------- */}

        <section className="mt-10">

          <QuickActions />

        </section>


        {/* ---------- Main Grid ---------- */}

        <section className="mt-10 grid grid-cols-1 gap-8 xl:grid-cols-3">


          {/* ---------- Left Column ---------- */}

          <div className="space-y-8 xl:col-span-2">


            <RecentInterviews
              interviews={
                dashboardData.interviews
              }
              reports={
                dashboardData.reports
              }
            />


            {/* ---------- Personalized AI Coach ---------- */}

            <AICoachCard
              recommendedFocus={
                dashboardData.recommendedFocus
              }

              weakTopics={
                resumeWeakTopics
              }

              targetCompany={
                targetCompany
              }

              targetRole={
                targetRole
              }

              technicalScore={
                dashboardData
                  .stats
                  .latestTechnicalScore
              }

              communicationScore={
                dashboardData
                  .stats
                  .latestCommunicationScore
              }

              confidenceScore={
                dashboardData
                  .stats
                  .latestConfidenceScore
              }
            />


          </div>


          {/* ---------- Right Column ---------- */}

          <div className="space-y-8">


            <CandidateProfileCard
              resumeUploaded={
                Boolean(resume)
              }

              filename={
                resume?.file_name ?? ""
              }

              skills={
                resume?.skills ?? []
              }

              projects={
                resume?.projects ?? []
              }

              analysis={
                resume?.analysis ?? null
              }

              recommendedCompany={
                targetCompany
              }
            />


            <GoalCard />

          </div>


        </section>


      </main>

    </div>
  );
}