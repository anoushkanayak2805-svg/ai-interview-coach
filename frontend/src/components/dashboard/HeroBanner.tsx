export default function HeroBanner() {
  return (
    <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-indigo-600 via-blue-600 to-cyan-500 p-10 text-white shadow-xl">

      <div className="max-w-3xl">

        <p className="text-sm uppercase tracking-widest text-blue-100">
          AI Career Preparation Platform
        </p>

        <h1 className="mt-3 text-5xl font-bold">
          Welcome Back 👋
        </h1>

        <p className="mt-5 text-lg text-blue-100">
          Continue preparing for your dream company using
          personalized AI interviews.
        </p>

        <button className="mt-8 rounded-xl bg-white px-6 py-3 font-semibold text-indigo-700 transition hover:scale-105">
          Continue Practice →
        </button>

      </div>

      <div className="absolute -right-10 -top-10 h-56 w-56 rounded-full bg-white/10 blur-2xl" />

      <div className="absolute bottom-0 right-40 h-36 w-36 rounded-full bg-cyan-300/20 blur-2xl" />

    </div>
  );
}