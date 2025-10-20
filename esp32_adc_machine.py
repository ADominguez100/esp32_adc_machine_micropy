#Write a Micropython script to read the analog data provided by POT connected  to GPIO34 and print on shell every o.1 sec
from machine import Pin, ADC
from time import sleep
POT = ADC(Pin(34))

POT.atten(ADC.ATTN_11DB)#Specifying the voltage of the  Analog sensor
while True:
    pot_value  = POT.read()
    print("Valor mostrat:", pot_value) #Text afegit al print
    sleep(0.1)