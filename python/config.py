#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
try:
    import RPi.GPIO as GPIO
    USE_GPIO = True
except ImportError:
    USE_GPIO = False

Temp = '0123456789ABCDEF*'
SERIAL = "/dev/ttyUSB0"

class config(object):
    FORCE  = 17
    STANDBY= 4
    def __init__(ser, Baudrate = 9600):
        ser.serial = serial.Serial(SERIAL,Baudrate)
        if USE_GPIO:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ser.FORCE, GPIO.IN)
            GPIO.setup(ser.STANDBY, GPIO.OUT)
            GPIO.output(ser.STANDBY, GPIO.HIGH)
        
    def Uart_SendByte(ser, value): 
        ser.serial.write(value.encode()) 
        
    def Uart_SendString(ser, value): 
        ser.serial.write(value.encode())
  

    def Uart_ReceiveByte(ser): 
        return ser.serial.read(1)

    def Uart_ReceiveString(ser, value): 
        data = ser.serial.read(value)
        return data.decode()
        
    def Uart_Set_Baudrate(ser, Baudrate):
         ser.serial = serial.Serial(SERIAL,Baudrate)

    
    
    