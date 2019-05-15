import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522



reader = SimpleMFRC522()

try:
	print('Please Scan your Licence.....')

	id, text = reader.read()
	print(text)

finally:

	GPIO.cleanup()
