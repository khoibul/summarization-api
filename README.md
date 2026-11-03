# Summarization API

## 1. Project Overview

Summarization API is a Python-based Web API that automatically summarizes English text using a pretrained Hugging Face model.

The project uses **BART Large CNN (`facebook/bart-large-cnn`)** to generate concise summaries from user-provided text.

The API is built with FastAPI and returns results in JSON format.

## 2. Student Information

- **Student Name:** Bùi Đăng Khôi
- **Student ID:** 25127203
- **Course:** Computational Thinking
- **University:** University of Science, VNU-HCM

## 3. Model Information

- **Model Name:** `facebook/bart-large-cnn`
- **Platform:** Hugging Face
- **Model Link:** https://huggingface.co/facebook/bart-large-cnn
- **Task:** Text Summarization
- **Description:** BART Large CNN is a pretrained sequence-to-sequence model fine-tuned for English text summarization.

## 4. Features

- Summarize English text using a pretrained BART model.
- Provide a RESTful API using FastAPI.
- Validate input data using Pydantic.
- Handle invalid input and inference errors.
- Return summarization results in JSON format.
- Provide interactive API documentation through Swagger UI.

## 5. Project Structure

```text
summarization-api/
│
├── services/
│   ├── __init__.py
│   └── summarizer.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. Installation

### Prerequisites

- Python 3.14.2
- pip

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/summarization-api.git
cd summarization-api
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 7. Running the API

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

The pretrained model will be downloaded from Hugging Face when it is loaded for the first time.

### Interactive API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

## 8. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns API information |
| GET | `/health` | Checks API health status |
| POST | `/predict` | Summarizes the provided text |

### 8.1 GET /

Returns basic information about the API.

**Example Response:**

```json
{
  "message": "Welcome to BART Text Summarization API!",
  "model": "facebook/bart-large-cnn",
  "docs": "/docs"
}
```

### 8.2 GET /health

Checks whether the API is running.

**Example Response:**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 8.3 POST /predict

Accepts English text and returns its generated summary.

**Example Request:**

```json
{
  "text": "Artificial intelligence is transforming many industries. In healthcare, AI systems help doctors analyze medical images and detect diseases earlier. In education, AI-powered tools provide personalized learning experiences."
}
```

**Example Response:**

```json
{
  "success": true,
  "model": "facebook/bart-large-cnn",
  "summary": "Artificial intelligence is transforming many industries..."
}
```

The actual summary depends on the input text and model generation.

### Input Validation

The API validates incoming requests:

- The `text` field is required.
- The input must be a string.
- The input must not be empty or contain only whitespace.
- The maximum input length is 10,000 characters.

Invalid requests return HTTP `422 Unprocessable Entity`.

Inference errors return HTTP `500 Internal Server Error`.

## 9. Technologies Used

- **Python** – Main programming language.
- **Hugging Face Transformers** – Loading and running the pretrained BART model.
- **PyTorch** – Deep learning framework.
- **FastAPI** – Building the Web API.
- **Pydantic** – Request data validation.
- **Uvicorn** – Running the API server.

## 10. Demo Video

[Insert your demonstration video link here.]

The demonstration video includes:

1. Introduction to the selected Hugging Face model.
2. Explanation of the project structure and implementation.
3. Running the FastAPI application.
4. Testing the API with different input texts.
5. Demonstrating the generated summaries.

