from fastapi import APIRouter
from app.services.similarity import cosine_similarity
from app.services.processor import preprocess
import re   

router = APIRouter()

indexer = None  # will inject from main


# ✅ helper function for snippet
def get_snippet(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # fallback if no proper sentences
    if len(sentences) < 2:
        return text[:200]
    
    return " ".join(sentences[:2])


@router.get("/search")
def search(q: str):
    query_tokens = preprocess(q)
    query_vector = indexer.vectorizer.transform(query_tokens)

    scores = []

    for doc, vec in indexer.doc_vectors.items():
        score = cosine_similarity(query_vector, vec)
        
        # ✅ use new snippet logic
        snippet = get_snippet(indexer.raw_docs[doc])

        scores.append({
            "document": doc,
            "score": round(score, 2),
            "snippet": snippet
        })

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    return {"results": scores[:3]}
