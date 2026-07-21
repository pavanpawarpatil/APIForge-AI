"use client";

import { useState } from "react";
import { generateBackend, downloadZip } from "@/services/api";

const prompts = {
  ecommerce: `Create an E-Commerce API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Users
- Products
- Categories
- Orders
- Cart
- Reviews

Features:
- User Registration
- User Login
- Product Search
- Product Filtering
- Pagination
- Redis Caching
- Role-Based Access Control
- Swagger Documentation

Generate a production-ready backend.`,

  hospital: `Create a Hospital Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Patients
- Doctors
- Appointments
- Prescriptions
- Billing

Features:
- User Registration
- User Login
- Appointment Booking
- Patient History
- Pagination
- Redis Caching
- Role-Based Access Control
- Swagger Documentation

Generate a production-ready backend.`,

  library: `Create a Library Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Books
- Authors
- Members
- Borrow Records

Features:
- User Registration
- User Login
- Search Books
- Pagination
- Redis Caching
- Swagger Documentation

Generate a production-ready backend.`,

  task: `Create a Task Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Users
- Projects
- Tasks
- Comments

Features:
- User Registration
- User Login
- Task Assignment
- Task Status Tracking
- Pagination
- Redis Caching
- Swagger Documentation

Generate a production-ready backend.`,

  student: `Create a Student Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Students
- Teachers
- Courses
- Enrollments

Features:
- Attendance
- User Login
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  restaurant: `Create a Restaurant Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Customers
- Menu
- Orders
- Tables

Features:
- Table Reservation
- Order Tracking
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  hotel: `Create a Hotel Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Rooms
- Bookings
- Customers
- Payments

Features:
- Room Availability
- Online Booking
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  travel: `Create a Travel Booking API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Users
- Trips
- Bookings
- Payments

Features:
- Trip Search
- Booking Management
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  banking: `Create a Banking API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Customers
- Accounts
- Transactions
- Cards

Features:
- Money Transfer
- Transaction History
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  movie: `Create a Movie Ticket Booking API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Movies
- Shows
- Tickets
- Users

Features:
- Seat Booking
- Search Movies
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  taxi: `Create a Taxi Booking API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Drivers
- Riders
- Trips
- Payments

Features:
- Ride Booking
- Live Trip Status
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,

  inventory: `Create an Inventory Management API using FastAPI, MySQL, JWT Authentication, Docker and Redis.

CRUD Modules:
- Products
- Suppliers
- Orders
- Stock

Features:
- Low Stock Alerts
- Search Products
- Pagination
- Swagger Documentation

Generate a production-ready backend.`,
};

const examples = [
  { key: "ecommerce", icon: "🛒", label: "E-Commerce" },
  { key: "hospital", icon: "🏥", label: "Hospital" },
  { key: "library", icon: "📚", label: "Library" },
  { key: "task", icon: "✅", label: "Task Manager" },
  { key: "student", icon: "🎓", label: "Student" },
  { key: "restaurant", icon: "🍽️", label: "Restaurant" },
  { key: "hotel", icon: "🏨", label: "Hotel" },
  { key: "travel", icon: "✈️", label: "Travel" },
  { key: "banking", icon: "🏦", label: "Banking" },
  { key: "movie", icon: "🎬", label: "Movie" },
  { key: "taxi", icon: "🚖", label: "Taxi" },
  { key: "inventory", icon: "📦", label: "Inventory" },
] as const;

export default function Generator() {
  const [selected, setSelected] =
    useState<(typeof examples)[number]["key"]>("ecommerce");

  const [prompt, setPrompt] = useState(prompts.ecommerce);
  const [loading, setLoading] = useState(false);
  const [projectName, setProjectName] = useState("");
  const [zipFile, setZipFile] = useState("");

  const handleClick = (key: keyof typeof prompts) => {
    setSelected(key);
    setPrompt(prompts[key]);
  };
  const handleGenerate = async () => {
    if (!prompt.trim()) {
      alert("Please enter a prompt.");
      return;
    }

    try {
      setLoading(true);

      const response = await generateBackend(prompt);

      setProjectName(response.project_name);
      setZipFile(response.zip_file);

      alert("Backend generated successfully!");
    } catch (error) {
      console.error(error);
      alert("Failed to generate backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="generate" className="px-6 py-24">
      <div className="mx-auto max-w-6xl rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl">

        <h2 className="text-center text-5xl font-bold text-white">
          Generate Your Backend
        </h2>

        <p className="mt-4 text-center text-lg text-gray-400">
          Select an example or write your own backend requirements.
        </p>

        <div className="mt-10">

          <p className="mb-4 text-sm font-semibold text-gray-300">
            💡 Try an Example
          </p>

          <div className="flex gap-4 overflow-x-auto pb-4 scrollbar-thin scrollbar-thumb-blue-600 scrollbar-track-transparent">

            {examples.map((item) => (

              <button
                key={item.key}
                onClick={() => handleClick(item.key)}
                className={`flex-shrink-0 rounded-full px-5 py-3 font-medium transition ${
                  selected === item.key
                    ? "bg-blue-600 text-white"
                    : "border border-white/10 bg-white/5 text-white hover:border-blue-500 hover:bg-blue-500/10"
                }`}
              >
                <span className="mr-2">{item.icon}</span>
                {item.label}
              </button>

            ))}

          </div>

        </div>

        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          rows={16}
          className="mt-8 w-full rounded-2xl border border-white/10 bg-black/30 p-6 text-white outline-none focus:border-blue-500"
        />

        <div className="mt-10 flex justify-center">

          <button
            onClick={handleGenerate}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-10 py-4 text-lg font-semibold transition hover:scale-105 hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Generating..." : "🚀 Generate Production Backend"}
          </button>

        </div>
        {zipFile && (
          <div className="mt-8 flex flex-col items-center gap-4">

            <p className="text-green-400 font-medium">
              ✅ {projectName} generated successfully.
            </p>

            <button
              onClick={() => downloadZip(zipFile)}
              className="rounded-xl bg-green-600 px-8 py-3 font-semibold text-white hover:bg-green-700 transition"
            >
              📥 Download ZIP
            </button>

          </div>
        )}

        <p className="mt-5 text-center text-sm text-gray-400">
          ⚡ Every generated project is automatically reviewed, validated and packaged before download.
        </p>

      </div>
    </section>
  );
}