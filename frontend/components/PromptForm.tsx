export default function PromptForm() {
  return (
    <section className="mx-auto max-w-4xl rounded-xl border border-slate-800 bg-slate-900 p-6">

      <label className="mb-3 block text-lg font-semibold">
        Project Description
      </label>

      <textarea
        rows={10}
        placeholder="Describe the backend you want to generate..."
        className="w-full rounded-lg border border-slate-700 bg-slate-950 p-4 outline-none focus:border-blue-500"
      />

      <button
        className="mt-6 w-full rounded-lg bg-blue-600 py-3 font-semibold transition hover:bg-blue-700"
      >
        Generate Backend
      </button>

    </section>
  );
}