# flyweight
class fly:
    cars = {}
    def __new__(obj , id):
        try:
            obj= fly.cars[id]
        except:
            fly.cars[id]= obj
    def __int__(self, id):
        self.id = id
 list= [("a",1),("a",2),("a",1)]
for i in list:
    obj = fly(i[1])
    print(fly.cars)
############################################################
#design pattern facade
 #complex subsystems
 class Subsystem A:
     def operation_a(self):
         print("Subsystem A:Operation A")
 class Subsystem B:
     def operation_b(self):
         print("Subsystem B: Operaion B")
#FACADE
class facade:
    def __int__(self):
        self.subsystem_a = subsystemA()
        self.subsystem_b = subsystemB ()
    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        facade= Facade()
        facade = operation()
##################################################################################
# design pattern singleton
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton , cls).__new__(cls)
            return cls._instance
Singleton_instance1 = Singleton()
Singleton_instance2 = Singleton()
print(Singleton_instance1 is Singleton_instance2)
#######################################################################################
# timer decorator module
import functools
import time

# ...

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer
####################################################################
# debug decorator module
import functools



def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  #create list of args
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()] #create list of kargs
        signature = ", ".join(args_repr + kwargs_repr) #create function signature
        print(f"Calling {func.__name__}({signature})") #print signature
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}") #print the return value
        return value
    return wrapper_debug
