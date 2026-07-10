import React from 'react';
import { useParams } from 'react-router-dom';

function Report() {
  const { id } = useParams();

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold text-gray-900">Interview Report</h1>
        <p className="text-gray-600 mt-2">Detailed analysis of your interview performance</p>
      </div>

      <div className="bg-white rounded-xl shadow-lg p-8 border border-gray-100">
        <p className="text-gray-600">Report for interview: {id}</p>
      </div>
    </div>
  );
}

export default Report;
