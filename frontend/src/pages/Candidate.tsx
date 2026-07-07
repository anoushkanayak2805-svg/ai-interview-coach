import { useState } from "react";
import Navbar from "../components/layout/Navbar";
import { uploadResume } from "../api/resume";

export default function Candidate() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleUpload() {
    if (!file) {
      alert("Please select a resume.");
      return;
    }

    try {
      setLoading(true);

      await uploadResume(file);

      alert("Resume uploaded successfully!");
    } catch (error) {
      console.error(error);
      alert("Resume upload failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <div className="mx-auto max-w-6xl px-8 py-8">
        <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-blue-600 p-8 text-white shadow-lg">
          <h1 className="text-4xl font-bold">Candidate Profile</h1>

          <p className="mt-3">
            Upload your resume to personalize your AI interview experience.
          </p>
        </div>

        <div className="mt-8 rounded-3xl bg-white p-8 shadow-lg">
          <h2 className="text-2xl font-bold">Resume Upload</h2>

          <input
            type="file"
            accept=".pdf"
            className="mt-6 w-full rounded-xl border p-4"
            onChange={(e) =>
              setFile(e.target.files?.[0] ?? null)
            }
          />

          <button
            onClick={handleUpload}
            disabled={loading}
            className="mt-6 rounded-xl bg-indigo-600 px-8 py-3 text-white transition hover:bg-indigo-700 disabled:opacity-50"
          >
            {loading ? "Uploading..." : "Upload Resume"}
          </button>
        </div>
      </div>
    </div>
  );
}