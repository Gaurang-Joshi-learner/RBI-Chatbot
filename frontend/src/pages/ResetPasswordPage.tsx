import { useState } from "react";
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
} from "@mui/material";

import {
  useLocation,
  useNavigate,
} from "react-router-dom";

import {
  resetPassword,
} from "../services/auth";

const ResetPasswordPage = () => {

  const [password,
    setPassword] =
    useState("");

  const location =
    useLocation();

  const navigate =
    useNavigate();

  const email =
    location.state?.email;

  const handleReset =
    async () => {

      try {

        await resetPassword(
          email,
          password
        );

        alert(
          "Password reset successful"
        );

        navigate(
          "/login"
        );

      } catch {

        alert(
          "Reset failed"
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
          Reset Password
        </Typography>

        <TextField
          fullWidth
          type="password"
          label="New Password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
        />

        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 2 }}
          onClick={
            handleReset
          }
        >
          Reset Password
        </Button>
      </Paper>
    </Box>
  );
};

export default ResetPasswordPage;