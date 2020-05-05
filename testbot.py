from maplebot import MapleChar
import pyautogui
import sys
import random
import time
import logging

"""
Author: Kevin Lee (me@mngyuan.com)

TestBot
"""

# for retina / hidpi screens
SCALE = 2
clickf = lambda pt: pyautogui.click(pt[0] / SCALE, pt[1] / SCALE)


class TestBot(MapleChar):
    """Test some keys"""

    def __init__(self):
        super().__init__()
        logging.basicConfig(
            filename="maplebot.log",
            filemode="w",
            format="%(asctime)s.%(msecs).03d : %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S",
            level=logging.INFO,
        )
        logging.info("-" * 75)
        logging.info(" " * 25 + "Start of TestBot Run")
        logging.info("-" * 75)


def main():
    test_bot = TestBot()
    test_keys = [
        test_bot.TILDE,
        test_bot.ONE,
        test_bot.ZERO,
        test_bot.Q,
        test_bot.P,
        test_bot.A,
        test_bot.L,
        test_bot.Z,
        test_bot.M,
    ]
    for key in test_keys:
        clickf(key)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
