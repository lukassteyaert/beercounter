COUNTER = 0


def print_counter():
    print "counter =", COUNTER


def increase_counter(inc=1):
   global COUNTER
   COUNTER+= inc


for i in [5,-3,7,8]:



    increase_counter(i)
    print_counter()
