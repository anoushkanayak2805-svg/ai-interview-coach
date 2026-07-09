import axios from "axios";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_URL ||
    "http://127.0.0.1:8000",
});


/* ---------------------------------
   Request Interceptor
   Attach JWT to protected requests
---------------------------------- */

api.interceptors.request.use(
  (config) => {
    const token =
      localStorage.getItem("token");

    if (token) {
      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  },

  (error) => {
    return Promise.reject(error);
  }
);


/* ---------------------------------
   Response Interceptor
   Handle expired / invalid JWT
---------------------------------- */

api.interceptors.response.use(
  (response) => {
    return response;
  },

  (error) => {
    const status =
      error.response?.status;

    const detail =
      error.response?.data?.detail;


    if (status === 401) {

      console.warn(
        "Authentication failed:",
        detail
      );


      /*
        Remove invalid or expired token.
      */

      localStorage.removeItem("token");


      /*
        Redirect only if we are not
        already on login/register pages.
      */

      const currentPath =
        window.location.pathname;

      if (
        currentPath !== "/login" &&
        currentPath !== "/register"
      ) {
        window.location.href = "/login";
      }
    }


    return Promise.reject(error);
  }
);


export default api;