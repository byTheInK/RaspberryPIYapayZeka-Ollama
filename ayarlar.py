import pyaudio

# Basit
Hassasiyet: int = 10
KanalSayısı: int = 1 # Lütfen bu değeri değiştirmeyiniz
SessizlikSüresi: float = 2

# Gelişmiş
Normalleştirme: float = (1.0/32768.0)
Frekans: int = 16000
Biçim = pyaudio.paInt16
Genişlik: int = 2
ParçaDeğeri: int = 1024
