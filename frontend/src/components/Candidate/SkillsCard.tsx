const skills = [
  "React",
  "FastAPI",
  "SQL",
  "Docker",
  "C++",
  "Tailwind",
];

export default function SkillsCard() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      <h2 className="text-2xl font-bold">
        Technical Skills
      </h2>

      <div className="mt-6 flex flex-wrap gap-3">

        {skills.map((skill) => (
          <span
            key={skill}
            className="rounded-full bg-indigo-100 px-4 py-2 text-indigo-700"
          >
            {skill}
          </span>
        ))}

      </div>

    </div>
  );
}