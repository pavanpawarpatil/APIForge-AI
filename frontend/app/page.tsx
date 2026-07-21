import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Features from "@/components/Features";
import Workflow from "@/components/Workflow";
import Generator from "@/components/Generator";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <Features />
      <Workflow />
      <Generator />
    </main>
  );
}