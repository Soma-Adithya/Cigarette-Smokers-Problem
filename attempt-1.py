import random
import threading
import time

# Agent is ready to execute
# There are no ingredients on the table (buffer)
agent = threading.Semaphore(1)
tobacco = threading.Semaphore(0)
paper = threading.Semaphore(0)
matches = threading.Semaphore(0)
# Initially, the lock is closed (we assume)
mutex_lock = threading.Lock()

# AGENT FUNCTION
def fun_agent():

    global tobacco, paper, matches, agent, mutex_lock
    
    # instead of selecting 2, we select 1 that shouldn't be included.
    flag = random.randint(1, 3)
    if flag != 1:
        tobacco.release()# tobacco is available
    if flag != 2:
        paper.release()#paper is available
    if flag != 3:
        matches.release()#matches is available
    
    # Here any 2 of them will not be equal, their respective ingredients are added to the table.
    if flag == 1:
        agent.acquire()  # agent sleeps.
        mutex_lock.release()  # lock opens
        fun_tobacco()
    elif flag == 2:
        agent.acquire()  # agent sleeps.
        mutex_lock.release()  # lock opens
        fun_paper()
    elif flag == 3:
        agent.acquire()  # agent sleeps.
        mutex_lock.release()  # lock opens
        fun_matches()


def fun_tobacco():
    while mutex_lock.acquire(blocking=False):  # Keep trying to acquire the lock
    #if we aquire lock we exit the loop
    #blocking parameter allows us to stay in loop until we aquire lock
    	#pass
    #CS Starts
    print("Tobacco smoker is smoking...")
    time.sleep(2)
    print("Finished")
    #CS Ends
    mutex_lock.release()
    

def fun_paper():
    while mutex_lock.acquire(blocking=False):  # Keep trying to acquire the lock
    #if we aquire lock we exit the loop
    #blocking parameter allows us to stay in loop until we aquire lock
    	#pass
    #CS Starts
    print("Paper smoker is smoking...")
    time.sleep(2)
    print("Finished")
    #CS Ends
    mutex_lock.release()

def fun_matches():
    while mutex_lock.acquire(blocking=False):  # Keep trying to acquire the lock
    #if we aquire lock we exit the loop
    #blocking parameter allows us to stay in loop until we aquire lock
    	#pass
    #CS Starts
    print("Matches smoker is smoking...")
    time.sleep(2)
    print("Finished")
    #CS Ends
    mutex_lock.release()


# Threads
agent_thread = threading.Thread(target=fun_agent, name="Agent")
tobacco_smoker_thread = threading.Thread(target=fun_tobacco, name="Tobacco Smoker")
paper_smoker_thread = threading.Thread(target=fun_paper, name="Paper Smoker")
matches_smoker_thread = threading.Thread(target=fun_matches, name="Matches Smoker")


# Start the threads
agent_thread.start()
tobacco_smoker_thread.start()
paper_smoker_thread.start()
matches_smoker_thread.start()

# Wait for all threads to finish
agent_thread.join()
tobacco_smoker_thread.join()
paper_smoker_thread.join()
matches_smoker_thread.join()




