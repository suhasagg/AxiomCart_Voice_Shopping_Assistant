from app.rag.catalog import CatalogRetriever
from app.services.support import search_support
R=CatalogRetriever()

def orchestrator(s):
    q=s['message'].lower(); support=any(x in q for x in ['return','warranty','shipping','refund','order'])
    product=any(x in q for x in ['buy','product','headphone','earbud','charger','recommend','price','cart'])
    intent='both' if support and product else ('support' if support else 'product')
    return {'intent':intent,'events':[f'orchestrator:{intent}']}
def product_agent(s):
    ps=R.search(s['message']); text='; '.join(f"{p['name']} (${p['price']:.0f}, stock {p['stock']})" for p in ps[:3])
    approval=any(x in s['message'].lower() for x in ['checkout','place order','purchase now'])
    return {'products':ps,'product_answer':text,'needs_approval':approval,'events':['product_agent:retrieved']}
def support_agent(s):
    hits=search_support(s['message']); return {'support':hits,'support_answer':' '.join(hits),'events':['support_agent:grounded']}
def synthesize(s):
    parts=[x for x in [s.get('product_answer'),s.get('support_answer')] if x]
    if s.get('needs_approval') and not s.get('approved'): parts.append('Checkout is prepared but requires explicit human approval before any irreversible action.')
    elif s.get('needs_approval') and s.get('approved'): parts.append('Approval recorded. Demo mode does not charge a payment method; a production checkout saga would start here.')
    return {'answer':' '.join(parts),'events':['synthesizer:complete']}
