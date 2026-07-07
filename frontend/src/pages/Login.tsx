import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import {
  useForm,
} from "react-hook-form";

import {
  zodResolver,
} from "@hookform/resolvers/zod";

import { loginSchema } from "../types/auth";
import type { LoginForm } from "../types/auth";
import {
  login,
} from "../api/auth";

import {
  useAuth,
} from "../context/AuthContext";

import Input from "../components/common/Input";
import Button from "../components/common/Button";

export default function Login() {

  const navigate = useNavigate();

  const auth = useAuth();

  const [loading, setLoading] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  });

  async function onSubmit(
    data: LoginForm
  ) {

    try {

      setLoading(true);

      const response = await login(data);

      auth.login(response.access_token);

      navigate("/dashboard");

    } catch {

      alert("Invalid credentials");

    } finally {

      setLoading(false);

    }

  }

  return (

    <div className="min-h-screen flex items-center justify-center bg-slate-100">

      <div className="bg-white rounded-xl shadow-xl p-10 w-[420px]">

        <h1 className="text-3xl font-bold mb-2">

          AI Interview Coach

        </h1>

        <p className="text-gray-500 mb-8">

          Welcome back

        </p>

        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-5"
        >

          <Input
            label="Email"
            type="email"
            {...register("email")}
            error={errors.email?.message}
          />

          <Input
            label="Password"
            type="password"
            {...register("password")}
            error={errors.password?.message}
          />

          <Button
            loading={loading}
            type="submit"
          >
            Login
          </Button>

        </form>

        <p className="mt-6 text-center">

          Don't have an account?

          <Link
            to="/register"
            className="text-blue-600 ml-2"
          >
            Register
          </Link>

        </p>

      </div>

    </div>

  );

}