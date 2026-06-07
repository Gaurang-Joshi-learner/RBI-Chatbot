import { useState } from "react";
import { login } from "../services/auth";

const LoginPage = () => {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const response = await login(
        email,
        password
      );

      localStorage.setItem(
        "token",
        response.access_token
      );

      alert("Login Successful");

    } catch (error: any) {

      alert(
        error.response?.data?.error ||
        "Login Failed"
      );
    }
  };

  return (
    <div>
      <h1>Login</h1>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) =>
          setEmail(e.target.value)
        }
      />

      <br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <br />

      <button onClick={handleLogin}>
        Login
      </button>
    </div>
  );
};

export default LoginPage;