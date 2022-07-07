from vosk import Model, KaldiRecognizer
import os
import pyaudio
import webbrowser
import Adam
import basa

adam = Adam.Adam(basa.Base("localhost"))


def rech():
    model = Model("vosk-model-small-ru-0.22")  # полный путь к модели
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8000
    )
    stream.start_stream()

    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break

        a = rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()

        if a.split()[1] == '"text"' and a.split()[3] != '""':
            lst = a.split()
            lst.remove('{')
            lst.remove('"text"')
            lst.remove(':')
            lst.remove('}')

            lst = (" ".join(lst).replace('"',"")).split(" ")

            return (lst)


while True:
    adam.neiro(rech())
