#import need libraries
import pyautogui
from os import chdir,path
#change path
chdir(path.join(path.expanduser("~"),'Desktop'))
#do screen
instance=pyautogui.screenshot()
#save photo
instance.save("screenshotPython.png")
print ("this is screen by python")