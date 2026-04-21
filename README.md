# 🔍 Semantic Document Search Engine

A custom-built semantic search engine that retrieves the most relevant documents for a given query using **manual TF-IDF vectorization** and **cosine similarity** — without relying on external NLP/AI libraries.

---

## 🚀 Objective

Build a backend system that:

* Accepts a search query
* Computes similarity with a corpus of documents
* Returns the **top 3 most relevant documents** with:

  * Filename
  * Similarity score
  * Text snippet (first 2 sentences)

---

## 🧠 Approach

### 1. Text Preprocessing

* Lowercasing
* Removing special characters
* Tokenization using regex

### 2. Vectorization (Manual TF-IDF)

* Term Frequency (TF)
* Inverse Document Frequency (IDF)
* Fully custom implementation (no sklearn/gensim)

### 3. Similarity Computation

* Cosine similarity between query vector and document vectors

### 4. Ranking

* Sort documents based on similarity score
* Return top 3 results

---

## 📁 Project Structure

```
semantic-search-engine/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── search.py
│   ├── services/
│   │   ├── indexer.py
│   │   ├── vectorizer.py
│   │   ├── similarity.py
│   │   └── processor.py
│   └── utils/
│       └── file_loader.py
│
├── documents/        # 50 text files
├── frontend/
│   └── index.html
├── README.md
└── pyproject.toml
```

---

## ⚙️ Installation (Using UV)

```bash
uv init
uv add fastapi uvicorn numpy
```

---

## ▶️ Run the Application

### Start Backend

```bash
uv run uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### Open API Docs

```
http://127.0.0.1:8000/docs
```

---

### Run Frontend

**Option 1:**

* Open `frontend/index.html` directly in browser

**Option 2 (Recommended):**

```bash
cd frontend
python -m http.server 5500
```
Then open:

```
http://127.0.0.1:5500
```

---

## 🔍 API Usage

### Endpoint

```
GET /search?q=<query>
```

### Example

```
GET /search?q=artificial intelligence in finance
```

---

### Sample Response

```json
	
Response body

{
  "results": [
    {
      "document": "doc_04_ai_in_agriculture.txt",
      "score": 0.49,
      "snippet": "**AI in Agriculture: Transforming Farming Practices for a Sustainable Future**\n\nArtificial Intelligence (AI) is revolutionizing various sectors, and agriculture is no exception. The integration of AI technologies into farming practices is reshaping the agricultural landscape, enhancing productivity, and promoting sustainability."
    },
    {
      "document": "doc_16_ai_and_robotics.txt",
      "score": 0.11,
      "snippet": "**AI and Robotics: Transforming Industries and Daily Life**\n\nArtificial Intelligence (AI) and robotics have emerged as transformative forces across numerous sectors, reshaping how businesses operate and how individuals interact with technology in their daily lives. The convergence of these two fields has given rise to innovative applications that streamline processes, enhance productivity, and improve decision-making."
    },
    {
      "document": "doc_34_ai_in_autonomous_drones.txt",
      "score": 0.09,
      "snippet": "### AI in Autonomous Drones: Transforming Industries and Shaping the Future\n\nThe integration of artificial intelligence (AI) in autonomous drones has ushered in a new era of innovation across various sectors. These unmanned aerial vehicles (UAVs), enhanced with sophisticated AI algorithms, are transforming operations in industries such as agriculture, logistics, surveillance, and environmental monitoring."
    }
  ]
}
```

---

## ✨ Features

* Manual TF-IDF implementation
* Cosine similarity calculation
* Top-k document retrieval (Top 3)
* Sentence-based snippet extraction
* Lightweight frontend UI
* FastAPI backend with modular structure

---

## ⚠️ Constraints Followed

* ❌ No external NLP libraries (sklearn, spacy, gensim)
* ✅ Used only standard Python libraries (math, re, collections)
* ✅ Implemented all logic manually

---

## 🔄 Bonus Feature

### Rebuild Index

```
GET /index
```

Reprocesses the document folder when new files are added.

---

## 💡 Design Decisions

* **TF-IDF over Bag-of-Words**

  * Gives importance to meaningful words
  * Reduces noise from common terms

* **Cosine Similarity**

  * Measures similarity independent of document length
  * Ideal for text comparison

* **Modular Architecture**

  * Clear separation of concerns
  * Easy to maintain and extend

---

## 🚀 Future Improvements

* Highlight matched query terms in snippet
* Implement inverted index for faster search
* Add pagination
* Improve UI with better UX
* Upgrade to embedding-based search (if allowed)

---

## 🎤 Interview Notes

* Built complete NLP pipeline from scratch
* Followed all constraints strictly (no external NLP tools)
* Focused on clean architecture and scalability
* Demonstrated full flow: UI → API → Processing → Results

---

## 👩‍💻 Author

Developed as part of a Gen AI Developer assessment task.
