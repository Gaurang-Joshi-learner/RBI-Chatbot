import { AppBar, Toolbar, Button, Typography, Box } from "@mui/material";
import { Link, useLocation } from "react-router-dom";
import ChatIcon from "@mui/icons-material/Chat";
import FolderIcon from "@mui/icons-material/Folder";
import SearchIcon from "@mui/icons-material/Search";
import AdminPanelSettingsIcon from "@mui/icons-material/AdminPanelSettings";

const Navbar = () => {
  const location = useLocation();

  const navItems = [
    { path: "/", label: "Chat", icon: <ChatIcon /> },
    { path: "/documents", label: "Documents", icon: <FolderIcon /> },
    { path: "/search", label: "Search", icon: <SearchIcon /> },
    { path: "/admin", label: "Admin", icon: <AdminPanelSettingsIcon /> },
  ];

  return (
    <AppBar 
      position="static" 
      elevation={2}
      sx={{ 
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      }}
    >
      <Toolbar sx={{ gap: 1, px: { xs: 2, sm: 3 } }}>
        <Typography
          variant="h6"
          component="div"
          sx={{ 
            flexGrow: 0, 
            mr: 4,
            fontWeight: 700,
            letterSpacing: '-0.5px',
          }}
        >
          RBI ChatBot
        </Typography>
        <Box sx={{ display: 'flex', gap: 0.5, flexGrow: 1 }}>
          {navItems.map((item) => (
            <Button
              key={item.path}
              color="inherit"
              component={Link}
              to={item.path}
              startIcon={item.icon}
              sx={{
                borderRadius: 2,
                px: 2,
                py: 1,
                backgroundColor: location.pathname === item.path 
                  ? 'rgba(255, 255, 255, 0.2)' 
                  : 'transparent',
                '&:hover': {
                  backgroundColor: 'rgba(255, 255, 255, 0.15)',
                },
                fontWeight: location.pathname === item.path ? 600 : 400,
              }}
            >
              {item.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
