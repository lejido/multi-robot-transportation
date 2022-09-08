import serial

prt = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0JPNGI-if00-port0"

ser = serial.Serial(prt) 
ser.timeout = 1.0
ser.flushInput() 

while 1:
  print("in1")
  ser_bytes = ser.readline()  
  print(ser_bytes)
  print("in2")
  weight = (ser_bytes.decode())
  print("in3")
  w = weight.strip() 
  print("in4")
  print(w)
  print("out")
