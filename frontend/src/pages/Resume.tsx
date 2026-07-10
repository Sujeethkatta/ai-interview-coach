import React, { useState } from 'react';
import { Upload, File, CheckCircle } from 'lucide-react';
import toast from 'react-hot-toast';

import { resumesApi } from '../services/api';

function Resume() {
  const [uploading, setUploading] = useState(false);
  const [resumes, setResumes] = useState<any[]>([]);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);

    try {
      const response = await resumesApi.uploadResume(file);
      setResumes([...resumes, response.data]);
      toast.success('Resume uploaded successfully');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Upload failed');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold text-gray-900">Resume Manager</h1>
        <p className="text-gray-600 mt-2">Upload and manage your resumes for interviews</p>
      </div>

      {/* Upload Area */}
      <div className="bg-white rounded-xl shadow-lg border-2 border-dashed border-gray-300 p-12 text-center hover:border-blue-500 transition duration-200">
        <Upload className="h-12 w-12 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-semibold text-gray-900">Upload Your Resume</h3>
        <p className="text-gray-600 mt-1">Drag and drop or click to select a file</p>
        <p className="text-sm text-gray-500 mt-1">Supported formats: PDF, DOC, DOCX</p>

        <label className="mt-6 inline-block">
          <input
            type="file"
            onChange={handleFileUpload}
            disabled={uploading}
            accept=".pdf,.doc,.docx"
            className="hidden"
          />
          <span className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold cursor-pointer hover:bg-blue-700 transition duration-200 inline-block">
            {uploading ? 'Uploading...' : 'Choose File'}
          </span>
        </label>
      </div>

      {/* Resumes List */}
      {resumes.length > 0 && (
        <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Your Resumes</h2>
          <div className="space-y-4">
            {resumes.map((resume) => (
              <div key={resume.id} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition duration-200">
                <div className="flex items-center gap-4">
                  <File className="h-8 w-8 text-blue-600" />
                  <div>
                    <p className="font-semibold text-gray-900">{resume.filename}</p>
                    <p className="text-sm text-gray-600">Uploaded on {new Date(resume.created_at).toLocaleDateString()}</p>
                  </div>
                </div>
                <CheckCircle className="h-6 w-6 text-green-500" />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default Resume;
