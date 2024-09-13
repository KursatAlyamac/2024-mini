# Report for EC463 Mini Project

## Exercise 1

What are the "max_bright" and "min_bright" values we found?

The __min_bright__ value is stable around __52000__ in a dark environment with minimal background lumination.

The __max_bright__ value goes as low as __10000__ when the sensor is directly exposed to a phone's flashlight under the same lighting conditions.

Additional description for our results in this exercise:

The results that were attained from this experiment are as expected because the value being measured is the resistance change in the photoresistor. In bright lighting conditions, the resistance of the photoresistor decreases, which leads to a lower voltage on the ADC pin and the opposite is true for dim lighting conditions.

## Exercise 2

Our results for the PWM sound output exercise:

We successfully used Pulse Width Modulation to play the opening line of Mozart's Rondo Alla Turka from the speaker, accurate to the original in terms of note and rhythm. 

PWM is a technique for simulating an analog output with digital means, where digital signals oscillate between LOW or HIGH states. The frequency of the square waves that are subsequently generated determine the pitch of the note coming from the speaker. Higher frequencies produce higher-pitched notes, whereas lower frequencies produce lower-pitched notes. In our code, the melody can then be constructed by specifying the corresponding note frequency in Hertz (None for rests) and the duration in which the note or rest is held for. 


## Exercise 3

Our results for the response time measurement and a general description of our web app:

We successfully implemented the game_exercise.py to play the game with a tactile switch and we uploaded the data to a Firebase Realtime Database.

When we run the code on the Pico 2, the LED correctly blinks 3 times, the reaction times are correctly measured, the data is stored in a json object and pushed to Firebase. Below is the terminal output that showcases these results:

![Thonny Screenshot](https://drive.google.com/file/d/1Wz2kCcBjGjJFfkKKJFJtQnIXmwyJPyMQ/view?usp=sharing)

Below is an image showing the same data as stored in a data.json file in Firebase Realtime Database:

![Firebase Screenshot](https://drive.google.com/file/d/1W2Ej5GVwiqCOaIZXP8-H5YFteTMW3oPV/view?usp=sharing)

In order to run this code on your own Pico, make sure to fill in these variables:

```python
SSID = 'wifi-name'
PASSWORD = 'wifi-password'

FIREBASE_URL = '<firebase-url>/<table-name>.json'
```

Here is a video link to our demo: [Demo Video](https://drive.google.com/file/d/1ZNDTjlPA04u8pWXWoGdf77zs1w5ZYLES/view?usp=sharing)
