import logging
import threading
import time
import argparse

from soundbridgefx import (
    backend,
    ledfx,
    cvlc,
    raspotify
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


def parse_args():
    parser = argparse.ArgumentParser(
        description="A Networked LED Effect Controller"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"soundbridgefx ",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "-lp",
        "--lport",
        dest="port",
        help="LedFx Web interface port (HTTP)",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-lp_s",
        "--lport_secure",
        dest="port_s",
        help="LedFX Web interface port (HTTPS)",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-sp",
        "--sport",
        dest="port",
        help="SoundBridgeFx Web interface port (HTTP)",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-sp_s",
        "--sport_secure",
        dest="port_s",
        help="SoundBridgeFx Web interface port (HTTPS)",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-mp",
        "--mport",
        dest="port",
        help="Stream port (HTTP)",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-mp_s",
        "--mport_secure",
        dest="port_s",
        help="Stream port (HTTPS)",
        default=None,
        type=int,
    )

    return parser.parse_args()

def main():
    args = parse_args()
    setup_logging(args.loglevel)

    # ledfx_thread = threading.Thread(
    #     target=ledfx.main(), args=(1,), daemon=True)
    # ledfx_thread.start()


    # cvlc_thread = threading.Thread(
    #     target=CVLC.main, args=(1,), daemon=True)
    # cvlc_thread.start()

    # raspotify_thread = threading.Thread(
    #     target=raspotify.main(), args=(1,), daemon=True)
    # raspotify_thread.start()

    backend_thread = threading.Thread(target=backend.main(), args=(1,))
    backend_thread.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        # ledfx_thread.join()
        # raspotify_thread.join()
        backend_thread.join()