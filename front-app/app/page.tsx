"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [responseData, setResponseData] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!prompt.trim()) return;
    setLoading(true);
    setResponseData(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/plan-trip", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: prompt }),
      });

      const data = await response.json();
      setResponseData(data.report);
    } catch {
      setResponseData("Failed to fetch data.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center p-4 relative">
      {/* Transparent Loading Overlay */}
      {loading && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
          <div className="text-white text-lg font-semibold animate-pulse">
            ⏳ Generating your travel report...
          </div>
        </div>
      )}

      <div className="w-full max-w-2xl bg-white shadow-xl rounded-xl p-6 z-10">
        <h1 className="text-2xl font-bold mb-4 text-center text-blue-700"> Travel Assistant</h1>

        <div className="flex gap-2 mb-4">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="flex-grow border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="e.g., Plan a one-day trip to Jaipur"
          />
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
          >
            Ask
          </button>
        </div>

        {responseData && (
          <div className="prose prose-sm sm:prose lg:prose-lg xl:prose-xl max-w-none mt-6">
            <ReactMarkdown>{responseData}</ReactMarkdown>
          </div>
        )}
      </div>
    </main>
  );
}
