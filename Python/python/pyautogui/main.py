import pyautogui as pg
import time

print("Staring in 5 seconds...")
time.sleep(5)

for i in range(10):
    pg.write("ayuda con mi tarea")
    pg.press("Enter")