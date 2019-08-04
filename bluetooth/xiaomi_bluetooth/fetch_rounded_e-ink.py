#!/usr/bin/env python3

import logging
import sys

from bluepy import btle

from xiaomi_bluetooth.common import setup_logging, connect_for_getting_values, int_from_bytes

# BASED ON: https://4pda.ru/forum/index.php?showtopic=927171&st=1140#entry86324805

_logger = logging.getLogger('rounded')


class Delegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        temperature_bytes = data[2:4]
        humidity_bytes = data[4:]

        humidity = int_from_bytes(humidity_bytes) / 10.0
        temperature = int_from_bytes(temperature_bytes) / 10.0

        _logger.debug('temperature: {}°C\trel_humidity: {}%'.format(temperature, humidity))


def main():
    setup_logging()
    device_mac = sys.argv[1]

    with connect_for_getting_values(device_mac, '00000100-0000-1000-8000-00805f9b34fb', Delegate()) as p:
        for index in range(5):
            _logger.debug('#{} {}'.format(index, p.waitForNotifications(timeout=5.0)))


if __name__ == '__main__':
    main()
