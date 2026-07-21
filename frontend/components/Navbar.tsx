export default function Navbar() {
  return (
    <nav className="fixed top-0 left-0 z-50 w-full border-b border-white/10 bg-black/30 backdrop-blur-xl">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-8">

        <div>
          <h1 className="text-2xl font-bold tracking-wide text-white">
            APIForge
            <span className="text-blue-500"> AI</span>
          </h1>
        </div>

        <div className="hidden items-center gap-10 md:flex">

          <a
            href="#features"
            className="text-gray-300 transition hover:text-white"
          >
            Features
          </a>

          <a
            href="#workflow"
            className="text-gray-300 transition hover:text-white"
          >
            Workflow
          </a>

          <a
            href="#generate"
            className="text-gray-300 transition hover:text-white"
          >
            Generate
          </a>

          <a
            href="https://github.com/pavanpawarpatil/APIForge-AI"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg border border-blue-500 px-4 py-2 text-blue-400 transition hover:bg-blue-500 hover:text-white"
          >
            GitHub
          </a>

        </div>
      </div>
    </nav>
  );
}