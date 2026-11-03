from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

from services.summarizer import TextSummarizer


# 1. Create FastAPI application
app = FastAPI(
    title="BART Text Summarization API",
    description="An API that summarizes English text using BART.",
    version="1.0.0"
)


# 2. Load the model
summarizer = TextSummarizer()


# 3. Define input data structure

class SummarizationRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=10000,
        description="The text that needs to be summarized."
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Text cannot contain only whitespace.")

        return value.strip()


# 4. GET /
@app.get("/")
def home():
    return {
        "message": "Welcome to BART Text Summarization API!",
        "model": "facebook/bart-large-cnn",
        "docs": "/docs"
    }


# 5. GET /health
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True
    }


# 6. POST /predict
@app.post("/predict")
def predict(request: SummarizationRequest):
    try:
        summary = summarizer.summarize(request.text)

        return {
            "success": True,
            "model": "facebook/bart-large-cnn",
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {str(e)}"
        )
