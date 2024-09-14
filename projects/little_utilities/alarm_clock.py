import pygame
import time
import datetime
import os

def set_alarm(alarm_time):
    print("Alarm set for ", alarm_time)
    sound_file = "alarm.mp3"

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time: ", current_time)

        if current_time == alarm_time:
            print("Time to wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            break
        
        time.sleep(1)

if __name__ == "__main__":  
    sound_file = "alarm.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    # alarm_time = input("Enter the time for the alarm (HH:MM:SS): ")
    # set_alarm(alarm_time)