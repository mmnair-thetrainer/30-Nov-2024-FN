import threading
import time

def my_thread(thread_name, thread_delay):
    count = 0
    while count < 5:
        time.sleep(thread_delay)
        count += 1
        print("Name: %s, Exec Time: %s" % (thread_name, time.ctime(time.time())))

try:
    for i in range(0,6):
        th1 = threading.Thread(target=my_thread, args=("Thread-" + str(i), 2))
        th1.start()
except:
    print("Unable to start thread.")