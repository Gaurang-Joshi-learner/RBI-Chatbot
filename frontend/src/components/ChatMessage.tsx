import { Box, Typography, Link, Stack } from "@mui/material";
import LinkIcon from "@mui/icons-material/Link";
import type { ChatMessage as ChatMessageType } from "../types/chat";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import IconButton from "@mui/material/IconButton";
interface Props {
  message: ChatMessageType;
}

const ChatMessage = ({ message }: Props) => {
  const isUser = message.role === "user";

  const formatTimestamp = (date: Date) => {
    const now = new Date();
    const messageDate = new Date(date);
    const diffInSeconds = Math.floor((now.getTime() - messageDate.getTime()) / 1000);

    if (diffInSeconds < 60) return "Just now";
    if (diffInSeconds < 3600) return `${Math.floor(diffInSeconds / 60)}m ago`;
    if (diffInSeconds < 86400) return `${Math.floor(diffInSeconds / 3600)}h ago`;
    
    return messageDate.toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <Box
      sx={{
        display: "flex",
        gap: 3,
        mb: 4,
        flexDirection: isUser ? "row-reverse" : "row",
        alignItems: "flex-start",
        maxWidth: "768px",
        mx: "auto",
      }}
    >
  
<Box
  sx={{
    flex: 1,
    color: "rgba(255, 255, 255, 0.95)",

    bgcolor: isUser
      ? "rgba(88,101,242,0.15)"
      : "rgba(255,255,255,0.03)",

    border: isUser
      ? "1px solid rgba(88,101,242,0.3)"
      : "1px solid rgba(255,255,255,0.08)",

    borderRadius: "16px",

    padding: "18px",
  }}
>
      <Typography
  variant="body1"
  sx={{
    lineHeight: 1.8,
    wordBreak: "break-word",
    whiteSpace: "pre-wrap",
    mb: message.citations && message.citations.length > 0 ? 2.5 : 0,
    fontSize: "0.95rem",
    fontWeight: 400,
    fontFamily: '"Montserrat", sans-serif',
    letterSpacing: "0.01em",
  }}
>
  {message.content}
</Typography>

{!isUser && (
  <Box
    sx={{
      display: "flex",
      justifyContent: "flex-end",
      mt: 1,
    }}
  >
    <IconButton
      size="small"
      onClick={() =>
        navigator.clipboard.writeText(
          message.content
        )
      }
      sx={{
        color:
          "rgba(255,255,255,0.7)",
      }}
    >
      <ContentCopyIcon
        fontSize="small"
      />
    </IconButton>
  </Box>
)}

{/* Citations */}
{message.citations && message.citations.length > 0 && (
          <Box 
            sx={{ 
              mt: 2.5, 
              pt: 2.5, 
              borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            }}
          >
            <Typography
              variant="caption"
              sx={{
                display: "block",
                mb: 1.5,
                color: "rgba(255, 255, 255, 0.6)",
                fontWeight: 600,
                fontSize: "0.75rem",
                textTransform: "uppercase",
                letterSpacing: "1px",
                fontFamily: '"Montserrat", sans-serif',
              }}
            >
              Sources:
            </Typography>
            {!isUser && (
  <IconButton
    size="small"
    onClick={() =>
      navigator.clipboard.writeText(
        message.content
      )
    }
    sx={{
      mt: 1,
      color: "white",
    }}
  >
    <ContentCopyIcon
      fontSize="small"
    />
  </IconButton>
)}
            <Stack direction="column" spacing={1.25}>
              {message.citations.map((citation, index) => (
                <Link
                  key={index}
                  href={citation.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  sx={{
                    display: "flex",
                    alignItems: "center",
                    gap: 1,
                    color: "#10b981",
                    textDecoration: "none",
                    fontSize: "0.875rem",
                    fontWeight: 500,
                    fontFamily: '"Montserrat", sans-serif',
                    transition: "all 0.2s ease",
                    borderRadius: 1,
                    px: 1,
                    py: 0.5,
                    "&:hover": {
                      textDecoration: "none",
                      color: "#059669",
                      bgcolor: "rgba(16, 185, 129, 0.1)",
                      transform: "translateX(4px)",
                    },
                  }}
                >
                  <LinkIcon sx={{ fontSize: 18 }} />
                  <Typography 
                    variant="body2" 
                    sx={{ 
                      fontSize: "0.875rem",
                      fontWeight: 500,
                      fontFamily: '"Montserrat", sans-serif',
                    }}
                  >
                    {citation.title}
                    {citation.source && ` - ${citation.source}`}
                  </Typography>
                </Link>
              ))}
            </Stack>
          </Box>
        )}

       
        
      </Box>
    </Box>
  );
};

export default ChatMessage;
