#!/usr/bin/env python3

import logging
import sys

from xiaomi_bluetooth.common import setup_logging, bluetooth_connect

# BASED ON: http://www.techort.com/how-i-took-data-from-the-ble-thermometer-from-xiaomi-habr/

_logger = logging.getLogger('discovery')


def main():
    setup_logging()
    device_mac = sys.argv[1]

    with bluetooth_connect(device_mac) as p:
        _logger.debug('Getting services...')
        for s in p.getServices():

            _logger.debug('Getting characteristics of service {}...'.format(s.uuid))
            for c in s.getCharacteristics():
                _logger.info('\tCharacteristic {} info:'.format(c.uuid))
                _logger.info('\t\thandle        : {}'.format(c.getHandle()))
                _logger.info('\t\tproperties    : {}'.format(c.propertiesToString().strip().replace(' ', ', ')))

                if c.supportsRead():
                    data = c.read()
                    _logger.info('\t\tread_raw_data : {}'.format(data))
                    _logger.info('\t\tread_bytes    : {}'.format([i for i in data]))


if __name__ == '__main__':
    main()
