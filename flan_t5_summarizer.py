from transformers import T5Tokenizer, T5ForConditionalGeneration
import textwrap

# Load Model
model_name = "google/flan-t5-large"  # Use "flan-t5-xl" for longer texts if you have a good GPU
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Research Paper Text
research_text = """
**Title:** Enhancing Research Paper Summarization using Retrieval-Augmented Generation (RAG)

**Abstract:**
Research paper summarization is a crucial task that helps scholars and researchers quickly grasp key insights from large volumes of academic literature. Traditional extractive and abstractive summarization techniques often struggle to balance informativeness and coherence. In this paper, we explore the use of Retrieval-Augmented Generation (RAG) for summarizing research papers. Our approach leverages a combination of ChromaDB for efficient information retrieval and a fine-tuned Transformer model for summarization. We evaluate our model's performance against standard benchmarks and demonstrate its advantages in generating high-quality, contextually rich summaries.

**1. Introduction**
The exponential growth of research papers has made it challenging for scholars to keep up with new developments. Automatic summarization techniques aim to address this issue by generating concise and meaningful summaries. Existing methods rely on either extractive or abstractive approaches, both of which have limitations. In this work, we propose a hybrid model that integrates retrieval-based methods with generative capabilities to improve summary relevance and coherence.

**2. Methodology**
Our proposed model utilizes Retrieval-Augmented Generation (RAG), which combines a retriever module and a generator module:
- **Retriever Module:** We use ChromaDB, a vector database, to efficiently retrieve relevant sections of a research paper based on a given query.
- **Generator Module:** A fine-tuned T5 model is used to generate a summary by leveraging the retrieved content.

The system workflow consists of document preprocessing, embedding storage in ChromaDB, retrieval of relevant information, and summary generation using the Transformer model.

**3. Experimental Setup**
We conducted experiments on a dataset of research papers across multiple domains. Our evaluation metrics include ROUGE scores and human evaluation for coherence and readability. We compare our RAG-based approach with baseline extractive (TextRank) and abstractive (BART) summarization models.

**4. Results and Discussion**
Our findings indicate that the RAG-based model outperforms traditional summarization methods in terms of informativeness and coherence. The use of retrieval mechanisms ensures that the generated summaries are more factually accurate compared to standard abstractive methods.

**5. Conclusion and Future Work**
This study demonstrates the effectiveness of Retrieval-Augmented Generation in summarizing research papers. Future work will focus on improving retrieval efficiency and exploring domain-specific fine-tuning of generative models to enhance summary quality further.

**References**
1. Lewis, M., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
2. Raffel, C., et al. (2020). Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).
3. Mihalcea, R., & Tarau, P. (2004). TextRank: Bringing Order into Texts.
4. Lin, C. Y. (2004). ROUGE: A Package for Automatic Evaluation of Summaries.


"""

# Function to summarize in chunks
def summarize_text(text, chunk_size=400):
    chunks = textwrap.wrap(text, width=chunk_size)  # Break text into chunks
    summaries = []
    
    for chunk in chunks:
        input_text = "Summarize: " + chunk
        inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
        output = model.generate(**inputs, max_length=100, num_beams=5, early_stopping=True)
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        summaries.append(summary)
    
    return " ".join(summaries)  # Merge summarized chunks

# Generate Summary
final_summary = summarize_text(research_text)
print("\n🔹 Summary:\n", final_summary)
