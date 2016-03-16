#!/usr/bin/python

import cwiid
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# pinouts subjectto change, make it easier here

LED1 = 17
LED2 = 18

#initialize LEDs
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)

button_dellay = 0.1

# Start a connecton to the Wiimote.  Most places say to use button 1 + 2, but I found that I need to use the little button on the back by the battery

print "Press the sync button on your remote now ..."
wm = None
i=2

while not wm:
  try:
    wm=cwiid.Wiimote()
  except RuntimeError:
    if (i>10):
      quit()
      break
    print "Error opening wiimote connecton"
    print "attempt " + str(i)
    i += 1
    
print "Conmnected to the Wiimote!\n\n"

# set up Wiimote reporting
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

#turn on led to show connected 
wm.led = 1
GPIO.output(LED1,1)

while True:

  # Display Accelerometer state.  
  print(wm.state['acc'])

  button = wm.state['buttons']
    # If Plus and Minus buttons pressed together then rumble and quit.
  if (button - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wm.rumble = 1
    time.sleep(1)
    wm.rumble = 0
    exit(wm)
    
    if (button & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)         
    

  if(button & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)          
    

  if (button & cwiid.BTN_UP):
    print 'Up pressed'        
    time.sleep(button_delay)          

  if (button & cwiid.BTN_DOWN):
    print 'Down pressed'      
    time.sleep(button_delay)  

  if (button & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  if (button & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  if (button & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          
    
  if (button & cwiid.BTN_B):
    print 'Button B pressed'
    

  if (button & cwiid.BTN_HOME):
    print 'Home Button pressed'
    
    
  if (button & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
       
    
  if (button & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)


  
