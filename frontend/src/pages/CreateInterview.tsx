import { useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";

import Navbar from "../components/layout/Navbar";
import { createInterview } from "../api/interview";

const companies = [
  "Google",
  "Microsoft",
  "Amazon",
  "Adobe",
  "Atlassian",
  "Netflix",
  "Uber",
  "Salesforce",
];

const roles = [
  "Software Engineer",
  "Frontend Developer",
  "Backend Developer",
  "Full Stack Developer",
  "Machine Learning Engineer",
];

export default function CreateInterview() {
  const navigate = useNavigate();
  const [params] = useSearchParams();

  const [loading, setLoading] = useState(false);

  const [duration, setDuration] = useState("45");

  const [formData, setFormData] = useState({
    title: "",
    company: params.get("company") || "Google",
    role: "Software Engineer",
    interview_type: "Technical",
    difficulty: "Medium",
  });

  async function handleSubmit(
    e: React.FormEvent<HTMLFormElement>
  ) {
    e.preventDefault();

    if (!formData.title.trim()) {
      alert("Please enter an interview title.");
      return;
    }

    try {
      setLoading(true);

      const interview = await createInterview(formData);

      navigate(`/interview/${interview.id}`);
    } catch (error) {
      console.error(error);
      alert("Unable to create interview.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <div className="mx-auto max-w-4xl px-8 py-10">

        <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-blue-600 p-8 text-white shadow-xl">

          <h1 className="text-4xl font-bold">
            Create AI Interview
          </h1>

          <p className="mt-3 text-indigo-100">
            Configure your personalized interview session.
          </p>

        </div>

        <form
          onSubmit={handleSubmit}
          className="mt-8 rounded-3xl bg-white p-8 shadow-xl space-y-6"
        >

          <div>

            <label className="font-semibold">
              Interview Title
            </label>

            <input
              className="mt-2 w-full rounded-xl border p-4"
              placeholder="Google SDE Interview"
              value={formData.title}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  title: e.target.value,
                })
              }
            />

          </div>

          <div className="grid gap-6 md:grid-cols-2">

            <div>

              <label className="font-semibold">
                Company
              </label>

              <select
                className="mt-2 w-full rounded-xl border p-4"
                value={formData.company}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    company: e.target.value,
                  })
                }
              >

                {companies.map((company) => (
                  <option key={company}>
                    {company}
                  </option>
                ))}

              </select>

            </div>

            <div>

              <label className="font-semibold">
                Role
              </label>

              <select
                className="mt-2 w-full rounded-xl border p-4"
                value={formData.role}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    role: e.target.value,
                  })
                }
              >

                {roles.map((role) => (
                  <option key={role}>
                    {role}
                  </option>
                ))}

              </select>

            </div>

          </div>

          <div className="grid gap-6 md:grid-cols-3">

            <div>

              <label className="font-semibold">
                Interview Type
              </label>

              <select
                className="mt-2 w-full rounded-xl border p-4"
                value={formData.interview_type}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    interview_type: e.target.value,
                  })
                }
              >

                <option>Technical</option>
                <option>Behavioral</option>
                <option>Mixed</option>

              </select>

            </div>

            <div>

              <label className="font-semibold">
                Difficulty
              </label>

              <select
                className="mt-2 w-full rounded-xl border p-4"
                value={formData.difficulty}
                onChange={(e) =>
                  setFormData({
                    ...formData,
                    difficulty: e.target.value,
                  })
                }
              >

                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>

              </select>

            </div>

            <div>

              <label className="font-semibold">
                Duration
              </label>

              <select
                className="mt-2 w-full rounded-xl border p-4"
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
              >

                <option value="30">30 Minutes</option>
                <option value="45">45 Minutes</option>
                <option value="60">60 Minutes</option>

              </select>

            </div>

          </div>

          <button
            disabled={loading}
            className="w-full rounded-xl bg-indigo-600 py-4 text-lg font-semibold text-white transition hover:bg-indigo-700 disabled:opacity-50"
          >
            {loading
              ? "Creating Interview..."
              : "Start AI Interview"}
          </button>

        </form>

      </div>
    </div>
  );
}