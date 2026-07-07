import { Bell } from "lucide-react";

export default function Topbar() {
  return (
    <header className="flex items-center justify-between border-b bg-white px-10 py-6">

      <div>

        <h1 className="text-3xl font-bold">

          Good Afternoon 👋

        </h1>

        <p className="text-gray-500">

          Ready for today's interview?

        </p>

      </div>

      <button className="rounded-full border p-3 hover:bg-slate-100">

        <Bell size={20} />

      </button>

    </header>
  );
}