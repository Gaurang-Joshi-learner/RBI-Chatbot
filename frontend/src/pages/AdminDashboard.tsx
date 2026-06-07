import { Container, Typography, Box, Grid, Paper, Card, CardContent } from "@mui/material";
import PeopleIcon from "@mui/icons-material/People";
import DescriptionIcon from "@mui/icons-material/Description";
import ChatIcon from "@mui/icons-material/Chat";
import AnalyticsIcon from "@mui/icons-material/Analytics";

const AdminDashboard = () => {
  const stats = [
    { title: "Total Users", value: "1,234", icon: <PeopleIcon />, color: "#667eea" },
    { title: "Documents", value: "567", icon: <DescriptionIcon />, color: "#f093fb" },
    { title: "Chat Sessions", value: "8,901", icon: <ChatIcon />, color: "#4facfe" },
    { title: "Analytics", value: "Active", icon: <AnalyticsIcon />, color: "#43e97b" },
  ];

  return (
    <Box sx={{ bgcolor: "background.default", minHeight: "calc(100vh - 64px)", py: 4 }}>
      <Container maxWidth="lg">
        <Typography variant="h4" sx={{ fontWeight: 600, mb: 4 }}>
          Admin Dashboard
        </Typography>

        <Grid container spacing={3}>
          {stats.map((stat, index) => (
            <Grid item xs={12} sm={6} md={3} key={index}>
              <Card
                sx={{
                  borderRadius: 3,
                  boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
                  transition: "transform 0.2s, box-shadow 0.2s",
                  "&:hover": {
                    transform: "translateY(-4px)",
                    boxShadow: "0 4px 16px rgba(0,0,0,0.15)",
                  },
                }}
              >
                <CardContent>
                  <Box
                    sx={{
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "space-between",
                      mb: 2,
                    }}
                  >
                    <Box
                      sx={{
                        width: 56,
                        height: 56,
                        borderRadius: 2,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        bgcolor: `${stat.color}20`,
                        color: stat.color,
                      }}
                    >
                      {stat.icon}
                    </Box>
                  </Box>
                  <Typography variant="h4" sx={{ fontWeight: 700, mb: 0.5 }}>
                    {stat.value}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {stat.title}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>

        <Paper
          sx={{
            mt: 4,
            p: 4,
            borderRadius: 3,
            bgcolor: "background.paper",
          }}
        >
          <Typography variant="h6" sx={{ fontWeight: 600, mb: 2 }}>
            System Overview
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Admin dashboard functionality will be expanded in future updates. This section will
            include detailed analytics, user management, and system configuration options.
          </Typography>
        </Paper>
      </Container>
    </Box>
  );
};

export default AdminDashboard;