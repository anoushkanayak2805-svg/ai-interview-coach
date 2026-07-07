import { useEffect, useState } from "react";

import Navbar from "../components/layout/Navbar";

import HeroBanner from "../components/dashboard/HeroBanner";
import StatsSection from "../components/dashboard/StatsSection";
import QuickActions from "../components/dashboard/QuickActions";
import RecentInterviews from "../components/dashboard/RecentInterviews";
import CandidateProfileCard from "../components/dashboard/CandidateProfileCard";
import GoalCard from "../components/dashboard/GoalCard";
import AICoachCard from "../components/dashboard/AICoachCard";

import { getDashboard } from "../api/dashboard";

export default function Dashboard() {

  const [dashboardData, setDashboardData] = useState({
    interviews: [],
    reports: [],
  });

  useEffect(() => {

    async function loadDashboard() {

      try {

        const data = await getDashboard();

        setDashboardData(data);

      } catch (error) {

        console.error(error);

      }

    }

    loadDashboard();

  }, []);

  const interviewCount = dashboardData.interviews.length;

  const averageScore =
    dashboardData.reports.length > 0
      ? Math.round(
          dashboardData.reports.reduce(
            (sum: number, report: any) =>
              sum + (report.overall_score ?? 0),
            0
          ) / dashboardData.reports.length
        )
      : 0;

  const targetCompany =
    dashboardData.interviews.length > 0
      ? dashboardData.interviews[0].company
      : "Not Set";

  // We'll replace this later when the backend exposes streak data
  const practiceStreak = 7;

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <main className="mx-auto max-w-7xl px-6 py-8 lg:px-8">

        {/* Greeting */}

        <section className="mb-8">

          <p className="text-sm font-medium uppercase tracking-widest text-indigo-600">
            Dashboard
          </p>

          <h1 className="mt-2 text-4xl font-bold text-slate-900">
            Good Afternoon 👋
          </h1>

          <p className="mt-2 text-lg text-slate-500">
            Welcome back! Continue preparing for your next dream job.
          </p>

        </section>

        {/* Hero */}

        <HeroBanner />

        {/* Statistics */}

        <section className="mt-10">

          <StatsSection
            interviews={interviewCount}
            averageScore={averageScore}
            targetCompany={targetCompany}
            practiceStreak={practiceStreak}
          />

        </section>

        {/* Quick Actions */}

        <section className="mt-10">

          <QuickActions />

        </section>

        {/* Main Grid */}

        <section className="mt-10 grid grid-cols-1 gap-8 xl:grid-cols-3">

          {/* Left */}

          <div className="space-y-8 xl:col-span-2">

            <RecentInterviews />

            <AICoachCard />

          </div>

          {/* Right */}

          <div className="space-y-8">

            <CandidateProfileCard />

            <GoalCard />

          </div>

        </section>

      </main>

    </div>
  );
}