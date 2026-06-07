import { create } from "zustand";
import { persist } from "zustand/middleware";
import { login as loginApi } from "../services/auth";

interface AuthState {
  isAuthenticated: boolean;
  user: {
    email: string;
    name: string;
  } | null;
  login: (email: string, password: string) => Promise<boolean>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      isAuthenticated: !!localStorage.getItem("token"),
      user: null,

     login: async (email, password) => {

  try {

    const response = await loginApi(
      email,
      password
    );
    if (response.error) {
  return false;
}
   if (!response.access_token) {
      return false;
    }

    localStorage.setItem(
      "token",
      response.access_token
    );

    set({
      isAuthenticated: true,
      user: {
        email,
        name: email.split("@")[0],
      },
    });

    return true;

  } catch (error) {

    return false;
  }
},
      logout: () => {

  localStorage.removeItem("token");
  localStorage.removeItem("chat-storage");

  set({
    isAuthenticated: false,
    user: null,
  });
},
    }),
    {
      name: "auth-storage",
    }
  )
);

