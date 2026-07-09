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
  category?: string;
  difficulty?: string;
}

export default function InterviewRoom() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  // 45-minute timer
  const [secondsLeft, setSecondsLeft] = useState(45 * 60);

  useEffect(() => {
    if (id) {
      loadQuestions();
    }
  }, [id]);

  useEffect(() => {
    if (secondsLeft <= 0) return;

    const timer = setInterval(() => {
      setSecondsLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [secondsLeft]);

  async function loadQuestions() {
    try {
      setLoading(true);

      const response: any = await generateQuestions(id!);

      console.log("========== RAW RESPONSE ==========");
      console.log(response);
      console.log("==================================");

      let rawQuestions: any[] = [];

      if (Array.isArray(response)) {
        rawQuestions = response;
      } else if (response?.questions) {
        rawQuestions = response.questions;
      } else if (response?.data) {
        rawQuestions = response.data;
      }

      const formattedQuestions: Question[] = rawQuestions.map(
        (q: any, index: number) => ({
          id:
            q.id ??
            q.question_id ??
            index + 1,

          question:
            q.question ??
            q.question_text ??
            q.text ??
            q.content ??
            "Question not available",

          category: q.category,

          difficulty: q.difficulty,
        })
      );

      console.log(
        "========== FORMATTED QUESTIONS =========="
      );

      console.log(formattedQuestions);

      console.log(
        "==========================================="
      );

      setQuestions(formattedQuestions);

    } catch (err) {

      console.error(
        "Failed to load questions:",
        err
      );

    } finally {

      setLoading(false);

    }
  }

  async function handleNext() {
    const current = questions[currentIndex];

    if (!current) {
      return;
    }

    if (!answer.trim()) {
      alert("Please enter an answer.");
      return;
    }

    try {
      setSubmitting(true);

      console.log(
        "========== SUBMITTING ANSWER =========="
      );

      console.log({
        interview_id: id,
        question_id: current.id,
        answer_text: answer,
      });

      const response = await submitAnswer(
        id!,
        {
          question_id: current.id,
          answer_text: answer,
        }
      );

      console.log(
        "========== SUBMIT RESPONSE =========="
      );

      console.log(response);

      console.log(
        "======================================"
      );

      /*
        If this is the final question,
        navigate to the report details page.

        Example:
        /reports/14
      */

      if (currentIndex === questions.length - 1) {

        console.log(
          "Interview completed. Opening report..."
        );

        navigate(`/reports/${id}`);

        return;
      }

      /*
        Otherwise move to next question
      */

      setCurrentIndex(
        (prev) => prev + 1
      );

      setAnswer("");

    } catch (err: any) {

      console.error(
        "========== SUBMIT ERROR =========="
      );

      console.error(err);

      if (err.response) {

        console.error(
          "Status:",
          err.response.status
        );

        console.error(
          "Response:",
          err.response.data
        );

        alert(
          `Submit failed (${err.response.status})\n\n${JSON.stringify(
            err.response.data,
            null,
            2
          )}`
        );

      } else {

        alert(
          "Unable to submit answer."
        );

      }

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

  if (questions.length === 0) {
    return (
      <div className="min-h-screen bg-slate-100">

        <Navbar />

        <div className="mx-auto mt-20 max-w-3xl rounded-3xl bg-white p-10 text-center shadow-xl">

          <h2 className="text-3xl font-bold text-red-600">
            No Questions Found
          </h2>

          <p className="mt-4 text-gray-600">
            The backend didn't return any interview questions.
          </p>

          <button
            onClick={loadQuestions}
            className="mt-8 rounded-xl bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700"
          >
            Retry
          </button>

        </div>

      </div>
    );
  }

  const current = questions[currentIndex];

  const minutes = Math.floor(
    secondsLeft / 60
  );

  const seconds =
    secondsLeft % 60;

  const progress =
    ((currentIndex + 1) /
      questions.length) *
    100;

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

              {minutes}:
              {seconds
                .toString()
                .padStart(2, "0")}

            </div>

          </div>

          {/* Progress */}

          <div className="mt-8">

            <div className="mb-2 flex justify-between text-sm">

              <span>
                Question {currentIndex + 1} /{" "}
                {questions.length}
              </span>

              <span>
                {Math.round(progress)}%
              </span>

            </div>

            <div className="h-2 rounded-full bg-gray-200">

              <div
                className="h-2 rounded-full bg-indigo-600 transition-all"
                style={{
                  width: `${progress}%`,
                }}
              />

            </div>

          </div>

          {/* Question */}

          <div className="mt-8 rounded-2xl bg-slate-100 p-8">

            <div className="flex flex-wrap items-center gap-3">

              <h2 className="text-xl font-semibold">
                Question
              </h2>

              {current.category && (
                <span className="rounded-full bg-indigo-100 px-3 py-1 text-sm font-medium text-indigo-700">
                  {current.category}
                </span>
              )}

              {current.difficulty && (
                <span className="rounded-full bg-emerald-100 px-3 py-1 text-sm font-medium text-emerald-700">
                  {current.difficulty}
                </span>
              )}

            </div>

            <p className="mt-4 text-lg font-medium">
              {current.question}
            </p>

          </div>

          {/* Answer */}

          <textarea
            rows={8}
            className="mt-8 w-full rounded-2xl border border-slate-300 p-5 outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            placeholder="Write your answer here..."
            value={answer}
            disabled={submitting}
            onChange={(e) =>
              setAnswer(e.target.value)
            }
          />

          <div className="mt-8 flex justify-end">

            <button
              disabled={
                submitting ||
                !answer.trim()
              }
              onClick={handleNext}
              className="rounded-xl bg-indigo-600 px-8 py-3 text-white transition hover:bg-indigo-700 disabled:cursor-not-allowed disabled:opacity-50"
            >

              {submitting
                ? "Submitting..."
                : currentIndex ===
                  questions.length - 1
                ? "Finish Interview"
                : "Submit & Next"}

            </button>

          </div>

        </div>

      </div>

    </div>
  );
}