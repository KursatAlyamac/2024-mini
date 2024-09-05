#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

def rest(duration: float) -> None:
    """Function to add a rest for the specified duration"""
    quiet()
    utime.sleep(duration)

notes = [
    493.88,  #B4
    440.00,  #A4
    415.3,  #G#4
    440.00,  #A4
    523.25, #C5
    None,
    587.30, #D5
    523.25,
    493.88,
    523.25,
    659.2, #E5
    None,
    698.4, #F5
    659.2,
    622.2, #D#5
    659.2,
    987.7, #B5
    880, #A5
    830.6, #A#5
    880,
    987.7,
    880,
    830.6,
    880,
    1046.5, #A6
    
]

# Durations for each note (in seconds)
durations = [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2,0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.4]  # Adjust for rhythm

# Play the Turkish March
for i, note in enumerate(notes):
    if note is not None:
        playtone(note, durations[i])
        quiet()  
        utime.sleep(0.1)
    else:
        rest(durations[i]) # Add a rest where note is None

# Turn off the PWM
quiet()
