#!/usr/bin/env python
import unicornhat, signal
pixels = [[(255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (0, 158, 158), (255, 255, 30)],
          [(0, 158, 158), (255, 255, 30), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30)],
          [(255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (0, 158, 158), (255, 255, 30), (255, 255, 30), (255, 255, 30), (255, 255, 30), (0, 158, 158), (0, 158, 158)],
          [(0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (255, 255, 30), (0, 158, 158)],
          [(255, 255, 30), (0, 158, 158), (0, 158, 158), (0, 158, 158), (255, 255, 30), (0, 158, 158), (0, 158, 158), (255, 255, 30)]]
unicornhat.set_pixels(pixels)
unicornhat.show()
signal.pause()
