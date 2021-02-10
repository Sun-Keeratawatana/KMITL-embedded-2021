import threading
sem = threading.Semaphore()
def sem1():
    sem.acquire()
    print("sem1 acquired")
    for i in range(5):
        print("sem1: {} by pid {}".format(i, threading.get_ident()))
    sem.release()
    print("sem1 released\n")

def sem2():
    while(sem.acquire()):
        print("sem2 acquired")
        for i in range(5):
            print("sem2: {} by pid {}".format(i, threading.get_ident()))
    sem.release()

t1 = threading.Thread(target = sem1)
t2 = threading.Thread(target = sem2)
t1.start()
t2.start()
