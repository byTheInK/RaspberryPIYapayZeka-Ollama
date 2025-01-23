import ollama
import vosk
from gtts import gTTS
from subprocess import run
import re

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
        message = input()

        try:
            response: ollama.ChatResponse = ollama.chat(
                model="gemma2",
                messages=[{"role": "user", "content": message}],
                )

            response = response.message.content
                
            print(response, end="", flush=True)

            gTTS(text=response,lang="tr",slow=False).save("sounds/tts.mp3")
            run(["cvlc", "--play-and-exit", "sounds/tts.mp3"])

        except ollama.ResponseError as e:
            if e.status_code == 404:
                pull("gemma2")

if __name__ == "__main__":
    main()