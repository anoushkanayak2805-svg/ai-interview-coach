type DashboardCardProps = {
  title: string;
  value: string;
};

export default function DashboardCard({
  title,
  value,
}: DashboardCardProps) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow hover:shadow-lg transition">
      <h3 className="text-gray-500 text-sm">{title}</h3>

      <p className="mt-3 text-3xl font-bold">
        {value}
      </p>
    </div>
  );
}