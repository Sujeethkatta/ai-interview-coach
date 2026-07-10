import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import toast from 'react-hot-toast';
import { Zap, Code, Brain, Users } from 'lucide-react';

import { interviewsApi } from '../services/api';

function Interview() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const interviewTypes = [
    {
      type: 'behavioral',
      name: 'Behavioral Interview',
      description: 'Master STAR method and soft skills',
      icon: Users,
      color: 'from-blue-500 to-cyan-500',
    },
    {
      type: 'technical',
      name: 'Technical Interview',
      description: 'Data structures, algorithms, systems design',
      icon: Brain,
      color: 'from-purple-500 to-pink-500',
    },
    {
      type: 'hr',
      name: 'HR Interview',
      description: 'Questions from HR professionals',
      icon: Zap,
      color: 'from-green-500 to-emerald-500',
    },
  ];

  const difficulties = [
    { value: 'beginner', label: 'Beginner' },
    { value: 'intermediate', label: 'Intermediate' },
    { value: 'advanced', label: 'Advanced' },
    { value: 'expert', label: 'Expert' },
  ];

  const [selectedType, setSelectedType] = useState('');
  const [selectedDifficulty, setSelectedDifficulty] = useState('intermediate');

  const handleStartInterview = async () => {
    if (!selectedType) {
      toast.error('Please select an interview type');
      return;
    }

    setLoading(true);

    try {
      const response = await interviewsApi.startInterview({
        interview_type: selectedType,
        difficulty: selectedDifficulty,
        title: `${selectedType} Interview - ${selectedDifficulty}`,
      });

      toast.success('Interview started!');
      navigate(`/report/${response.data.id}`);
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to start interview');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold text-gray-900">Interview Practice</h1>
        <p className="text-gray-600 mt-2">Choose an interview type and difficulty level to get started</p>
      </div>

      {/* Interview Types */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {interviewTypes.map((interview) => {
          const Icon = interview.icon;
          return (
            <div
              key={interview.type}
              onClick={() => setSelectedType(interview.type)}
              className={`cursor-pointer p-6 rounded-xl border-2 transition duration-200 ${
                selectedType === interview.type
                  ? 'border-blue-500 bg-blue-50'
                  : 'border-gray-200 bg-white hover:border-gray-300'
              }`}
            >
              <div className={`bg-gradient-to-br ${interview.color} p-3 rounded-lg w-fit mb-4`}>
                <Icon className="h-6 w-6 text-white" />
              </div>
              <h3 className="text-lg font-semibold text-gray-900">{interview.name}</h3>
              <p className="text-gray-600 text-sm mt-2">{interview.description}</p>
            </div>
          );
        })}
      </div>

      {/* Difficulty Selection */}
      {selectedType && (
        <div className="bg-white rounded-xl shadow-lg p-8 border border-gray-100">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Select Difficulty Level</h2>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            {difficulties.map((diff) => (
              <button
                key={diff.value}
                onClick={() => setSelectedDifficulty(diff.value)}
                className={`p-4 rounded-lg border-2 font-semibold transition duration-200 ${
                  selectedDifficulty === diff.value
                    ? 'border-blue-500 bg-blue-50 text-blue-600'
                    : 'border-gray-200 bg-white text-gray-600 hover:border-gray-300'
                }`}
              >
                {diff.label}
              </button>
            ))}
          </div>

          {/* Start Button */}
          <button
            onClick={handleStartInterview}
            disabled={loading}
            className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-lg font-semibold hover:shadow-lg transition duration-200 disabled:opacity-50"
          >
            {loading ? 'Starting...' : 'Start Interview'}
          </button>
        </div>
      )}
    </div>
  );
}

export default Interview;
