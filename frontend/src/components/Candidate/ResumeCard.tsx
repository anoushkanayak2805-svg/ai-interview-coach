export default function ResumeCard() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <h2 className="text-2xl font-bold">
        Resume
      </h2>

      <div className="mt-6 flex items-center justify-between">

        <div>

          <p className="font-semibold">
            Resume Uploaded
          </p>

          <p className="text-sm text-gray-500">
            Last updated 2 days ago
          </p>

        </div>

        <button className="rounded-xl bg-indigo-600 px-5 py-2 text-white hover:bg-indigo-700">
          Upload New
        </button>

      </div>

    </div>
  );
}