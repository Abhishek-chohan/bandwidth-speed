import time
import psutil


def main():
    old_value = 0
    arr = []

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            a = "%0.3f" % convert_to_kbit(new_value - old_value)

            arr.append(float(a))
            send_stat(arr)
        old_value = new_value

        time.sleep(1)


def convert_to_kbit(value):
    return value / 1024. * 1


def send_stat(arr):


# print ("%0.3f" % convert_to_kbit(value) + "KBps")
    print("data used = "+ str(sum(arr)/1024) +"MB")


main()