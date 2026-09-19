from app.agents.graph import build_graph
def test_graph():
    g=build_graph(); r=g.invoke({'thread_id':'t','user_id':'u','message':'headphones return policy','approved':False,'events':[]},config={'configurable':{'thread_id':'t'}}); assert 'return' in r['answer'].lower(); assert r['products']
