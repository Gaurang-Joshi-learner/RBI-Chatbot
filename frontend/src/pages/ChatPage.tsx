import { 
  Box, 
  TextField, 
  Typography, 
  IconButton,
  Alert,
  Snackbar,
  CircularProgress,
} from "@mui/material";
import { useState, useRef, useEffect } from "react";
import SendIcon from "@mui/icons-material/Send";
import MenuRoundedIcon from "@mui/icons-material/MenuRounded";
import ChatMessage from "../components/ChatMessage";
import TypingIndicator from "../components/TypingIndicator";
import ChatSidebar from "../components/ChatSidebar";
import { useChatStore } from "../store/chatStore";

import {
  sendChatMessage,
} from "../services/api";

const ChatPage = () => {
const {
  messages,
  isLoading,
  error,
  currentSessionId,
  addMessage,
  setLoading,
  setError,
  clearMessages,
  setCurrentSessionId,
} = useChatStore();

  const [input, setInput] = useState("");
  const [sidebarOpen, setSidebarOpen] =
  useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Initialize session if none exists
 

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput("");

    // Add user message
    addMessage({
      role: "user",
      content: userMessage,
    });

    // Set loading state
    setLoading(true);
    setError(null);

    try {
      const response =
  await sendChatMessage(
    userMessage,
    currentSessionId || undefined
  );

      if (!response?.answer) {
        throw new Error("Empty response from server");
      }
   if (
  !currentSessionId &&
  response.session_id
) {

  setCurrentSessionId(
    response.session_id
  );

  window.dispatchEvent(
    new Event("refreshSessions")
  );
}
      addMessage({
        role: "assistant",
        content: response.answer,
       citations: (response.sources || []).map((source) => ({
  title: source.title || "RBI Document",
  source: source.source || "RBI",
  issue_date: source.issue_date || "Unknown",
  url: "#",
})),
      });
    }  catch (err) {

  console.error("Chat error:", err);

  setError(
    "Unable to generate response right now. Please try again."
  );
  
    } finally {
      setLoading(false);
    }
  };

