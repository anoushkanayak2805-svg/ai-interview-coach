import { useNavigate } from "react-router-dom";

export default function QuickActions() {
  const navigate = useNavigate();

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">

      <button
        onClick={() => navigate("/resume")}
        className="rounded-2xl bg-blue-600 p-8 text-white hover:bg-blue-700 transition"
      >
        📄 Upload Resume
      </button>

      <button
        onClick={() => navigate("/interviews/create")}
        className="rounded-2xl bg-emerald-600 p-8 text-white hover:bg-emerald-700 transition"
      >
        🎤 Start Interview
      </button>

    </div>
  );
}