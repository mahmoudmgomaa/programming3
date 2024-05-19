# multi Threading
import time

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)


print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
##################################################################
import time
import threading

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join
#######################################################################################
# A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks.
# The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool.

# Simple example

import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
##########################################################################
#Race Condition Problem

import threading

# global variable x
x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task():
	"""
	task for thread
	calls increment function 1000 times.
	"""
	for _ in range(100000):
		increment()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating threads
	t1 = threading.Thread(target=thread_task)
	t2 = threading.Thread(target=thread_task)

	# start threads
	t1.start()
	t2.start()














