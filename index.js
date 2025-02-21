const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/bfhl', (req, res) => {
  const data = req.body.data || [];
  // Convert all items to strings to handle both number and string inputs
  const numbers = data.filter(item => !isNaN(String(item))).map(String);
  const alphabets = data.filter(item => /^[a-zA-Z]$/.test(String(item)));
  const highestAlphabet = alphabets.length ? 
    [alphabets.sort((a, b) => b.localeCompare(a, undefined, {sensitivity: 'base'}))[0]] : 
    [];

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