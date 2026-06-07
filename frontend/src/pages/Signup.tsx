import { useState } from "react";
import { signup } from "../services/auth";
import {
  Box,
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  Alert,
} from "@mui/material";
import { useNavigate } from "react-router-dom";``

const SignupPage = () => {
  const navigate = useNavigate();
``
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {

    try {

      const response = await signup(
        username,
        email,
        password
      );

      
alert("Account created successfully!");

navigate("/login");
    } catch (error: any) {

      alert(
        error.response?.data?.error ||
        "Signup failed"
      );
    }
  };

 return (
  <Box
    sx={{
      minHeight: "100vh",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      background:
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
      py: 4,
    }}
  >
    <Container maxWidth="sm">
      <Paper
        elevation={10}
        sx={{
          p: 4,
          borderRadius: 3,
          boxShadow:
            "0 8px 32px rgba(0,0,0,0.1)",
        }}
      >
        <Box
          sx={{
            textAlign: "center",
            mb: 5,
          }}
        >
          <Typography
            variant="h4"
            sx={{
              fontWeight: 700,
              mb: 1.5,
              fontFamily:
                '"Montserrat", sans-serif',
              background:
                "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
              backgroundClip: "text",
              WebkitBackgroundClip:
                "text",
              WebkitTextFillColor:
                "transparent",
            }}
          >
            Create Account
          </Typography>

          <Typography
            variant="body1"
            color="text.secondary"
          >
            Join RBI ChatBot
          </Typography>
        </Box>

        <TextField
          fullWidth
          label="Username"
          value={username}
          onChange={(e) =>
            setUsername(
              e.target.value
            )
          }
          sx={{ mb: 2 }}
        />

        <TextField
          fullWidth
          label="Email"
          type="email"
          value={email}
          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
          sx={{ mb: 2 }}
        />

        <TextField
          fullWidth
          label="Password"
          type="password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
          sx={{ mb: 3 }}
        />

        <Button
          fullWidth
          variant="contained"
          size="large"
          onClick={handleSignup}
          sx={{
            py: 1.5,
            borderRadius: 2,
            textTransform: "none",
            fontSize: "1rem",
            fontWeight: 600,
            background:
              "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",

            "&:hover": {
              background:
                "linear-gradient(135deg, #5568d3 0%, #653a91 100%)",
            },
          }}
        >
          Create Account
        </Button>

        <Button
          fullWidth
          sx={{ mt: 2 }}
          onClick={() =>
            navigate("/login")
          }
        >
          Already have an account?
        </Button>
      </Paper>
    </Container>
  </Box>
);
}

export default SignupPage;