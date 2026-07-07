import Navbar from "../components/layout/Navbar";

import CandidateHeader from "../components/candidate/CandidateHeader";
import ResumeCard from "../components/candidate/ResumeCard";
import SkillsCard from "../components/candidate/SkillsCard";

export default function Candidate() {
  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto max-w-7xl px-8 py-8 space-y-8">

        <CandidateHeader />

        <ResumeCard />

        <SkillsCard />

      </div>

    </div>
  );
}