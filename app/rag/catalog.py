import json, re
from pathlib import Path
DATA=Path(__file__).parents[1]/"data/products.json"
class CatalogRetriever:
    def __init__(self): self.items=json.loads(DATA.read_text())
    def search(self,q,k=5):
        words=set(re.findall(r"[a-z0-9]+",q.lower()))
        def score(p):
            text=(p['name']+' '+p['category']+' '+p['description']).lower()
            return sum(w in text for w in words)
        return sorted(self.items,key=score,reverse=True)[:k]
