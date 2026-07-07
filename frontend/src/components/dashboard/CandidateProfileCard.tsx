export default function CandidateProfileCard() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <h2 className="text-2xl font-bold">
        Candidate Profile
      </h2>

      <p className="mt-2 text-gray-500">
        Personalized Interview Profile
      </p>

      <div className="mt-8 space-y-5">

        <div>
          <p className="text-sm text-gray-500">
            Experience
          </p>

          <p className="font-semibold">
            Intermediate
          </p>
        </div>

        <div>
          <p className="text-sm text-gray-500">
            Preferred Language
          </p>

          <p className="font-semibold">
            C++
          </p>
        </div>

        <div>

          <p className="mb-3 text-sm text-gray-500">
            Skills
          </p>

          <div className="flex flex-wrap gap-2">

            {["React", "FastAPI", "SQL", "Docker"].map((skill) => (
              <span
                key={skill}
                className="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-700"
              >
                {skill}
              </span>
            ))}

          </div>

        </div>

        <div>

          <p className="text-sm text-gray-500">
            Recommended Company
          </p>

          <p className="font-semibold text-indigo-600">
            Google
          </p>

        </div>

      </div>

    </div>
  );
}