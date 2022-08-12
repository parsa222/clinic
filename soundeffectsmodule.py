import winsound


class Sounds:

    def loginsound(self):
        freq = 100
        dur = 50
        for i in range(0, 4):
            winsound.Beep(freq, dur)
            freq += 100
            dur += 50

    def logoutsound(self):
        freq = 500
        dur = 150
        for i in range(0, 4):
            winsound.Beep(freq, dur)
            freq -= 100
            dur -= 50
    def quitsound(self):

        winsound.PlaySound('./sounds/xpshutdown.wav', winsound.SND_FILENAME)
    def errorsound(self):
        winsound.PlaySound('./sounds/NO.wav', winsound.SND_FILENAME)

if __name__ == "__main__":
    print("plz run clinic.py")