import { useState } from "react";
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { forgotPassword } from "../services/auth";

const ForgotPasswordPage = () => {

  const [email, setEmail] =
    useState("");

  const navigate =
    useNavigate();

  const handleSubmit =
    async () => {

      try {

        await forgotPassword(
          email
        );

        navigate(
          "/verify-otp",
          {
            state: { email },
          }
        );

      } catch {

        alert(
          "Failed to generate OTP"
        );
      }
    };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        justifyContent:
          "center",
        alignItems: "center",
        background:
          "linear-gradient(135deg,#667eea 0%,#764ba2 100%)",
      }}
    >
      <Paper
        sx={{
          p: 4,
          width: 400,
        }}
      >
        <Typography
          variant="h4"
          sx={{ mb: 3 }}
        >
          Forgot Password
        </Typography>

        <TextField
          fullWidth
          label="Email"
          value={email}
          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
        />

        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 2 }}
          onClick={
            handleSubmit
          }
        >
          Send OTP
        </Button>
      </Paper>
    </Box>
  );
};

export default ForgotPasswordPage;