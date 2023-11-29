import socket
from playsound import playsound
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import threading

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Ses düzeyi kontrolü için arayüzü alın
volume = cast(interface, POINTER(IAudioEndpointVolume))


def play(argggg):
    playsound(argggg)

def main():
    host = 'technology-soup.gl.at.ply.gg'
    port = 32880

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Bağlandı")
    while True:
        try:
            message = client.recv(1024)
            if message:
                if message.decode('utf-8') == "mute":
                    print("muted")
                    volume.SetMasterVolumeLevelScalar(0.0, None)
                    continue
                elif message.decode('utf-8') == "full":
                    print("fulled")
                    volume.SetMasterVolumeLevelScalar(1.0, None)
                    continue
                msg = message.decode('utf-8')
                print(msg)


                argg = msg + ".mp3"
                client_thread = threading.Thread(target=play, args=(argg,))
                client_thread.start()

        except Exception as e:
            print("Bir hata oluştu:", e)
            break

if __name__ == "__main__":
    main()
