import pyaudio
import wave

def record_audio(filename, duration=5):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=sample_format, channels=channels,
                    rate=fs, frames_per_buffer=chunk, input=True)
    frames = []

    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
