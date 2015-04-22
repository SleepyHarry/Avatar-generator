import pygame as pg
import os, sys, time, math, random

if __name__=="__main__":
    pg.init()
    try:
        size = width, height = int(sys.argv[2]), int(sys.argv[2])
    except:
        size = width, height = 600, 600

    try:
        ext = sys.argv[3]
    except:
        ext = ".bmp"

fps_tgt = 30
frame_delta = 1.0/fps_tgt
then = time.clock()

if __name__=="__main__":
    screen = pg.display.set_mode(size)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)

toMorse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
           "E": ".", "F": "..-.", "G": "--.", "H": "....",
           "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
           "M": "--", "N": "-.", "O": "---", "P": ".--.",
           "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
           "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
           "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
           "2": "..---", "3": "...--", "4": "....-", "5": ".....",
           "6": "-....", "7": "--...", "8": "---..", "9": "----."}

def makeAvatar(username, saveToFile = True):
    n = len(username)

    w, h = screen.get_size()

    squareHeight = h/n
    squareWidth = w/10

    slack = h-squareHeight*n

    brightness = sum(ord(c)*i for i, c in enumerate(username.upper()))%255

    brightColour = (sum(ord(c) for c in username.upper())*101%128+128,
                    sum(ord(c) for c in username.upper())*211%128+128,
                    sum(ord(c) for c in username.upper())*307%128+128)
                    
    #print brightColour

    pallette = {".": brightColour,
                "-": black}

    out = pg.Surface((width, height))
    out.fill(tuple(c/2 for c in brightColour))

    for y, c in enumerate(username.upper()):
        m = toMorse[c]
        for x, d in enumerate(m):
            out.fill(pallette[d], (x*squareWidth+h/2, y*squareHeight,
                                   squareWidth,
                                   squareHeight+slack*(not n-y-1)))
            out.fill(pallette[d], (-(x+1)*squareWidth+h/2, y*squareHeight,
                                   squareWidth,
                                   squareHeight+slack*(not n-y-1)))

    if saveToFile:
        pg.image.save(out, "resource/avatars/{}_avatar_{w}x{h}.{ext}".\
                      format(username, w=w, h=h, ext=ext))

    return out

if __name__=="__main__":
    OVERRIDE = False

    if not OVERRIDE:
        try:
            username = sys.argv[1]
        except:
            username = "SleepyHarry"

        result = makeAvatar(username)
    else:
        results = []
        for username in ["SleepyHarry", "mutatedllama", "professorlamp",
                         "dailyprogrammer", "sarlak", "sarlek", "sarlik",
                         "varlek"]:
            results.append(makeAvatar(username))
            result = random.choice(results)

    while True:
        now = time.clock()
        if now-then < frame_delta:
            continue
        else:
            then = now
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill(white)

        screen.blit(result, (0, 0))
        
        pg.display.flip()
