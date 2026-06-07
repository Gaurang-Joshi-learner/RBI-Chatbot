import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Navbar from './components/Navbar';
import ChatPage from './pages/ChatPage';
import LoginPage from './pages/LoginPage';
import DocumentLibrary from './pages/DocumentLibrary';
import SearchPage from './pages/SearchPage';
import AdminDashboard from './pages/AdminDashboard';
import ProtectedRoute from './components/ProtectedRoute';
import { useAuthStore } from './store/authStore';
import SignupPage from './pages/Signup';
import ForgotPasswordPage from "./pages/ForgotPasswordPage";
import VerifyOtpPage from "./pages/VerifyOtpPage";
import ResetPasswordPage from "./pages/ResetPasswordPage";
import './App.css';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#6366f1',
      light: '#818cf8',
      dark: '#4f46e5',
    },
    secondary: {
      main: '#8b5cf6',
    },
    background: {
      default: '#f8fafc',
      paper: '#ffffff',
    },
  },
  typography: {
    fontFamily: '"Montserrat", "Roboto", "Helvetica", "Arial", sans-serif',
    h1: {
      fontWeight: 700,
      letterSpacing: '-0.5px',
    },
    h2: {
      fontWeight: 700,
      letterSpacing: '-0.5px',
    },
    h3: {
      fontWeight: 600,
      letterSpacing: '-0.3px',
    },
    h4: {
      fontWeight: 600,
      letterSpacing: '-0.3px',
    },
    h5: {
      fontWeight: 600,
      letterSpacing: '-0.2px',
    },
    h6: {
      fontWeight: 600,
      letterSpacing: '-0.1px',
    },
    body1: {
      fontWeight: 400,
      letterSpacing: '0.01em',
    },
    body2: {
      fontWeight: 400,
      letterSpacing: '0.01em',
    },
    button: {
      fontWeight: 500,
      letterSpacing: '0.5px',
      textTransform: 'none',
    },
  },
  shape: {
    borderRadius: 12,
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          fontWeight: 500,
          borderRadius: 10,
          letterSpacing: '0.5px',
          padding: '10px 24px',
          boxShadow: 'none',
          '&:hover': {
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
          },
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            borderRadius: 12,
            fontFamily: '"Montserrat", sans-serif',
          },
        },
      },
    },
  },
});

function App() {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/login" element={isAuthenticated ? <Navigate to="/" replace /> : <LoginPage />} />
          <Route
  path="/signup"
  element={
    isAuthenticated
      ? <Navigate to="/" replace />
      : <SignupPage />
      
      
  }
  
/>
<Route
  path="/forgot-password"
  element={
    <ForgotPasswordPage />
  }
/>

<Route
  path="/verify-otp"
  element={
    <VerifyOtpPage />
  }
/>

<Route
  path="/reset-password"
  element={
    <ResetPasswordPage />
  }
/>
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <ChatPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/documents"
            element={
              <ProtectedRoute>
                <Navbar />
                <DocumentLibrary />
              </ProtectedRoute>
            }
          />
          <Route
            path="/search"
            element={
              <ProtectedRoute>
                <Navbar />
                <SearchPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/admin"
            element={
              <ProtectedRoute>
                <Navbar />
                <AdminDashboard />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<Navigate to={isAuthenticated ? "/" : "/login"} replace />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
