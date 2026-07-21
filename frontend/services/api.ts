const API_BASE_URL = "http://127.0.0.1:8000";

export interface GenerateResponse {
  success: boolean;
  message: string;
  project_name: string;
  zip_file: string;
}

export async function generateBackend(prompt: string) {
  const response = await fetch(`${API_BASE_URL}/generate/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to generate backend");
  }

  return response.json() as Promise<GenerateResponse>;
}

export function downloadZip(filename: string) {
  window.open(`${API_BASE_URL}/download/${filename}`, "_blank");
}