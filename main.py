# Circuit Playground Express Chord Guitar
# scruss - 2017-12

# these libraries should be installed by default in CircuitPython
import touchio
import board
import time
import neopixel
import digitalio
import audioio

# touch pins, anticlockwise from battery connector
touch_pins= [
    touchio.TouchIn(board.A1),
    touchio.TouchIn(board.A2),
    touchio.TouchIn(board.A3),
    touchio.TouchIn(board.A4),
    touchio.TouchIn(board.A5),
    touchio.TouchIn(board.A6),
    touchio.TouchIn(board.A7)
]

# 16 kHz 16-bit mono audio files, in same order as pins
chord_files = [
    "chord-C.wav",
    "chord-D.wav",
    "chord-E.wav",
    "chord-Em.wav",
    "chord-F.wav",
    "chord-G.wav",
    "chord-A.wav"
]

# nearest pixels to touch pads
chord_pixels = [ 6, 8, 9, 0, 1, 3, 4 ]

# set up neopixel access
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

# set up speaker output
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

# poll touch pins
while True:
    for i in range(len(touch_pins)):
        # if a pin is touched
        if touch_pins[i].value:
            # set nearest pixel
            pixels[chord_pixels[i]] = (0, 0x10, 0) 
            pixels.show()
            # open and play corresponding file
            f=open(chord_files[i], "rb") 
            a = audioio.AudioOut(board.A0, f)
            a.play()
            # blank nearest pixel
            pixels[chord_pixels[i]] = (0, 0, 0) 
            pixels.show()
            # short delay to let chord sound
            # might want to try this a little shorter for faster play
            time.sleep(0.2)
