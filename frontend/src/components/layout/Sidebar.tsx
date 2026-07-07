import {
  LayoutDashboard,
  User,
  Building2,
  Mic2,
  BarChart3,
  Settings,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menu = [
  {
    title: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Candidate",
    path: "/candidate",
    icon: User,
  },
  {
    title: "Companies",
    path: "/companies",
    icon: Building2,
  },
  {
    title: "Interviews",
    path: "/interviews",
    icon: Mic2,
  },
  {
    title: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    title: "Profile",
    path: "/profile",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="flex h-screen w-72 flex-col bg-slate-900 text-white">

      <div className="border-b border-slate-800 p-8">

        <h1 className="text-2xl font-bold">
          InterviewAI
        </h1>

        <p className="mt-1 text-sm text-slate-400">
          AI Career Platform
        </p>

      </div>

      <nav className="flex-1 space-y-2 p-5">

        {menu.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-4 rounded-xl px-4 py-3 transition-all ${
                  isActive
                    ? "bg-indigo-600"
                    : "hover:bg-slate-800"
                }`
              }
            >
              <Icon size={20} />

              <span>{item.title}</span>

            </NavLink>

          );

        })}

      </nav>

      <div className="border-t border-slate-800 p-6">

        <div className="rounded-xl bg-slate-800 p-4">

          <p className="text-sm text-slate-400">

            Practice Streak

          </p>

          <h2 className="mt-2 text-3xl font-bold">

            🔥 7 Days

          </h2>

        </div>

      </div>

    </aside>
  );
}