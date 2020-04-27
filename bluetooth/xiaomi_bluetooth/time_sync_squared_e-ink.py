#!/usr/bin/env python3

import logging
import sys
from datetime import datetime

from lywsd02 import Lywsd02Client

from xiaomi_bluetooth.common import setup_logging

_logger = logging.getLogger('time_sync_squared')


def main():
    setup_logging()
    device_mac = sys.argv[1]

    with Lywsd02Client(device_mac).connect() as client:
        logging.info('sync time')
        client.time = datetime.now()

        logging.info('check sync result')
        print(client.time)


if __name__ == '__main__':
    main()
