import api from "./axios";

export interface DashboardData {
  interviews: any[];
  reports: any[];
}

export async function getDashboard(): Promise<DashboardData> {
  const [interviews, reports] = await Promise.all([
    api.get("/interviews"),
    api.get("/reports"),
  ]);

  return {
    interviews: interviews.data,
    reports: reports.data,
  };
}