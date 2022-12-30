
from ledfx import __main__

def main():
    try:
        __main__.main()
    except: 
        _LOGGER.error("Could not start ledfx")