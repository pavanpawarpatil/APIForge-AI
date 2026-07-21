export default function Workflow() {
  const steps = [
    "User Prompt",
    "Request Parser",
    "Project Planner",
    "Code Generator",
    "Validator",
    "Code Reviewer",
    "Project Builder",
    "ZIP Export",
  ];

  return (
    <section id="workflow" className="px-6 py-24">
      <div className="mx-auto max-w-6xl">

        <h2 className="text-center text-5xl font-bold text-white">
          How APIForge AI Works
        </h2>

        <p className="mx-auto mt-5 mb-16 max-w-2xl text-center text-lg text-gray-400">
          A multi-agent workflow that transforms your idea into a production-ready backend.
        </p>

        <div className="flex flex-wrap items-center justify-center gap-4">
          {steps.map((step, index) => (
            <div key={step} className="flex items-center">

              <div className="rounded-xl border border-white/10 bg-white/5 px-6 py-4 text-white backdrop-blur-xl">
                {step}
              </div>

              {index !== steps.length - 1 && (
                <div className="mx-3 text-2xl text-blue-400">
                  →
                </div>
              )}

            </div>
          ))}
        </div>

      </div>
    </section>
  );
}