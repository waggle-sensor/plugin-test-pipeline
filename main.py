import argparse
import logging
from random import random
import time
from waggle.plugin import Plugin


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debug logs")
    parser.add_argument("--rate", default=300.0, type=float, help="sampling rate")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    with Plugin() as plugin:
        while True:
            logging.info("publishing random measurement")
            plugin.publish("test", 25.0 + 5 * random())

            logging.info("uploading test image file")
            plugin.upload_file("test.jpg", keep=True)

            time.sleep(args.rate)


if __name__ == "__main__":
    main()
