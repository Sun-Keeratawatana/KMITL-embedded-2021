import threading

mutex = threading.Lock()
def Mutex(i, mutex):
    mutex.acquire()
    print("Mutex: {}".format(i))
    mutex.release()

for i in range(10):
    t = threading.Thread(target=Mutex, args=(i,mutex))
    t2 = threading.Thread(target=Mutex, args=(i,mutex))
    t3 = threading.Thread(target=Mutex, args=(i,mutex))
    t.start()
    t2.start()
    t3.start()



