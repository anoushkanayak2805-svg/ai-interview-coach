export default function GoalCard() {
  return (
    <div className="rounded-3xl bg-gradient-to-br from-indigo-600 to-blue-600 p-8 text-white shadow-lg">

      <h2 className="text-2xl font-bold">
        Today's Goal
      </h2>

      <p className="mt-6">
        Complete one Google Software Engineer interview.
      </p>

      <div className="mt-6 h-3 rounded-full bg-white/20">

        <div className="h-3 w-3/4 rounded-full bg-white"></div>

      </div>

      <p className="mt-3 text-sm">
        75% Completed
      </p>

    </div>
  );
}