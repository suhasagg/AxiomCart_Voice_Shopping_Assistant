from fastapi import FastAPI, UploadFile, File
from app.core.models import ChatRequest
from app.agents.graph import build_graph
from app.voice.pipeline import VoicePipeline
import tempfile, os
app=FastAPI(title='AxiomCart Voice Shopping Assistant',version='1.0.0')
graph=build_graph(); voice=VoicePipeline()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/chat')
def chat(r:ChatRequest):
    cfg={'configurable':{'thread_id':r.thread_id}}
    state={'thread_id':r.thread_id,'user_id':r.user_id,'message':r.message,'approved':r.approved,'events':[]}
    return graph.invoke(state,config=cfg)
@app.post('/v1/voice')
async def voice_chat(thread_id:str,user_id:str,audio:UploadFile=File(...)):
    fd,path=tempfile.mkstemp(); os.close(fd)
    with open(path,'wb') as f: f.write(await audio.read())
    text=voice.transcribe(path); result=chat(ChatRequest(thread_id=thread_id,user_id=user_id,message=text)); os.unlink(path)
    return {'transcript':text,'result':result}
