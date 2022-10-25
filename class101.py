
import time
#Define the countdown function
def countdown_timer(secs):
    while secs > 0 :
        mins = int(secs/60)
        seconds = int (secs%60)
        timer = f'{mins}:{seconds}'
        print(timer)
        secs = secs-1
#Take a input
second = input("Enter the time in nuber of seconds")
#calling function
countdown_timer(int(second))