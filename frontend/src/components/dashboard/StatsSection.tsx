import DashboardCard from "./DashboardCard";

interface StatsSectionProps {
  interviews: number;
  averageScore: number;
  targetCompany: string;
  practiceStreak: number;
}

export default function StatsSection({
  interviews,
  averageScore,
  targetCompany,
  practiceStreak,
}: StatsSectionProps) {
  return (
    <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">

      <DashboardCard
        title="Interviews"
        value={String(interviews)}
      />

      <DashboardCard
        title="Average Score"
        value={`${averageScore}%`}
      />

      <DashboardCard
        title="Target Company"
        value={targetCompany}
      />

      <DashboardCard
        title="Practice Streak"
        value={`${practiceStreak} Days`}
      />

    </div>
  );
}