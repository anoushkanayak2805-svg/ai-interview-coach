import api from "./axios";

export async function getDashboard() {
  try {
    const interviewsPromise = api.get("/interviews");

    const reportsPromise = api
      .get("/reports")
      .catch(() => ({ data: [] }));

    const [interviews, reports] = await Promise.all([
      interviewsPromise,
      reportsPromise,
    ]);

    return {
      interviews: interviews.data,
      reports: reports.data,
    };
  } catch (error) {
    console.error(error);

    return {
      interviews: [],
      reports: [],
    };
  }
}