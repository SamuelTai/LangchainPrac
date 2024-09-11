from transformers import pipeline

def transcribe_audio(filename):
    asr = pipeline("automatic-speech-recognition")
    transcription = asr(filename)
    return transcription['text']
