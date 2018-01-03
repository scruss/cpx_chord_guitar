# cpx_chord_guitar

Simple 7-chord touch-pad guitar for the Adafruit [Circuit Playground Express](https://www.adafruit.com/product/3333) (“CPX”). Plays C, D, E, F, G and A major chords, plus E*min*. Enough for traditional 3-chord (Ⅰ, Ⅳ, Ⅴ) songs in the keys of C, D and G.

* Demo video: [Circuit Playground Express Chord Guitar](https://www.youtube.com/watch?v=lwbUNxSwCiw)

* Writeup: [Circuit Playground Express Chord Guitar](http://scruss.com/blog/2017/12/27/circuit-playground-express-chord-guitar/)

## Directions

Upload all the chord WAV files + main.py to your CPX. Play a chord by touching a pad:

    PAD       CHORD
    ========  ========  
     A1        C
     A2        D
     A3        E
     A4        Emin
     A5        F
     A6        G
     A7        A

## Synthesizing chords

The chords were made with [SoX](http://sox.sourceforge.net/) and this script:

    cat guitar.txt | while read chord foo first third fifth
    do
      echo "$chord" :
      sox -n -r 16000 -b 16 "chord-${chord}.wav" synth 1 pl "$first" pl "$third" pl "$fifth" delay 0 .05 .1 remix - fade p 0 1 0.5 norm -5 reverb
    done
    
along with this file, **guitar.txt**:

    G   :  G2  B2  D3
    C   :  C3  E3  G4
    D   :  D3  F#4 A3
    F   :  F3  A3  C4
    A   :  A3  C#4 E4
    E   :  E2  G#3 B3
    Em  :  E2  G3  B3

You probably won't need to remake the chords. If you do, remember that the CPX can only play 16-bit mono 16 kHz WAV files.
