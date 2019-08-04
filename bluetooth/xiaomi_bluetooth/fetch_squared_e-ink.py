#!/usr/bin/env python3

import logging
import sys

from bluepy import btle

from xiaomi_bluetooth.common import setup_logging, connect_for_getting_values, int_from_bytes

# BASED ON: http://www.techort.com/how-i-took-data-from-the-ble-thermometer-from-xiaomi-habr/

_logger = logging.getLogger('squared')


class Delegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        temperature_bytes = data[:2]
        humidity_bytes = data[2]

        temperature = int_from_bytes(temperature_bytes) / 100.0
        humidity = humidity_bytes

        _logger.debug('temperature: {}°C\trel_humidity: {}%'.format(temperature, humidity))


def main():
    setup_logging()
    device_mac = sys.argv[1]

    with connect_for_getting_values(device_mac, 'ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6', Delegate()) as p:
        for index in range(5):
            _logger.debug('#{} {}'.format(index, p.waitForNotifications(timeout=5.0)))


if __name__ == '__main__':
    main()
