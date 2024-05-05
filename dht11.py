import Adafruit_DHT
import time
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

sensor = Adafruit_DHT.DHT11

#GPIO18
gpio_dht11 = 18

def main():
    humidity_latest = 0
    temp_latest = 0
    while True:
        #store readings in tuple
        humidity, temp = Adafruit_DHT.read_retry(sensor, gpio_dht11)
        
        if (humidity != humidity_latest) or (temp != temp_latest):
            humidity_latest = humidity
            temp_latest = temp
            #print('Temp={0:0.1f}°C, Humidity={1:0.1f}%'.format(temp, humidity))
            logging.info('Temp={0:0.1f}°C, Humidity={1:0.1f}%'.format(temp, humidity))
        elif (humidity == humidity_latest) and (temp == temp_latest):
            pass
        else:
            #print('Failed to get reading. Try again')
            logging.error('Reading not updated. Try again')
    
if __name__ == '__main__':
    main()
