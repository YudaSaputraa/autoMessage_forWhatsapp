import pywhatkit
import pyautogui
import time

loc = time.localtime()
day = time.strftime('%A', loc)

phoneNumber = ["+6289623004061", "+6285158911402"]
message = day + "\n*Presensi duluu ebellll* _[automatic Message with python]_"
hour = [7, 8, 9, 10, 11, 12, 13, 14, 15]
minute = [00, 30, 15, 20]
if (day == "Monday"):
    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[0], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[3], minute[1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

if (day == "Tuesday"):
    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[2], minute[1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[5], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

if (day == "Wednesday"):
    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[1], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[5], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

if (day == "Thursday"):
    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[0], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[7], minute[1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

if (day == "Friday"):
    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[0], minute[0])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()

    print(day)
    pywhatkit.sendwhatmsg(phoneNumber[0], message, hour[2], minute[1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(50)
    pyautogui.moveTo(1250, 10, duration=4)
    pyautogui.click()
