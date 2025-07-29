from transformers import T5Tokenizer, T5ForConditionalGeneration
import textwrap
import torch

# Load Flan-T5 Model
model_name = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available
model.to(device)

# Function to summarize in chunks
def summarize_text(text, chunk_size=400):
    chunks = textwrap.wrap(text, width=chunk_size)  # Split long text
    summaries = []
    
    for chunk in chunks:
        input_text = "Summarize: " + chunk
        inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
        output = model.generate(**inputs, max_length=100, num_beams=5, early_stopping=True)
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        summaries.append(summary)
    
    return " ".join(summaries)  # Merge summarized chunks

# Test Summarization
retrieved_text = "Artificial Intelligence is transforming healthcare by improving diagnostics and automating workflows."
summary = summarize_text(retrieved_text)
print("\n🔹 Summary:\n", summary)
