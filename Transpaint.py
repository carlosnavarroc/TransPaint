# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:07:59 2024

@author: caldostrong
"""

import os
import time
import pygetwindow as gw
import win32gui
import win32api
import win32con

# Abre MSPaint
os.system('start mspaint')

# Espera un momento para asegurarse de que MSPaint se abra
time.sleep(2)

# Encuentra la ventana de MSPaint
windows = gw.getWindowsWithTitle('Paint')
if not windows:
    print("No se encontró la ventana de MSPaint")
    exit()

paint_window = windows[0]

# Función para hacer la ventana transparente
def make_window_transparent(hwnd, alpha):
    # Establece el estilo extendido de la ventana para aceptar transparencia
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, 
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    # Establece la transparencia (alpha)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, alpha, win32con.LWA_ALPHA)

# Aplica transparencia a la ventana de MSPaint
make_window_transparent(paint_window._hWnd, 128)  # 128 es el nivel de transparencia (0-255)

print("La ventana de MSPaint es ahora transparente.")
