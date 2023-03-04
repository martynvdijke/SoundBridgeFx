import logging
import threading
import time
import argparse

from soundbridgefx import (
    ffmpeg,
    ledfx,
    raspotify,
    web_backend
)

def setup_logging(loglevel):
    console_loglevel = loglevel or logging.WARNING
    console_logformat = "[%(levelname)-8s] %(name)-30s : %(message)s"

    root_logger = logging.getLogger()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_loglevel)  # set loglevel
    console_formatter = logging.Formatter(
        console_logformat
    )  # a simple console format
    console_handler.setFormatter(
        console_formatter
    )  # tell the console_handler to use this format

    # add the handlers to the root logger
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)

    # Suppress some of the overly verbose logs
    logging.getLogger("sacn").setLevel(logging.WARNING)
    logging.getLogger("aiohttp.access").setLevel(logging.WARNING)
    logging.getLogger("pyupdater").setLevel(logging.WARNING)
    logging.getLogger("zeroconf").setLevel(logging.WARNING)

    global _LOGGER
    _LOGGER = logging.getLogger(__name__)


def main():
    # args = parse_args()
    # setup_logging(args.loglevel)

    ledfx_thread = threading.Thread(
        target=ledfx.main(), args=(1,), daemon=True)
    ledfx_thread.start()


    ffmpeg_thread = threading.Thread(
        target=ffmpeg.main(), args=(1,), daemon=True)
    ffmpeg_thread.start()

    # raspotify_thread = threading.Thread(
    #     target=raspotify.main(), args=(1,), daemon=True)
    # raspotify_thread.start()

    backend_thread = threading.Thread(target=web_backend.main(), args=(1,))
    backend_thread.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        ffmpeg_thread.join()
        # ledfx_thread.join()
        # raspotify_thread.join()
        backend_thread.join()