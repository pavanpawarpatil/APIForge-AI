export default function Features() {
  const features = [
    {
      icon: "🤖",
      title: "Multi-Agent AI",
      description:
        "Specialized AI agents collaborate to understand, plan, generate, review, and package your backend."
    },
    {
      icon: "⚡",
      title: "LangGraph Workflow",
      description:
        "A structured workflow coordinates every stage of backend generation with validation and retries."
    },
    {
      icon: "🚀",
      title: "FastAPI Generation",
      description:
        "Generate production-ready FastAPI projects with authentication, database support, and clean architecture."
    },
    {
      icon: "📦",
      title: "ZIP Export",
      description:
        "Download the complete generated backend project, ready to open and run."
    }
  ];

  return (
    <section id="features" className="px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <h2 className="text-center text-5xl font-bold text-white">
            Why Choose APIForge AI?
        </h2>

        <p className="mx-auto mt-5 mb-16 max-w-2xl text-center text-lg text-gray-400">
            Build production-ready backend APIs with an intelligent multi-agent system that plans,
            generates, validates, and packages your project automatically.
        </p>

        <div className="grid gap-8 md:grid-cols-2">
          {features.map((feature) => (
            <div
              key={feature.title}
                className="group rounded-2xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl transition-all duration-300 hover:-translate-y-2 hover:border-blue-500/50 hover:bg-white/10 hover:shadow-[0_0_30px_rgba(59,130,246,0.25)]">
            <div className="mb-4 text-5xl transition-transform duration-300 group-hover:scale-110">
                {feature.icon}
            </div>

              <h3 className="mb-3 text-2xl font-semibold text-white">
                {feature.title}
              </h3>

              <p className="text-gray-400">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}