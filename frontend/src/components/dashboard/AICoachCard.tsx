import { Sparkles } from "lucide-react";

export default function AICoachCard() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <div className="flex items-center gap-3">

        <Sparkles className="text-indigo-600" />

        <h2 className="text-2xl font-bold">
          AI Coach
        </h2>

      </div>

      <div className="mt-6 rounded-2xl bg-indigo-50 p-6">

        <p className="font-semibold text-indigo-700">
          Recommended Focus
        </p>

        <h3 className="mt-2 text-2xl font-bold">
          Operating Systems
        </h3>

        <p className="mt-3 text-gray-600">
          Improve Operating Systems before your next
          Google interview.
        </p>

      </div>

    </div>
  );
}