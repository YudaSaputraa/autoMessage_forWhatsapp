import pywhatkit
import pyautogui
import time

phoneNumber = ["+6287861009087", "+6285158911402"]
message = "Presensi duluu [automatic Message with python]"
hour = 12
minute = 29
pywhatkit.sendwhatmsg(phoneNumber[1], message, hour, minute)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')
