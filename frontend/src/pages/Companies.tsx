import { useNavigate } from "react-router-dom";

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

export default function Companies() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="mx-auto max-w-7xl p-8">

        <h1 className="text-4xl font-bold">
          Company Preparation
        </h1>

        <p className="mt-2 text-gray-500">
          Choose your target company.
        </p>

        <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">

          {companies.map((company) => (

            <button
              key={company}
              onClick={() =>
                navigate(
                  `/interviews/create?company=${company}`
                )
              }
              className="rounded-3xl bg-white p-8 text-left shadow transition hover:-translate-y-1 hover:shadow-xl"
            >

              <h2 className="text-2xl font-bold">
                {company}
              </h2>

              <p className="mt-3 text-gray-500">
                Practice Interview
              </p>

            </button>

          ))}

        </div>

      </div>

    </div>
  );
}