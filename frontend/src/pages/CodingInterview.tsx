import React, { useState } from 'react';
import toast from 'react-hot-toast';

function CodingInterview() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [running, setRunning] = useState(false);

  const handleRunCode = async () => {
    setRunning(true);
    try {
      // Mock code execution - in production, use a safe code execution service
      toast.success('Code executed successfully');
      setOutput('Output: Hello World');
    } catch (error) {
      toast.error('Code execution failed');
    } finally {
      setRunning(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold text-gray-900">Coding Interview</h1>
        <p className="text-gray-600 mt-2">Practice coding problems and improve your algorithmic skills</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Problem Statement */}
        <div className="lg:col-span-1 bg-white rounded-xl shadow-lg p-6 border border-gray-100 h-fit">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Problem</h2>
          <div className="text-gray-600 space-y-3 text-sm">
            <p>
              <strong>Two Sum</strong>
            </p>
            <p>Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.</p>
            <div className="mt-4 p-3 bg-gray-50 rounded border border-gray-200">
              <p className="font-mono text-xs">Example: nums = [2,7,11,15], target = 9</p>
              <p className="font-mono text-xs mt-2">Output: [0,1]</p>
            </div>
          </div>
        </div>

        {/* Code Editor */}
        <div className="lg:col-span-2 space-y-4">
          <div className="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden">
            <div className="bg-gray-900 text-white p-4 font-mono flex items-center justify-between">
              <span>editor.py</span>
              <button
                onClick={handleRunCode}
                disabled={running}
                className="bg-green-600 hover:bg-green-700 px-4 py-1 rounded text-sm font-semibold disabled:opacity-50"
              >
                {running ? 'Running...' : '▶ Run Code'}
              </button>
            </div>

            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="Write your code here..."
              className="w-full h-96 p-4 font-mono text-sm border-none focus:outline-none"
            />
          </div>

          {/* Output */}
          {output && (
            <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
              <h3 className="text-lg font-bold text-gray-900 mb-3">Output</h3>
              <div className="bg-gray-900 text-white p-4 rounded font-mono text-sm whitespace-pre-wrap">{output}</div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default CodingInterview;
