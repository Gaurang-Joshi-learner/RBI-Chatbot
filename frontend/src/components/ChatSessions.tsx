import {
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  IconButton,
  Typography,
  Divider,
  Button,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import AddIcon from "@mui/icons-material/Add";
import { useChatStore } from "../store/chatStore";

interface ChatSessionsProps {
  open: boolean;
  onClose: () => void;
}

const ChatSessions = ({ open, onClose }: ChatSessionsProps) => {
  const {
    sessions,
    currentSessionId,
    createSession,
    setCurrentSession,
    deleteSession,
  } = useChatStore();

  const handleNewChat = () => {
    createSession();
    onClose();
  };

  const handleSelectSession = (sessionId: number) => {
    setCurrentSession(sessionId);
    onClose();
  };

  const handleDeleteSession = (e: React.MouseEvent, sessionId: number) => {
    e.stopPropagation();
    deleteSession(sessionId);
  };

  return (
    <Drawer anchor="left" open={open} onClose={onClose} variant="temporary">
      <Box sx={{ width: 280, p: 2 }}>
        <Typography variant="h6" sx={{ mb: 2, fontWeight: 600 }}>
          Chat Sessions
        </Typography>
        <Button
          variant="contained"
          fullWidth
          startIcon={<AddIcon />}
          onClick={handleNewChat}
          sx={{ mb: 2, textTransform: "none", borderRadius: 2 }}
        >
          New Chat
        </Button>
        <Divider sx={{ mb: 2 }} />
        <List>
          {sessions.length === 0 ? (
            <Typography variant="body2" color="text.secondary" sx={{ p: 2, textAlign: "center" }}>
              No chat sessions yet. Create a new one to get started!
            </Typography>
          ) : (
            sessions.map((session) => (
              <ListItem
                key={session.id}
                disablePadding
                sx={{
                  mb: 1,
                  borderRadius: 2,
                  bgcolor: currentSessionId === session.id ? "action.selected" : "transparent",
                }}
              >
                <ListItemButton
                  onClick={() => handleSelectSession(session.id)}
                  sx={{ borderRadius: 2 }}
                >
                  <ListItemText
                    primary={session.title}
                    secondary={new Date(session.updatedAt).toLocaleDateString()}
                    primaryTypographyProps={{
                      sx: {
                        overflow: "hidden",
                        textOverflow: "ellipsis",
                        whiteSpace: "nowrap",
                      },
                    }}
                  />
                  <IconButton
                    edge="end"
                    onClick={(e) => handleDeleteSession(e, session.id)}
                    sx={{ ml: 1 }}
                    size="small"
                  >
                    <DeleteIcon fontSize="small" />
                  </IconButton>
                </ListItemButton>
              </ListItem>
            ))
          )}
        </List>
      </Box>
    </Drawer>
  );
};

export default ChatSessions;

