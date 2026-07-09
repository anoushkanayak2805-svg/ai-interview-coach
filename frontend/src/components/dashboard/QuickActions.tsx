import { useNavigate } from "react-router-dom";

export default function QuickActions() {
  const navigate = useNavigate();

  return (
    <div className="mt-10 grid grid-cols-1 gap-6 md:grid-cols-2">

      <button
        onClick={() => navigate("/candidate")}
        className="rounded-2xl bg-blue-600 p-8 text-white transition hover:bg-blue-700"
      >
        📄 Upload Resume
      </button>

      <button
        onClick={() => navigate("/interviews/create")}
        className="rounded-2xl bg-emerald-600 p-8 text-white transition hover:bg-emerald-700"
      >
        🎤 Start Interview
      </button>

    </div>
  );
}