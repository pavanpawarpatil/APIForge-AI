export default function Hero() {
  return (
    <section className="flex min-h-screen items-center justify-center px-6">
      <div className="mx-auto max-w-5xl text-center">

        {/* Badge */}
        <div className="mb-8 inline-flex rounded-full border border-blue-500/30 bg-blue-500/10 px-5 py-2 text-sm font-medium text-blue-300">
          ✨ Powered by Multi-Agent AI
        </div>

        {/* Heading */}
        <h1 className="text-6xl font-bold leading-tight text-white md:text-7xl">
          From Prompt
          <br />
          <span className="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
            To Production Backend
          </span>
        </h1>

        {/* Description */}
        <p className="mx-auto mt-8 max-w-3xl text-xl leading-9 text-gray-400">
          Generate production-ready FastAPI backend applications
          using LangGraph, AI Agents, Docker, JWT Authentication,
          and MySQL — all from a single prompt.
        </p>

        {/* Buttons */}
        <div className="mt-10 flex justify-center gap-4">
          <button className="rounded-xl bg-blue-600 px-8 py-4 font-semibold transition hover:bg-blue-700">
            🚀 Generate Backend
          </button>

          <button className="rounded-xl border border-white/20 bg-white/5 px-8 py-4 font-semibold text-white transition hover:bg-white/10">
            📖 Documentation
          </button>
        </div>

        {/* Tech Stack */}
        <div className="mt-10 flex flex-wrap justify-center gap-3">
          {["FastAPI", "LangGraph", "Docker", "JWT", "MySQL"].map((tech) => (
            <span
              key={tech}
              className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-gray-300"
            >
              {tech}
            </span>
          ))}
        </div>

      </div>
    </section>
  );
}