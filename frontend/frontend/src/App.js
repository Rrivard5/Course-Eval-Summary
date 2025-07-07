import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    const res = await axios.post('http://localhost:5000/upload', formData);
    setResponse(res.data.result);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Course Evaluation Summarizer</h1>
      <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload and Analyze</button>
      <div style={{ marginTop: '2rem', whiteSpace: 'pre-wrap' }}>{response}</div>
    </div>
  );
}

export default App;
