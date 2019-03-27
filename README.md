# Vinbot
This respository is my project to play with Raspberry Pi, few sensors and AI to create some interesting things

# Disclaimer
- I am not a programmer by education or experience. 
- Most codes are copied from other resources in github and / or other internet sites
- I give due credits to all from whom I have copied or 'taken inspiration' from. In case I missed any point, please let me know and I will correct them
- I am a newbie to coding as well as using github. Any critisicm / comments / suggestions are most welcome

# High level user stories
## Basic hardware integration
- Integration of Raspberry Pi with hc-sr04 (ultrasonic sensor), pi-camera, L298n (DC motor controller), DC motors

## Basic rover control using keyboard inputs
- control 4 DC motors using python

## Distance measurement using hc-sr04
- write program to measure distance using ultrasonic sensor

## Integrate distance measurement to control rover autonomously
- As a user, I want the rover to detect objects using ultrasonic sensor, so that the rover can stop and avoid hitting the object
- As a user, I want the rover to take corrective actions after detecting an object, so that the rover can navigate a new path without obstacles... This will be one step towards autonomous driving

## Using pi-camera and viewing feeds online
- As a user, I want the rover to be able to take in feed from the pi-camera and share it over the internet so that I can see exactly what the rover camera sees

## Machine learning to injest images from the video feed
- As a user, I want a machine learning (ML) algorithm which can injest the picamera images so that it can process it to identify objects in its path... Object classification
- As a user, I want ML to give command to the DC Motor controller on changing directions et al so the rover can manouever itself around the house

## ML and ultrasonic sensor
- Use both ML as well as ultrasnoci sensor feeds to control the DC motors

# Hardware
- Raspberry Pi 3 B+
- Pi camera
- resistors 1k and 3k
- L298n controller
- hc-sr04 ultrasonic sensor
- 4 x DC motors
- Breadboard
- jumper cables
- power source for DC motors
- power source for Raspberry Pi