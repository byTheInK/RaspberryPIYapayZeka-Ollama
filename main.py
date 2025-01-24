import ollama
from vosk import Model, KaldiRecognizer
from gtts import gTTS
from subprocess import run
from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
from os import system
import colorama
import re
import wave
from memory import Memory
from os.path import exists
from json import loads
from voice import Recorder

ENTRIES = 20
CONST_DATA = {"Language": "Türkçe"}

emoji_pattern = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF"
                            "\U0001F680-\U0001F6FF\U0001F700-\U0001F77F"
                            "\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF"
                            "\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F"
                            "\U0001FA70-\U0001FAFF\U00002700-\U000027BF]+")

done = False

def speechToText():
    if exists("vosk-model-small-tr-0.3"):
        model_path = "vosk-model-small-tr-0.3"
    else:
        model_path = "vosk-tr"

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    with wave.open("sounds/recording.wav", "rb") as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                return loads(result)["text"]

def generate(message):
    global done

    memory = Memory("memory.json")
    history = memory.load()
    new_history = []

    for entry in history.get("History", [])[-ENTRIES:]:
        if "user" in entry:
            new_history.append({"role": "user", "content": entry["user"]})
        if "assistant" in entry:
            new_history.append({"role": "assistant", "content": entry["assistant"]})

    new_history.append({"role": "user", "content": message})

    for key, value in CONST_DATA.items():
        new_history.append({"role": "system", "content": f"{key}: {value}"})

    done = False
    Thread(target=load).start()

    response = ollama.chat(
        model="gemma2",
        messages=new_history,
    ).message.content

    memory.save(message, response)
    done = True

    return response

def load():
    global done
    print("Yükleniyor: ", end="")

    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break

        terminal.write(f'\rYükleniyor: {c}')
        terminal.flush()
        sleep(0.15)

    terminal.flush()

def pull(model="gemma2"):
    print(f"{model.capitalize()} modeli bulunamadı")
    print(f"{model.capitalize()} modelini yüklemek ister misiniz? ([E]vet/[H]ayır)")
    message = input()

    if message.lower() == "e":
        try:
            ollama.pull(model)
        except ollama.ResponseError as e:
            print("Bir hata oluştu: \n", e)
    return 

def main():
    while True:
        print("Ses bekleniyor...")
        Recorder().listen()

        message = speechToText()

        try:
            response = generate(message)

            system("clear")
            print()

            tts_response = re.sub(r"\*", "", emoji_pattern.sub("", response))

            print(colorama.Fore.GREEN + response, end="", flush=True)
            print()

            if tts_response.strip():
                gTTS(text=tts_response,lang="tr",slow=False).save("sounds/tts.mp3")
                run(["cvlc", "--play-and-exit", "sounds/tts.mp3"])

        except ollama.ResponseError as e:
            if e.status_code == 404:
                pull()
                return

        except Exception as e:
            print("Bir hata oluştu: \n", e)

if __name__ == "__main__":
    colorama.init(autoreset=True)
    main()