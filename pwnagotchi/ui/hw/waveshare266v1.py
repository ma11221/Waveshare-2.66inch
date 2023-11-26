import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class waveshare266v1(DisplayImpl):
    def __init__(self, config):
        super(waveshare266v1, self).__init__(config, 'waveshare266v1')
        self._display = None

    def layout(self):
        fonts.setup(10, 8, 10, 35, 25, 9)
        self._layout['width'] = 296
        self._layout['height'] = 152
        self._layout['face'] = (0, 48)
        self._layout['name'] = (5, 20)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (34, 0)
        self._layout['uptime'] = (220, 0)
        self._layout['line1'] = [0, 16, 296, 16]
        self._layout['line2'] = [0, 138, 296, 138]
        self._layout['friend_face'] = (0, 116)
        self._layout['friend_name'] = (48, 116)
        self._layout['shakes'] = (0, 139)
        self._layout['mode'] = (266, 139)
        self._layout['status'] = {
            'pos': (133, 20),
            'font': fonts.status_font(fonts.Medium),
            'max': 30
        }

        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 2.66inch display")
        from pwnagotchi.ui.hw.libs.waveshare.waveshare266v1.epd2in66 import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear(0xFF)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.displayPartial(buf)

    def clear(self):
        #pass
        self._display.Clear(0xFF)
