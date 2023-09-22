import threading
import time
from soundbridgefx.sonos.controller import SonosController

def main():
    controller = SonosController()

    # args = parse_args()
    # setup_logging(args.loglevel)

    # ledfx_thread = threading.Thread(target=ledfx.main(), args=(1,), daemon=True)
    # ledfx_thread.start()

    # ffmpeg_thread = threading.Thread(target=ffmpeg.main(), args=(1,), daemon=True)
    # ffmpeg_thread.start()

    # # raspotify_thread = threading.Thread(
    # #     target=raspotify.main(), args=(1,), daemon=True)
    # # raspotify_thread.start()

    # backend_thread = threading.Thread(target=web_backend.main(), args=(1,))
    # backend_thread.start()

    # try:
    #     while True:
    #         time.sleep(2)
    # except KeyboardInterrupt:
    #     ffmpeg_thread.join()
    #     # ledfx_thread.join()
    #     # raspotify_thread.join()
    #     backend_thread.join()
