import time

seconds = time.time()
print('Seconds since epoch =%f' %seconds)
loc_time = time.ctime(seconds)
print('Local time: %s' %loc_time)
time.sleep(10)
print('This is printed after 10 seconds')
seconds1 = time.time()
loc_time1 = time.ctime(seconds1)
print('Local time after 10 seconds: %s' %loc_time1)
