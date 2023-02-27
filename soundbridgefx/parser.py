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