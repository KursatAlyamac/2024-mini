"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import network
import urequests

N: int = 10
sample_ms = 10.0
on_ms = 500

SSID = 'wifi-name'
PASSWORD = 'wifi-password'

FIREBASE_URL = '<firebase-url>/<table-name>.json'

def connect_wifi(ssid: str, password: str) -> None:
    """Connects to the Wi-Fi network."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    max_wait = 15
    while max_wait > 0:
        if wlan.isconnected():
            break
        print('Waiting for connection...')
        time.sleep(1)
        max_wait -= 1
    if wlan.isconnected():
        print('Connected to Wi-Fi')
        print('Network config:', wlan.ifconfig())
    else:
        print('Failed to connect to Wi-Fi')
        raise RuntimeError('Wi-Fi connection failed')

def random_time_interval(tmin: float, tmax: float) -> float:
    """Returns a random time interval between tmin and tmax."""
    return random.uniform(tmin, tmax)

def blinker(N: int, led: Pin) -> None:
    """Blinks the LED N times to signal start or end of the game."""
    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)

def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file."""
    with open(json_filename, "w") as f:
        json.dump(data, f)

def scorer(t: list[int | None]) -> None:
    """Calculates and prints the response time statistics, uploads data to Firebase."""
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]
    print("Response times:", t_good)

    if t_good:
        avg_time = sum(t_good) / len(t_good)
        min_time = min(t_good)
        max_time = max(t_good)
    else:
        avg_time = min_time = max_time = 0

    print(f"Average response time: {avg_time} ms")
    print(f"Minimum response time: {min_time} ms")
    print(f"Maximum response time: {max_time} ms")

    data = {
        "misses": misses,
        "total_flashes": len(t),
        "avg_response_time": avg_time,
        "min_response_time": min_time,
        "max_response_time": max_time,
        "score": (len(t_good) / len(t)) if len(t) > 0 else 0
    }

    now: tuple[int] = time.localtime()
    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"
    print("Writing to", filename)
    write_json(filename, data)

    try:
        print("Uploading data to Firebase...")
        response = urequests.post(FIREBASE_URL, json=data)
        print('Data sent to Firebase, response:', response.text)
        response.close()
    except Exception as e:
        print("Failed to upload data to Firebase:", e)

if __name__ == "__main__":
    # Connect to Wi-Fi
    try:
        connect_wifi(SSID, PASSWORD)
    except RuntimeError as e:
        print(e)

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    # start of game
    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    # end of game
    blinker(5, led)

    scorer(t)
