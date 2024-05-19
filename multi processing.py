import time
import multiprocessing


def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n * n))
        time.sleep(3)


def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n * n * n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2, 3, 8]

    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done in : ", time.time() - t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count())
    #####################################################################################################
    import multiprocessing
    import os


    def worker1():
        # printing process id
        print("ID of process running worker1: {}".format(os.getpid()))


    def worker2():
        # printing process id
        print("ID of process running worker2: {}".format(os.getpid()))


    if __name__ == "__main__":
        # printing main program process id
        print("ID of main process: {}".format(os.getpid()))

        # creating processes
        p1 = multiprocessing.Process(target=worker1)
        p2 = multiprocessing.Process(target=worker2)

        # starting processes
        p1.start()
        p2.start()

        # process IDs
        print("ID of process p1: {}".format(p1.pid))
        print("ID of process p2: {}".format(p2.pid))

        # wait until processes are finished
        p1.join()
        p2.join()

        # both processes finished
        print("Both processes finished execution!")

        # check if processes are alive
        print("Process p1 is alive: {}".format(p1.is_alive()))
        print("Process p2 is alive: {}".format(p2.is_alive()))
########################################################################################
    # This example demonstrate shared data space by different processes(problem)

    import multiprocessing

    # empty list with global scope
    result = []


    def square_list(mylist):
        """
        function to square a given list
        """
        global result
        # append squares of mylist to global list result
        for num in mylist:
            result.append(num * num)
        # print global list result
        print("Result(in process p1): {}".format(result))


    if __name__ == "__main__":
        # input list
        mylist = [1, 2, 3, 4]

        # creating new process
        p1 = multiprocessing.Process(target=square_list, args=(mylist,))
        # starting process
        p1.start()
        # wait until process is finished
        p1.join()

        # print global result list
        print("Result(in main program): {}".format(result))
##############################################################################################
 #This example demonstrate communications between processes



# Queue Example

import multiprocessing

def square_list(mylist, q):
	"""
	function to square a given list
	"""
	# append squares of mylist to queue
	for num in mylist:
		q.put(num * num)

def print_queue(q):
	"""
	function to print queue elements
	"""
	print("Queue elements:")
	while not q.empty():
		print(q.get())
	print("Queue is now empty!")

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating multiprocessing Queue
	q = multiprocessing.Queue()

	# creating new processes
	p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
	p2 = multiprocessing.Process(target=print_queue, args=(q,))

	# running process p1 to square list
	p1.start()
	p1.join()

	# running process p2 to get queue elements
	p2.start()
	p2.join()

