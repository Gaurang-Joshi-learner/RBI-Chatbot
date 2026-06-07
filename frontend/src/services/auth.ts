import axios from "axios";

const API_URL = "http://localhost:8000";

export const signup = async (
  username: string,
  email: string,
  password: string
) => {
  const response = await axios.post(
    `${API_URL}/auth/signup`,
    {
      username,
      email,
      password,
    }
  );

  return response.data;
};

export const login = async (
  email: string,
  password: string
) => {
  const response = await axios.post(
    `${API_URL}/auth/login`,
    {
      email,
      password,
    }
  );

  return response.data;
};
export const forgotPassword = async (
  email: string
) => {

  const response = await axios.post(
    `${API_URL}/auth/forgot-password`,
    {
      email,
    }
  );

  return response.data;
};

export const verifyOtp = async (
  email: string,
  otp: string
) => {

  const response = await axios.post(
    `${API_URL}/auth/verify-otp`,
    {
      email,
      otp,
    }
  );

  return response.data;
};

export const resetPassword = async (
  email: string,
  newPassword: string
) => {

  const response = await axios.post(
    `${API_URL}/auth/reset-password`,
    {
      email,
      new_password: newPassword,
    }
  );

  return response.data;
};