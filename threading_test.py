import threading
import time

def cook(dish):
    time.sleep(2)
    print(f"Finished cooking {dish}.")

def listen():
    time.sleep(8)
    print("Finished listening to music.")

def eat():
    time.sleep(6)
    print("Finished eating.")

# .start() -> Create new thread
# .join() -> Execute the thread before main thread
# .is_alive() -> Check if the thread is alive/running
# daemon -> will stop when the main thread stops

t1 = threading.Thread(target=cook, args=("Pasta",), daemon=True) # if we remove `,` there is no longer tuple, instead we're passing a string
t1.start()

t2 = threading.Thread(target=listen)
t2.start()

t3 = threading.Thread(target=eat)
t3.start()

t1.join()
t2.join()
t3.join()

print("All chores are completed")