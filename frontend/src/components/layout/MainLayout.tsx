import type { ReactNode } from "react";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

type Props = {
  children: ReactNode;
};

export default function MainLayout({
  children,
}: Props) {
  return (
    <div className="flex bg-slate-100">

      <Sidebar />

      <div className="flex min-h-screen flex-1 flex-col">

        <Topbar />

        <main className="flex-1 p-8">

          {children}

        </main>

      </div>

    </div>
  );
}