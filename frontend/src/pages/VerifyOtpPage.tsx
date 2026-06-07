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
  verifyOtp,
} from "../services/auth";

const VerifyOtpPage = () => {

  const [otp, setOtp] =
    useState("");

  const location =
    useLocation();

  const navigate =
    useNavigate();

  const email =
    location.state?.email;

  const handleVerify =
    async () => {

      try {

        await verifyOtp(
          email,
          otp
        );

        navigate(
          "/reset-password",
          {
            state: { email },
          }
        );

      } catch {

        alert(
          "Invalid OTP"
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
          Verify OTP
        </Typography>

        <TextField
          fullWidth
          label="OTP"
          value={otp}
          onChange={(e) =>
            setOtp(
              e.target.value
            )
          }
        />

        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 2 }}
          onClick={
            handleVerify
          }
        >
          Verify
        </Button>
      </Paper>
    </Box>
  );
};

export default VerifyOtpPage;