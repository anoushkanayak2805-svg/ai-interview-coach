import { useNavigate } from "react-router-dom";

import type {
  ResumeAnalysis,
} from "../../api/resume";


interface CandidateProfileCardProps {
  resumeUploaded?: boolean;

  filename?: string;

  skills?: string[];

  projects?: string[];

  analysis?: ResumeAnalysis | null;

  recommendedCompany?: string;
}


export default function CandidateProfileCard({
  resumeUploaded = false,

  filename = "",

  skills = [],

  projects = [],

  analysis = null,

  recommendedCompany = "",
}: CandidateProfileCardProps) {

  const navigate = useNavigate();


  /* ---------------------------------
     Display Values
  ---------------------------------- */

  const displayedSkills =
    skills.slice(0, 8);

  const displayedProjects =
    projects.slice(0, 3);

  const displayedFocusTopics =
    analysis?.weak_topics?.slice(0, 3) ?? [];


  const candidateLevel =
    analysis?.candidate_level ??
    analysis?.career_level ??
    "Not available";


  const experienceLevel =
    analysis?.experience_level ??
    "Not available";


  const codingLevel =
    analysis?.coding_level ??
    "Not available";


  return (
    <div className="rounded-3xl bg-white p-8 shadow-lg">

      {/* ---------------------------------
          Header
      ---------------------------------- */}

      <div className="flex items-start justify-between gap-4">

        <div>

          <h2 className="text-2xl font-bold text-slate-900">
            Candidate Profile
          </h2>

          <p className="mt-2 text-gray-500">
            AI-powered profile generated from your resume.
          </p>

        </div>


        <span
          className={`rounded-full px-3 py-1 text-xs font-semibold ${
            resumeUploaded
              ? "bg-green-100 text-green-700"
              : "bg-amber-100 text-amber-700"
          }`}
        >
          {resumeUploaded
            ? "Resume Analyzed"
            : "Resume Missing"}
        </span>

      </div>


      <div className="mt-8 space-y-7">

        {/* ---------------------------------
            Resume
        ---------------------------------- */}

        <div>

          <p className="text-sm text-gray-500">
            Resume
          </p>

          <p className="mt-1 break-words font-semibold text-slate-900">
            {resumeUploaded && filename
              ? filename
              : "No resume uploaded"}
          </p>

        </div>


        {/* ---------------------------------
            Candidate Levels
        ---------------------------------- */}

        {resumeUploaded && analysis && (

          <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">

            <div className="rounded-2xl bg-indigo-50 p-4">

              <p className="text-xs font-medium text-indigo-600">
                Career Level
              </p>

              <p className="mt-1 font-bold text-slate-900">
                {candidateLevel}
              </p>

            </div>


            <div className="rounded-2xl bg-blue-50 p-4">

              <p className="text-xs font-medium text-blue-600">
                Experience
              </p>

              <p className="mt-1 font-bold text-slate-900">
                {experienceLevel}
              </p>

            </div>


            <div className="rounded-2xl bg-emerald-50 p-4">

              <p className="text-xs font-medium text-emerald-600">
                Coding Level
              </p>

              <p className="mt-1 font-bold text-slate-900">
                {codingLevel}
              </p>

            </div>

          </div>

        )}


        {/* ---------------------------------
            Skills
        ---------------------------------- */}

        <div>

          <p className="mb-3 text-sm text-gray-500">
            Top Skills
          </p>

          {displayedSkills.length > 0 ? (

            <div className="flex flex-wrap gap-2">

              {displayedSkills.map((skill) => (

                <span
                  key={skill}
                  className="rounded-full bg-indigo-100 px-3 py-1 text-sm font-medium text-indigo-700"
                >
                  {skill}
                </span>

              ))}

              {skills.length > displayedSkills.length && (

                <span className="rounded-full bg-slate-100 px-3 py-1 text-sm font-medium text-slate-600">

                  +{skills.length - displayedSkills.length} more

                </span>

              )}

            </div>

          ) : (

            <p className="text-sm text-slate-400">
              Upload a resume to extract your skills.
            </p>

          )}

        </div>


        {/* ---------------------------------
            Projects
        ---------------------------------- */}

        <div>

          <div className="flex items-center justify-between">

            <p className="text-sm text-gray-500">
              Projects Detected
            </p>

            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
              {projects.length}
            </span>

          </div>


          {displayedProjects.length > 0 ? (

            <div className="mt-3 space-y-2">

              {displayedProjects.map((project) => (

                <div
                  key={project}
                  className="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3"
                >
                  <p className="text-sm font-medium text-slate-700">
                    {project}
                  </p>
                </div>

              ))}

            </div>

          ) : (

            <p className="mt-2 text-sm text-slate-400">
              No projects detected yet.
            </p>

          )}

        </div>


        {/* ---------------------------------
            Recommended Focus
        ---------------------------------- */}

        {displayedFocusTopics.length > 0 && (

          <div className="rounded-2xl bg-amber-50 p-5">

            <p className="text-sm font-semibold text-amber-700">
              Recommended Focus
            </p>

            <div className="mt-3 space-y-2">

              {displayedFocusTopics.map(
                (topic, index) => (

                  <div
                    key={`${topic}-${index}`}
                    className="flex items-start gap-2"
                  >

                    <span className="mt-1 text-amber-600">
                      •
                    </span>

                    <p className="text-sm leading-relaxed text-slate-700">
                      {topic}
                    </p>

                  </div>

                )
              )}

            </div>

          </div>

        )}


        {/* ---------------------------------
            Target Company
        ---------------------------------- */}

        <div>

          <p className="text-sm text-gray-500">
            Current Target Company
          </p>

          <p className="mt-1 font-semibold text-indigo-600">
            {recommendedCompany || "Not set"}
          </p>

        </div>


        {/* ---------------------------------
            Action
        ---------------------------------- */}

        <button
          onClick={() =>
            navigate("/candidate")
          }
          className="w-full rounded-xl bg-indigo-600 px-5 py-3 font-semibold text-white transition hover:bg-indigo-700"
        >
          {resumeUploaded
            ? "Update Resume"
            : "Upload Resume"}
        </button>

      </div>

    </div>
  );
}