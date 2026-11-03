
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class TextSummarizer:

    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )

        print("Loading model...")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name
        )

        self.model.eval()

        print("Summarizer is ready!")

    def summarize(self, text: str) -> str:

        # Convert input text into tokens
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )

        # Generate summary
        with torch.inference_mode():
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_new_tokens=100,
                num_beams=4,
                do_sample=False
            )

        # Convert generated tokens into text
        summary = self.tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        return summary
