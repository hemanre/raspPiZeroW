import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

#GPIO18
gpio_dht11 = 18

while True:
    #store readings in tuple
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio_dht11)
    
    if humidity is not None and temp is not None:
        print('Temp={0:0.1f}°C, Humidity={1:0.1f}%'.format(temp, humidity))
    else:
        print('Failed to get reading. Try again')
    
    time.sleep(2)
