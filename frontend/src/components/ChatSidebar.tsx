import {
  Box,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  IconButton,
  Typography,
  Divider,
  Button,
  Tooltip,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import AddIcon from "@mui/icons-material/Add";
import LogoutIcon from "@mui/icons-material/Logout";
import { useChatStore } from "../store/chatStore";
import { useAuthStore } from "../store/authStore";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import {
  getSessions,
  getSessionMessages,
  deleteBackendSession,
} from "../services/api";


interface ChatSidebarProps {
  onNewChat: () => void;
}

const ChatSidebar = ({ onNewChat }: ChatSidebarProps) => {
const {
  currentSessionId,
  setCurrentSessionId,
  setMessages,
} = useChatStore();
  const logout = useAuthStore((state) => state.logout);
  const navigate = useNavigate();
  console.log("ChatSidebar mounted");
  const [backendSessions, setBackendSessions] =
  useState<any[]>([]);
  const loadSessions = async () => {

  try {

    const data =
      await getSessions();

    setBackendSessions(
      Array.isArray(data)
        ? data
        : []
    );

  } catch (error) {

    console.error(
      "Failed loading sessions",
      error
    );
  }
};
useEffect(() => {

  loadSessions();

  window.addEventListener(
    "refreshSessions",
    loadSessions
  );

  return () => {

    window.removeEventListener(
      "refreshSessions",
      loadSessions
    );
  };

}, []);

const handleSelectSession = async (
  sessionId: number
) => {

  try {

    const messages =
      await getSessionMessages(
        sessionId
      );

    setCurrentSessionId(
      sessionId
    );

    setMessages(
      messages.map((m: any) => ({
        id: m.id.toString(),
        role: m.role,
        content: m.content,
        timestamp: new Date(
          m.created_at
        ),
      }))
    );

  } catch (error) {

    console.error(
      "Failed loading messages",
      error
    );
  }
};

const handleDeleteSession = async (
  e: React.MouseEvent,
  sessionId: number
) => {

  e.stopPropagation();

  try {

    await deleteBackendSession(
      sessionId
    );

    const data =
      await getSessions();

    setBackendSessions(
      Array.isArray(data)
        ? data
        : []
    );

  } catch (error) {

    console.error(
      "Delete failed",
      error
    );
  }
};

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const formatDate = (date: Date) => {
    const today = new Date();
    const sessionDate = new Date(date);
    const diffTime = today.getTime() - sessionDate.getTime();
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays === 0) return "Today";
    if (diffDays === 1) return "Yesterday";
    if (diffDays < 7) return `${diffDays} days ago`;
    
    return sessionDate.toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
    });
  };

  return (
    <Box
      sx={{
        width: 280,
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        bgcolor: "#1a1a1f",
        borderRight: "1px solid rgba(255, 255, 255, 0.08)",
        color: "white",
        boxShadow: "2px 0 8px rgba(0, 0, 0, 0.1)",
      }}
    >
      {/* New Chat Button */}
      <Box sx={{ p: 2 }}>
        <Button
          fullWidth
          variant="contained"
          startIcon={<AddIcon />}
          onClick={onNewChat}
          sx={{
            bgcolor: "rgba(99, 102, 241, 0.15)",
            color: "#a5b4fc",
            textTransform: "none",
            borderRadius: 3,
            py: 1.5,
            fontWeight: 500,
            border: "1px solid rgba(99, 102, 241, 0.2)",
            transition: "all 0.2s ease",
            "&:hover": {
              bgcolor: "rgba(99, 102, 241, 0.25)",
              borderColor: "rgba(99, 102, 241, 0.4)",
              transform: "translateY(-1px)",
              boxShadow: "0 4px 12px rgba(99, 102, 241, 0.2)",
            },
            justifyContent: "flex-start",
            px: 2.5,
          }}
        >
          New Chat
        </Button>
      </Box>

      <Divider sx={{ borderColor: "rgba(255, 255, 255, 0.08)", mx: 2 }} />

      {/* Chat History List */}
      <Box
        sx={{
          flex: 1,
          overflowY: "auto",
          px: 1,
          "&::-webkit-scrollbar": {
            width: "6px",
          },
          "&::-webkit-scrollbar-track": {
            bgcolor: "transparent",
          },
          "&::-webkit-scrollbar-thumb": {
            bgcolor: "rgba(255, 255, 255, 0.15)",
            borderRadius: "3px",
            "&:hover": {
              bgcolor: "rgba(255, 255, 255, 0.25)",
            },
          },
        }}
      >
        {backendSessions.length === 0 ? (
          <Box sx={{ p: 4, textAlign: "center" }}>
            <Typography 
              variant="body2" 
              sx={{ 
                color: "rgba(255, 255, 255, 0.4)",
                fontSize: "0.875rem",
                fontWeight: 400,
              }}
            >
              No chat history yet
            </Typography>
          </Box>
        ) : (
          <List sx={{ p: 0, pt: 1 }}>
            {backendSessions.map((session) => (
              <ListItem
                key={session.id}
                disablePadding
                sx={{
                  position: "relative",
                  mb: 0.5,
                  "&:hover .delete-button": {
                    opacity: 1,
                  },
                }}
              >
                <ListItemButton
                  onClick={() => handleSelectSession(session.id)}
                  sx={{
                    py: 1.25,
                    px: 2,
                    borderRadius: 2,
                    mx: 1,
                    transition: "all 0.2s ease",
                    bgcolor:
                      currentSessionId === session.id
                        ? "rgba(99, 102, 241, 0.15)"
                        : "transparent",
                    border: currentSessionId === session.id 
                      ? "1px solid rgba(99, 102, 241, 0.3)" 
                      : "1px solid transparent",
                    "&:hover": {
                      bgcolor: "rgba(255, 255, 255, 0.05)",
                      transform: "translateX(2px)",
                    },
                  }}
                >
                  <ListItemText
                    primary={
                      <Typography
                        variant="body2"
                        sx={{
                          color: currentSessionId === session.id ? "#a5b4fc" : "rgba(255, 255, 255, 0.9)",
                          overflow: "hidden",
                          textOverflow: "ellipsis",
                          whiteSpace: "nowrap",
                          fontWeight: currentSessionId === session.id ? 600 : 500,
                          fontSize: "0.875rem",
                          letterSpacing: "0.01em",
                        }}
                      >
                        {session.title}
                      </Typography>
                    }
                    secondary={
                      <Typography
                        variant="caption"
                        sx={{
                          color: "rgba(255, 255, 255, 0.4)",
                          fontSize: "0.75rem",
                          fontWeight: 400,
                          mt: 0.25,
                        }}
                      >
                        {formatDate(
  new Date(session.created_at)
)}
                      </Typography>
                    }
                  />
                  <IconButton
                    className="delete-button"
                    size="small"
                    onClick={(e) => handleDeleteSession(e, session.id)}
                    sx={{
                      opacity: 0,
                      transition: "all 0.2s ease",
                      color: "rgba(255, 255, 255, 0.5)",
                      "&:hover": {
                        color: "#ef4444",
                        bgcolor: "rgba(239, 68, 68, 0.1)",
                        transform: "scale(1.1)",
                      },
                    }}
                  >
                    <DeleteIcon fontSize="small" />
                  </IconButton>
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        )}
      </Box>

      <Divider sx={{ borderColor: "rgba(255, 255, 255, 0.08)", mx: 2 }} />

      {/* User Info & Logout */}
      <Box sx={{ p: 2 }}>
        <Tooltip title="Logout" placement="right">
          <Button
            fullWidth
            startIcon={<LogoutIcon />}
            onClick={handleLogout}
            sx={{
              color: "rgba(255, 255, 255, 0.6)",
              textTransform: "none",
              justifyContent: "flex-start",
              px: 2.5,
              py: 1.25,
              borderRadius: 2,
              fontWeight: 500,
              transition: "all 0.2s ease",
              "&:hover": {
                bgcolor: "rgba(239, 68, 68, 0.1)",
                color: "#ef4444",
                transform: "translateX(2px)",
              },
            }}
          >
            Logout
          </Button>
        </Tooltip>
      </Box>
    </Box>
  );
};

export default ChatSidebar;

