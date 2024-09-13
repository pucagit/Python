import threading
from time import sleep

def task1(arg):
    sleep(1)
    print("Task 1 executed with argument:", arg)

def task2(arg):
    sleep(2)
    print("Task 2 executed with argument:", arg)

def task3(arg):
    sleep(3)
    print("Task 3 executed with argument:", arg)    

t1 = threading.Thread(target=task1, args=("HAHA",))
t2 = threading.Thread(target=task2, args=("HIHI",))
t3 = threading.Thread(target=task3, args=("HOHO",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks are done!")