# https://stackoverflow.com/questions/18406570/python-record-audio-on-detected-sound?newreg=ce474bdf18e043e0911502ec2587e97c

import pyaudio
import math
import struct
import wave
import time
from ayarlar import *

class Recorder:
    @staticmethod
    def rms(frame):
        count = len(frame) / Genişlik
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * Normalleştirme
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=Biçim,
                                  channels=KanalSayısı,
                                  rate=Frekans,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=ParçaDeğeri)
        self.done = False

    def record(self):
        print('Kayıt başladı')
        rec = []
        current = time.time()
        end = time.time() + Normalleştirme

        while current <= end:

            data = self.stream.read(ParçaDeğeri)
            if self.rms(data) >= Hassasiyet: end = time.time() + SessizlikSüresi

            current = time.time()
            rec.append(data)
        self.write(b''.join(rec))

    def write(self, recording):
        filename = "sounds/recording.wav"

        wf = wave.open(filename, 'wb')
        wf.setnchannels(KanalSayısı)
        wf.setsampwidth(self.p.get_sample_size(Biçim))
        wf.setframerate(Frekans)
        wf.writeframes(recording)
        wf.close()
        self.done = True

    def listen(self):
        while not self.done:
            input = self.stream.read(ParçaDeğeri)
            rms_val = self.rms(input)
            if rms_val > Hassasiyet:
                self.record()

if __name__ == "__main__":
    a = Recorder()

    a.listen()