KB={"return":"Returns are accepted within 30 days when eligible.","warranty":"Electronics include a one-year limited warranty in this demo.","shipping":"Standard shipping is 3-5 business days in this demo."}
def search_support(q):
    q=q.lower(); hits=[v for k,v in KB.items() if k in q]
    return hits or ["No grounded support article matched; escalate to a human support specialist."]
