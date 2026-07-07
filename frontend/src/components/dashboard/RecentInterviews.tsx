const interviews = [
  {
    company: "Google",
    role: "Software Engineer",
    score: "90%",
    color: "bg-green-100 text-green-700",
  },
  {
    company: "Amazon",
    role: "SDE I",
    score: "82%",
    color: "bg-yellow-100 text-yellow-700",
  },
  {
    company: "Microsoft",
    role: "Backend Engineer",
    score: "88%",
    color: "bg-blue-100 text-blue-700",
  },
];

export default function RecentInterviews() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <div className="mb-8 flex items-center justify-between">

        <h2 className="text-2xl font-bold">
          Recent Interviews
        </h2>

        <button className="text-indigo-600 hover:underline">
          View History
        </button>

      </div>

      <div className="space-y-5">

        {interviews.map((item) => (
          <div
            key={`${item.company}-${item.role}`}
            className="flex items-center justify-between rounded-2xl border border-slate-200 p-5 transition hover:-translate-y-1 hover:shadow-md"
          >
            <div>

              <h3 className="font-semibold">
                {item.company}
              </h3>

              <p className="text-sm text-gray-500">
                {item.role}
              </p>

            </div>

            <span
              className={`rounded-full px-4 py-2 font-semibold ${item.color}`}
            >
              {item.score}
            </span>

          </div>
        ))}

      </div>

    </div>
  );
}