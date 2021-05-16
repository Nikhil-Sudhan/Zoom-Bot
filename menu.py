import subprocess
import pyautogui
import time 
import pandas as pd 
from datetime import datetime



def sing_in(meetingid,pswd):

    subprocess.call(['C:\\Users\\Payload\\Desktop\\zoom\\ZoomInstaller.exe'])
    time.sleep(20)

    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button1.png')
    print(join_btn) 
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #type meeting id
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button2.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.write(meetingid)

    #disable both the camera and mic
    media_btn = pyautogui.locateAllOnScreen('button.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    #hits the join button
    join_btn=pyautogui.locateCenterOnScreen('getin_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #types the password
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pass2.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    time.sleep(10)
    pyautogui.write(pswd)
    time.sleep(10)

    #hits the last join buton
    join_btn=pyautogui.locateCenterOnScreen('join_last.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

#Reading the cvs file
df=pd.read_csv('timing.csv')

while True:
    #checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timing']):

        row = df.loc[df['timing']== now]
        m_id = str(row.iloc[0,1])
        m_pass = str(row.iloc[0,2])

        sing_in(m_id,m_pass)
        time.sleep(20)
        print('Joined')
        exit
        

    