const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/bfhl', (req, res) => {
  const data = req.body.data || [];
  const numbers = data.filter(item => !isNaN(item));
  const alphabets = data.filter(item => /^[a-zA-Z]$/.test(item));
  const highestAlphabet = alphabets.length ? [alphabets.sort((a, b) => b.toLowerCase().localeCompare(a.toLowerCase()))[0]] : [];

  const response = {
    is_success: true,
    user_id: "john_doe_17091999",
    email: "john@xyz.com",
    roll_number: "ABCD123",
    numbers,
    alphabets,
    highest_alphabet: highestAlphabet
  };

  res.json(response);
});

app.get('/', (req, res) => {
  res.json({ status: "healthy" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
}); 