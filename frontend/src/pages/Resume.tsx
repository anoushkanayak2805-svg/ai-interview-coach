import Navbar from "../components/layout/Navbar";

export default function Resume() {
  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <div className="mx-auto max-w-5xl p-8">

        <h1 className="text-4xl font-bold">
          Resume
        </h1>

        <p className="mt-2 text-gray-500">
          Upload your latest resume for AI analysis.
        </p>

        <div className="mt-10 rounded-2xl bg-white p-8 shadow">

          <h2 className="text-2xl font-semibold">
            Upload Resume
          </h2>

          <input
            type="file"
            accept=".pdf"
            className="mt-6 block w-full rounded-lg border p-3"
          />

          <button
            className="mt-6 rounded-xl bg-blue-600 px-8 py-3 font-semibold text-white hover:bg-blue-700"
          >
            Upload Resume
          </button>

        </div>

      </div>
    </div>
  );
}