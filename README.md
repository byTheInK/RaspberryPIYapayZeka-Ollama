# Hakkında

Bu proje terk edilmiş bir projeyi yenilemiştir. Bu proje sayesinde Raspberry Pi cihazınıza Alexa tarzında bir yapay zeka kurabilirsiniz. Ollama ve Vosk sayesinde hızlı ve güvenli bir deneyim elde edebilirsiniz.

> [!CAUTION]
> Bu proje tamamlanmış durumda değildir. Performans sorunları ve başka hatalar ortaya çıkabilir. Lütfen bu hataları [geliştiriciye bildirin](https://github.com/byTheInK/RaspberryPIYapayZeka-Ollama/issues)
# Donanım
- Mikrofon
- Hoparlör
- NVIDIA Ekran kartı (Önerilir)

# Kurulum

Yapay zekayı kurmak için [Debian](https://tr.wikipedia.org/wiki/Debian) tabanlı bir [Linux](https://tr.wikipedia.org/wiki/Linux) dağıtımı gerekiyor. Eğer [Raspberry Pi OS](https://www.raspberrypi.com/software/) veya eski adıyla [Raspbian](https://www.raspbian.org/) kullanıyorsanız yeterli olucaktır. Aşağıdaki kodu kullanarak işletim sisteminize [Ollama](https://github.com/ollama/ollama), [Vosk](https://alphacephei.com/vosk/) ve diğer gerekli paketleri indiricek bir betik dosyası çalıştıracaksınız.

> [!TIP]
> Kurulum esnasında bazı paketleri indirmeniz gerektiği soruluyorsa **"e"** yazınız. Bu gerekli paketleri indirecektir.

```bash
cd ~
sudo apt-get install -y git
git clone https://github.com/byTheInK/RaspberryPIYapayZeka-Ollama.git
cd ./RaspberryPIYapayZeka-Ollama
sh ./installer
```

# Güncelleme

```bash
cd ~
sudo mv RaspberryPIYapayZeka-Ollama/ayarlar.py RaspberryPIYapayZeka-Ollama/vosk-tr RaspberryPIYapayZeka-Ollama/memory.py /tmp/
sudo rm -rf RaspberryPIYapayZeka-Ollama
git clone https://github.com/byTheInK/RaspberryPIYapayZeka-Ollama.git
sudo mv /tmp/ayarlar.py /tmp/vosk-tr /tmp/memory.py RaspberryPIYapayZeka-Ollama/
cd RaspberryPIYapayZeka-Ollama
sudo sh installer
```

# Çalıştırma

Çalıştırmak için komut satırınıza `yzpi` yazmanız yeterli olucaktır.

# Kaldırma

```bash
sudo rm -rf  ~/RaspberryPIYapayZeka-Ollama
```

# Ayarlar

Ayarlara girmek için istediğiniz bir metin düzenleyicisi seçin(GNU Nano, Vim, Kate, Visual Studio Code, ...) ve `"~/RaspberryPIYapayZeka-Ollama/ayarlar.py"` dosyasını düzenleyin.

**Örnek:**

```bash
nano ~/RaspberryPIYapayZeka-Ollama/ayarlar.py
```
