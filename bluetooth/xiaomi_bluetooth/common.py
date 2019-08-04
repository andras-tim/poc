import logging
from contextlib import contextmanager

from bluepy import btle

_logger = logging.getLogger('common')


def int_from_bytes(bites) -> int:
    return int.from_bytes(bites, byteorder='little')


def int_to_bytes(value: int):
    return value.to_bytes(2, byteorder="little")


def _write_descriptor(characteristic, uuid, value):
    descriptor = characteristic.getDescriptors(forUUID=uuid)[0]
    descriptor.write(value, withResponse=True)


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-7s [%(name)s] %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )


@contextmanager
def bluetooth_connect(device_mac: str):
    _logger.debug('Connecting to... {}'.format(device_mac))
    with btle.Peripheral(deviceAddr=device_mac) as p:
        _logger.debug('Connected')

        yield p


@contextmanager
def connect_for_getting_values(device_mac: str, characteristic_uuid: str, delegate: btle.DefaultDelegate):
    with bluetooth_connect(device_mac) as p:
        _logger.debug('Configuring delegator... {!r}'.format(delegate))
        p.withDelegate(delegate)

        _logger.debug('Getting characteristic... {}'.format(characteristic_uuid))
        ch = p.getCharacteristics(uuid=characteristic_uuid)[0]

        _logger.debug('Setting up scientific typing...')
        # The value of the byte that needs to be sent was found by scientific typing
        _write_descriptor(ch, 0x2902, int_to_bytes(1))

        yield p