const handleNewChat = () => {

  setCurrentSessionId(null);

  clearMessages();

  setError(null);
};

  return (
    <Box
      sx={{
        display: "flex",
        height: "100vh",
        bgcolor: "#2d2d30",
        overflow: "hidden",
      }}
      
    >
      <IconButton
  onClick={() =>
    setSidebarOpen(
      !sidebarOpen
    )
  }
  sx={{
    position: "absolute",
    top: 20,
    left: sidebarOpen ? 320 : 20,
    color: "white",
    borderRadius: 2,
    zIndex: 9999,
    bgcolor:
      "rgba(255,255,255,0.08)",

    "&:hover": {
      bgcolor:
        "rgba(255,255,255,0.15)",
    },
  }}
>
 <MenuRoundedIcon />
</IconButton>
      
      {/* Sidebar */}
      {
  sidebarOpen && (
    <ChatSidebar
      onNewChat={handleNewChat}
    />
  )
}
     

      {/* Main Chat Area */}
      <Box
        sx={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          height: "100vh",
          bgcolor: "#2d2d30",
          position: "relative",
        }}
      >

        {/* Messages Area */}
        <Box
          sx={{
            flex: 1,
            overflowY: "auto",
            px: { xs: 3, sm: 6, md: 8 },
            py: 6,
            "&::-webkit-scrollbar": {
              width: "10px",
            },
            "&::-webkit-scrollbar-track": {
              bgcolor: "transparent",
            },
            "&::-webkit-scrollbar-thumb": {
              bgcolor: "rgba(255, 255, 255, 0.15)",
              borderRadius: "5px",
              border: "2px solid transparent",
              backgroundClip: "padding-box",
              "&:hover": {
                bgcolor: "rgba(255, 255, 255, 0.25)",
              },
            },
          }}
        >
          {messages.length === 0 ? (
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                height: "100%",
                color: "rgba(255, 255, 255, 0.8)",
              }}
            >
              <Typography 
                variant="h3" 
                gutterBottom 
                sx={{ 
                  fontWeight: 700, 
                  mb: 2, 
                  color: "white",
                  letterSpacing: "-0.5px",
                }}
              >
                RBI ChatBot
              </Typography>
              <Typography 
                variant="body1" 
                sx={{ 
                  color: "rgba(255, 255, 255, 0.6)",
                  fontSize: "1rem",
                  fontWeight: 400,
                }}
              >
                Start a conversation by typing a message below
              </Typography>
            </Box>
          ) : (
            <>
              {messages.map((message) => (
                <ChatMessage key={message.id} message={message} />
              ))}
              {isLoading && <TypingIndicator />}
              <div ref={messagesEndRef} />
            </>
          )}
        </Box>

        {/* Input Area */}
        <Box
          sx={{
            p: 3,
            borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            bgcolor: "#2d2d30",
            background: "linear-gradient(to top, rgba(0,0,0,0.1) 0%, transparent 100%)",
          }}
        >
          <Box
            display="flex"
            gap={2}
            alignItems="flex-end"
            sx={{
              maxWidth: "768px",
              mx: "auto",
            }}
          >
            <TextField
              fullWidth
              multiline
              maxRows={4}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey && !isLoading) {
                  e.preventDefault();
                  sendMessage();
                }
              }}
              placeholder="Message RBI ChatBot..."
              variant="outlined"
              disabled={isLoading}
              sx={{
                "& .MuiOutlinedInput-root": {
                  bgcolor: "#3c3c44",
                  color: "white",
                  borderRadius: 4,
                  fontFamily: '"Montserrat", sans-serif',
                  fontSize: "0.95rem",
                  transition: "all 0.2s ease",
                  "& fieldset": {
                    borderColor: "rgba(255, 255, 255, 0.1)",
                    borderWidth: "1.5px",
                  },
                  "&:hover fieldset": {
                    borderColor: "rgba(99, 102, 241, 0.4)",
                  },
                  "&.Mui-focused fieldset": {
                    borderColor: "rgba(99, 102, 241, 0.6)",
                    borderWidth: "2px",
                  },
                },
                "& .MuiInputBase-input::placeholder": {
                  color: "rgba(255, 255, 255, 0.4)",
                  opacity: 1,
                  fontWeight: 400,
                },
              }}
            />
            <IconButton
              onClick={sendMessage}
              disabled={!input.trim() || isLoading}
              sx={{
                bgcolor: isLoading 
                  ? "rgba(255, 255, 255, 0.1)" 
                  : "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
                color: "white",
                width: 44,
                height: 44,
                borderRadius: 3,
                transition: "all 0.2s ease",
                boxShadow: !isLoading && input.trim() 
                  ? "0 4px 12px rgba(99, 102, 241, 0.3)" 
                  : "none",
                "&:hover": {
                  bgcolor: isLoading 
                    ? "rgba(255, 255, 255, 0.1)" 
                    : "linear-gradient(135deg, #5855eb 0%, #7c3aed 100%)",
                  transform: isLoading ? "none" : "translateY(-2px)",
                  boxShadow: isLoading 
                    ? "none" 
                    : "0 6px 16px rgba(99, 102, 241, 0.4)",
                },
                "&:disabled": {
                  bgcolor: "rgba(255, 255, 255, 0.05)",
                  color: "rgba(255, 255, 255, 0.3)",
                },
              }}
            >
              {isLoading ? (
                <CircularProgress size={20} sx={{ color: "white" }} />
              ) : (
                <SendIcon fontSize="small" />
              )}
            </IconButton>
          </Box>
        </Box>

        {/* Error Snackbar */}
        <Snackbar
          open={!!error}
          autoHideDuration={6000}
          onClose={() => setError(null)}
          anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
        >
          <Alert onClose={() => setError(null)} severity="error" sx={{ width: "100%" }}>
            {error}
          </Alert>
        </Snackbar>
      </Box>
    </Box>
  );
};

export default ChatPage;
