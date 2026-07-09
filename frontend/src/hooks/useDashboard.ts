import { useEffect, useState } from "react";

import {
  getDashboard,
  type DashboardData,
} from "../api/dashboard";

export function useDashboard() {
  const [data, setData] =
    useState<DashboardData | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);
        setError("");

        const result = await getDashboard();

        setData(result);
      } catch (error) {
        console.error(
          "Unable to load dashboard:",
          error
        );

        setError(
          "Unable to load dashboard."
        );
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