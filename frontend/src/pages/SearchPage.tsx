import { Container, Typography, Box, Paper, TextField, Button, IconButton } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import { useState } from "react";

const SearchPage = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);

  const handleSearch = () => {
    // Placeholder for search functionality
    console.log("Searching for:", searchQuery);
    // Will be implemented with backend integration
  };

  return (
    <Box sx={{ bgcolor: "background.default", minHeight: "calc(100vh - 64px)", py: 4 }}>
      <Container maxWidth="md">
        <Typography variant="h4" sx={{ fontWeight: 600, mb: 4, textAlign: "center" }}>
          Search Documents
        </Typography>

        <Paper
          elevation={0}
          sx={{
            p: 3,
            borderRadius: 3,
            mb: 4,
            border: "1px solid",
            borderColor: "divider",
          }}
        >
          <Box sx={{ display: "flex", gap: 2 }}>
            <TextField
              fullWidth
              placeholder="Search for documents, keywords, or content..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyPress={(e) => {
                if (e.key === "Enter") {
                  handleSearch();
                }
              }}
              sx={{
                "& .MuiOutlinedInput-root": {
                  borderRadius: 2,
                },
              }}
            />
            <Button
              variant="contained"
              onClick={handleSearch}
              startIcon={<SearchIcon />}
              sx={{ borderRadius: 2, textTransform: "none", px: 4 }}
            >
              Search
            </Button>
          </Box>
        </Paper>

        {results.length === 0 && searchQuery === "" && (
          <Paper
            sx={{
              p: 6,
              textAlign: "center",
              borderRadius: 3,
              bgcolor: "background.paper",
            }}
          >
            <SearchIcon sx={{ fontSize: 64, color: "text.secondary", mb: 2 }} />
            <Typography variant="h6" color="text.secondary" gutterBottom>
              Start searching
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Enter a search query above to find documents and content
            </Typography>
          </Paper>
        )}

        {results.length === 0 && searchQuery !== "" && (
          <Paper
            sx={{
              p: 6,
              textAlign: "center",
              borderRadius: 3,
              bgcolor: "background.paper",
            }}
          >
            <Typography variant="h6" color="text.secondary" gutterBottom>
              No results found
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Try adjusting your search query
            </Typography>
          </Paper>
        )}
      </Container>
    </Box>
  );
};

export default SearchPage;