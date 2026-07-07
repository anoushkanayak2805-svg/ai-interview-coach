import { useEffect, useState } from "react";
import {
  DashboardResponse,
  getDashboard,
} from "../api/dashboard";

export function useDashboard() {
  const [data, setData] =
    useState<DashboardResponse | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {

    async function loadDashboard() {

      try {

        const result = await getDashboard();

        setData(result);

      } catch {

        setError("Unable to load dashboard.");

      } finally {

        setLoading(false);

      }

    }

    loadDashboard();

  }, []);

  return {
    data,
    loading,
    error,
  };
}