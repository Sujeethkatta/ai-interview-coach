import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ChevronRight, BookOpen, Code, Zap, TrendingUp } from 'lucide-react';

function Home() {
  const navigate = useNavigate();

  const features = [
    {
      icon: BookOpen,
      title: 'AI-Powered Interviews',
      description: 'Practice with realistic interview scenarios powered by AI',
    },
    {
      icon: Code,
      title: 'Coding Challenges',
      description: 'Solve coding problems with real-time execution and feedback',
    },
    {
      icon: Zap,
      title: 'Instant Feedback',
      description: 'Get immediate AI-generated feedback on your answers',
    },
    {
      icon: TrendingUp,
      title: 'Progress Tracking',
      description: 'Track your improvement with detailed analytics and reports',
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50">
      {/* Navigation */}
      <nav className="flex items-center justify-between px-6 py-4 md:px-12">
        <div className="flex items-center gap-3">
          <div className="inline-flex items-center justify-center w-10 h-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg">
            <span className="text-lg font-bold text-white">AI</span>
          </div>
          <span className="text-xl font-bold text-gray-900">Interview Coach</span>
        </div>
        <div className="flex items-center gap-4">
          <button onClick={() => navigate('/login')} className="text-gray-600 hover:text-gray-900 font-medium">
            Login
          </button>
          <button
            onClick={() => navigate('/register')}
            className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-6 py-2 rounded-lg font-semibold hover:shadow-lg transition duration-200"
          >
            Sign Up
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="px-6 py-20 md:px-12 md:py-32 text-center">
        <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
          Master Interviews with
          <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent"> AI Coaching</span>
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto mb-8">
          Practice realistic interview scenarios, get instant AI feedback, and track your progress with detailed analytics.
        </p>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <button
            onClick={() => navigate('/register')}
            className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-3 rounded-lg font-semibold hover:shadow-lg transition duration-200 flex items-center gap-2"
          >
            Get Started Free
            <ChevronRight className="h-5 w-5" />
          </button>
          <button onClick={() => navigate('/login')} className="border-2 border-blue-600 text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition duration-200">
            Sign In
          </button>
        </div>
      </section>

      {/* Features Section */}
      <section className="px-6 py-20 md:px-12">
        <h2 className="text-4xl font-bold text-gray-900 text-center mb-16">Why Choose Interview Coach?</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <div key={index} className="bg-white rounded-xl shadow-lg p-8 border border-gray-100 hover:shadow-xl transition duration-200">
                <div className="bg-gradient-to-br from-blue-100 to-indigo-100 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
                  <Icon className="h-6 w-6 text-blue-600" />
                </div>
                <h3 className="text-lg font-bold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600 text-sm">{feature.description}</p>
              </div>
            );
          })}
        </div>
      </section>

      {/* CTA Section */}
      <section className="px-6 py-20 md:px-12 text-center bg-gradient-to-r from-blue-600 to-indigo-600 rounded-3xl mx-6 md:mx-12">
        <h2 className="text-4xl font-bold text-white mb-4">Ready to Ace Your Interviews?</h2>
        <p className="text-blue-100 mb-8 text-lg">Join thousands of students preparing for their dream jobs</p>
        <button
          onClick={() => navigate('/register')}
          className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:shadow-lg transition duration-200"
        >
          Start Free Trial
        </button>
      </section>

      {/* Footer */}
      <footer className="px-6 py-12 md:px-12 text-center text-gray-600 border-t border-gray-200 mt-20">
        <p>&copy; 2024 Interview Coach. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Home;
