import ollama
import vosk

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
            for chunk in ollama.chat(
                model="gemma2",
                messages=[{"role": "user", "content": message}],
                stream=True,
                ):

                content = chunk["message"]["content"]
                
                print(content, end="", flush=True)
        
        except ollama.ResponseError as e:
            if e.status_code == 404:
                pull("gemma2")



if __name__ == "__main__":
    main()