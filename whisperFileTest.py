import whisper

model = whisper.load_model("base")
result = model.transcribe("ah.wav")
print(result["text"])
