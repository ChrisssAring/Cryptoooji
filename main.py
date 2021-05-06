from bitcoin import *
import time
import threading
import btclog

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def run():

    print("{} started!".format(name))

    while True:

        priv = random_key()

        pub = privtopub(priv)

        addr = pubtoaddr(pub)

        log_message = "private:{},address:{}".format(
            priv, addr)

        btclog.log(log_message)

        if BinarySearch(mylist, addr) > 0:
            print("BTC FOUND!", priv, addr)
            f = open("btc_found.txt", "a")
            f.write(log_message + "\n")
            f.close()
            passwords_raw.close()


if __name__ == '__main__':

    num_threads = 12

    btclog = btclog.BtcLog()

    time0 = time.perf_counter()

    with open('btc_latest_cleaned.txt') as f:
        mylist = [line.rstrip('\n') for line in f]

    time1 = time.perf_counter()
    print(f"Converted file to list in {time1 - time0:0.4f} seconds")
    mylist.sort()
    time2 = time.perf_counter()
    print(f"Sorted list in {time2 - time1:0.4f} seconds")

    for x in range(num_threads):
        thread_name = "Thread-{}".format(x + 1)
        mythread = threading.Thread(target=run, args=(thread_name,))
        mythread.start()
