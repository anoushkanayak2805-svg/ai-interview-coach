export default function CandidateHeader() {
  return (
    <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-blue-600 p-8 text-white shadow-lg">

      <p className="text-indigo-100 uppercase tracking-widest text-sm">
        AI Candidate Profile
      </p>

      <h1 className="mt-3 text-4xl font-bold">
        Candidate Overview
      </h1>

      <p className="mt-3 text-indigo-100">
        Your interview profile generated from your resume and interview history.
      </p>

    </div>
  );
}