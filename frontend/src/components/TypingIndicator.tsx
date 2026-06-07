import { Box, Typography } from "@mui/material";

const TypingIndicator = () => {
  return (
    <Box
      sx={{
        display: "flex",
        gap: 3,
        mb: 4,
        alignItems: "flex-start",
        maxWidth: "768px",
        mx: "auto",
      }}
    >
      <Box
        sx={{
          width: 30,
          height: 30,
          borderRadius: "50%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          bgcolor: "#ab68ff",
          color: "white",
          flexShrink: 0,
        }}
      >
        <Box
          sx={{
            display: "flex",
            gap: 0.3,
            "& > div": {
              width: 6,
              height: 6,
              borderRadius: "50%",
              bgcolor: "white",
              animation: "typing 1.4s infinite",
              "&:nth-of-type(2)": {
                animationDelay: "0.2s",
              },
              "&:nth-of-type(3)": {
                animationDelay: "0.4s",
              },
            },
            "@keyframes typing": {
              "0%, 60%, 100%": {
                transform: "translateY(0)",
                opacity: 0.7,
              },
              "30%": {
                transform: "translateY(-8px)",
                opacity: 1,
              },
            },
          }}
        >
          <Box />
          <Box />
          <Box />
        </Box>
      </Box>
      <Box
        sx={{
          flex: 1,
          color: "rgba(255, 255, 255, 0.7)",
        }}
      >
        <Typography 
          variant="body2" 
          sx={{ 
            fontSize: "0.9rem",
            fontFamily: '"Montserrat", sans-serif',
            fontWeight: 400,
            fontStyle: "italic",
          }}
        >
          Generating response...
        </Typography>
      </Box>
    </Box>
  );
};

export default TypingIndicator;

