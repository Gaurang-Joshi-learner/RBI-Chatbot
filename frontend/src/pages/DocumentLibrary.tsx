import { Container, Typography, Box, Paper, Grid, Card, CardContent, CardActions, Button } from "@mui/material";
import FolderIcon from "@mui/icons-material/Folder";
import DescriptionIcon from "@mui/icons-material/Description";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

const DocumentLibrary = () => {
  // Placeholder data - will be replaced with actual data from backend
  const documents = [
    { id: 1, name: "Sample Document 1.pdf", date: "2024-01-15", size: "2.4 MB" },
    { id: 2, name: "Sample Document 2.docx", date: "2024-01-14", size: "1.8 MB" },
    { id: 3, name: "Sample Document 3.xlsx", date: "2024-01-13", size: "3.2 MB" },
  ];

  return (
    <Box sx={{ bgcolor: "background.default", minHeight: "calc(100vh - 64px)", py: 4 }}>
      <Container maxWidth="lg">
        <Box sx={{ mb: 4, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <Typography variant="h4" sx={{ fontWeight: 600, color: "text.primary" }}>
            Document Library
          </Typography>
          <Button
            variant="contained"
            startIcon={<CloudUploadIcon />}
            sx={{ borderRadius: 2, textTransform: "none" }}
          >
            Upload Document
          </Button>
        </Box>

        {documents.length === 0 ? (
          <Paper
            sx={{
              p: 6,
              textAlign: "center",
              borderRadius: 3,
              bgcolor: "background.paper",
            }}
          >
            <FolderIcon sx={{ fontSize: 64, color: "text.secondary", mb: 2 }} />
            <Typography variant="h6" color="text.secondary" gutterBottom>
              No documents yet
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
              Upload your first document to get started
            </Typography>
            <Button variant="contained" startIcon={<CloudUploadIcon />}>
              Upload Document
            </Button>
          </Paper>
        ) : (
          <Grid container spacing={3}>
            {documents.map((doc) => (
              <Grid item xs={12} sm={6} md={4} key={doc.id}>
                <Card
                  sx={{
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    borderRadius: 3,
                    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
                    transition: "transform 0.2s, box-shadow 0.2s",
                    "&:hover": {
                      transform: "translateY(-4px)",
                      boxShadow: "0 4px 16px rgba(0,0,0,0.15)",
                    },
                  }}
                >
                  <CardContent sx={{ flexGrow: 1 }}>
                    <DescriptionIcon sx={{ fontSize: 48, color: "primary.main", mb: 2 }} />
                    <Typography variant="h6" gutterBottom sx={{ fontWeight: 600 }}>
                      {doc.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Uploaded: {doc.date}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Size: {doc.size}
                    </Typography>
                  </CardContent>
                  <CardActions sx={{ p: 2, pt: 0 }}>
                    <Button size="small" sx={{ textTransform: "none" }}>
                      View
                    </Button>
                    <Button size="small" sx={{ textTransform: "none" }}>
                      Download
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>
        )}
      </Container>
    </Box>
  );
};

export default DocumentLibrary;