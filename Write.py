import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
	text = input('Enter Driving Licence Number for new entry: ')
	print('Now place your Licence to write......')
	reader.write(text)
	print('Data Successfully Written....')

finally:
	GPIO.cleanup()
