import React,{ useState } from "react";
import "tailwindcss/tailwind.css";

export default function BloodReportParser() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    setData(result);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-4">Blood Report Parser</h1>
      <div className="bg-white p-4 rounded-lg shadow-md flex gap-3">
        <input type="file" onChange={handleFileChange} className="p-2 border" />
        <button
          onClick={handleUpload}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Upload
        </button>
      </div>
      {data && (
        <div className="mt-6 p-4 bg-white rounded-lg shadow-md w-full max-w-2xl">
          <h2 className="text-xl font-semibold mb-2">Extracted Data:</h2>
          <table className="w-full border-collapse border border-gray-300">
            <thead>
              <tr className="bg-gray-200">
                <th className="border p-2">Parameter</th>
                <th className="border p-2">Value</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(data.extracted_data).map(([key, value]) => (
                <tr key={key}>
                  <td className="border p-2">{key}</td>
                  <td className="border p-2">{value}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <h2 className="text-xl font-semibold mt-4">Classified Data:</h2>
          <table className="w-full border-collapse border border-gray-300">
            <thead>
              <tr className="bg-gray-200">
                <th className="border p-2">Category</th>
                <th className="border p-2">Parameters</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(data.classified_data).map(([category, values]) => (
                <tr key={category}>
                  <td className="border p-2 font-semibold">{category}</td>
                  <td className="border p-2">
                    {values.length > 0 ? (
                      values.map(([param, value]) => (
                        <div key={param}>{param}: {value}</div>
                      ))
                    ) : (
                      "None"
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
