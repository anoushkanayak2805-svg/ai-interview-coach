import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import Navbar from "../components/layout/Navbar";

import {
  generateQuestions,
  submitAnswer,
} from "../api/interview";

interface Question {
  id: number;
  question: string;
}

export default function InterviewRoom() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  // 45 minute timer
  const [secondsLeft, setSecondsLeft] = useState(45 * 60);

  useEffect(() => {
    loadQuestions();
  }, []);

  useEffect(() => {
    if (secondsLeft <= 0) return;

    const timer = setInterval(() => {
      setSecondsLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [secondsLeft]);

  async function loadQuestions() {
    try {
      const data = await generateQuestions(id!);
      setQuestions(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  async function handleNext() {
    const current = questions[currentIndex];

    if (!current) return;

    try {
      setSubmitting(true);

      await submitAnswer(id!, {
        question_id: current.id,
        answer,
      });

      if (currentIndex === questions.length - 1) {
        navigate("/reports");
        return;
      }

      setCurrentIndex((prev) => prev + 1);
      setAnswer("");

    } catch (err) {
      console.error(err);
      alert("Unable to submit answer.");
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center text-xl">
        Loading Interview...
      </div>
    );
  }

  const current = questions[currentIndex];

  const minutes = Math.floor(secondsLeft / 60);
  const seconds = secondsLeft % 60;

  const progress =
    ((currentIndex + 1) / questions.length) * 100;

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="mx-auto max-w-5xl px-8 py-8">

        <div className="rounded-3xl bg-white p-8 shadow-xl">

          <div className="flex items-center justify-between">

            <div>

              <h1 className="text-3xl font-bold">
                AI Interview
              </h1>

              <p className="mt-2 text-gray-500">
                Answer confidently and clearly.
              </p>

            </div>

            <div className="rounded-xl bg-indigo-100 px-5 py-3 font-bold text-indigo-700">

              {minutes}:{seconds.toString().padStart(2, "0")}

            </div>

          </div>

          {/* Progress */}

          <div className="mt-8">

            <div className="mb-2 flex justify-between text-sm">

              <span>

                Question {currentIndex + 1} / {questions.length}

              </span>

              <span>

                {Math.round(progress)}%

              </span>

            </div>

            <div className="h-2 rounded-full bg-gray-200">

              <div
                className="h-2 rounded-full bg-indigo-600 transition-all"
                style={{ width: `${progress}%` }}
              />

            </div>

          </div>

          {/* Question */}

          <div className="mt-8 rounded-2xl bg-slate-100 p-8">

            <h2 className="text-xl font-semibold">

              Question

            </h2>

            <p className="mt-4 text-lg">

              {current?.question}

            </p>

          </div>

          {/* Answer */}

          <textarea
            rows={8}
            className="mt-8 w-full rounded-2xl border p-5"
            placeholder="Write your answer..."
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
          />

          <div className="mt-8 flex justify-end">

            <button
              disabled={submitting}
              onClick={handleNext}
              className="rounded-xl bg-indigo-600 px-8 py-3 text-white hover:bg-indigo-700 disabled:opacity-50"
            >
              {submitting
                ? "Submitting..."
                : currentIndex === questions.length - 1
                ? "Finish Interview"
                : "Submit & Next"}
            </button>

          </div>

        </div>

      </div>

    </div>
  );
}