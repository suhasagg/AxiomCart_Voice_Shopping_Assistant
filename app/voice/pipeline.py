import os
class VoicePipeline:
    def __init__(self): self.offline=os.getenv('OFFLINE_MODE','true').lower()=='true'
    def transcribe(self,path):
        if self.offline: return 'Recommend noise cancelling headphones and tell me the return policy'
        from openai import OpenAI
        with open(path,'rb') as f: return OpenAI().audio.transcriptions.create(model=os.getenv('WHISPER_MODEL','whisper-1'),file=f).text
    def speak(self,text,out):
        if self.offline:
            open(out,'wb').write(b'OFFLINE_TTS:'+text.encode()); return out
        from openai import OpenAI
        r=OpenAI().audio.speech.create(model=os.getenv('TTS_MODEL','gpt-4o-mini-tts'),voice=os.getenv('TTS_VOICE','alloy'),input=text)
        r.stream_to_file(out); return out
