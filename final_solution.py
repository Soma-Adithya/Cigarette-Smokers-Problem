"""
B V SOMA ADITHYA
CIGARETTE SMOKERS PROBLEM 
"""

import random
import threading
import time

#Thread running
active_thread = None

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

    global tobacco, paper, matches, agent, mutex_lock, active_thread
    while True:
    
        # instead of selecting 2, we select 1 that shouldn't be included.
        flag = random.randint(1, 3)
        if flag != 1:
            print("Tobacco is selected")
            tobacco.release()# tobacco is available
        if flag != 2:
            print("Paper is selected")
            paper.release()#paper is available
        if flag != 3:
            print("Matches is selected")
            matches.release()#matches is available
            
        print(f"Process number '{flag}' will access Critical Section ")
    
        # Here any 2 of them will not be equal, their respective ingredients are added to the table.
        if flag == 1:
            agent.acquire()  # agent sleeps.
            mutex_lock.acquire()#To release we need to aquire else we get RuntimeError
            mutex_lock.release()  # lock opens
            #fun_tobacco()
            active_thread = threading.Thread(target=fun_tobacco, name="Tobacco Smoker")
            #tobacco_smoker_thread.start()
          
        elif flag == 2:
            agent.acquire()  # agent sleeps.
            mutex_lock.acquire()
            mutex_lock.release()  # lock opens
            #fun_paper()
            active_thread = threading.Thread(target=fun_paper, name="Paper Smoker")
            #paper_smoker_thread.start()
            
        elif flag == 3:
            agent.acquire()  # agent sleeps.
            mutex_lock.acquire()
            mutex_lock.release()  # lock opens
            #fun_matches()
            active_thread = threading.Thread(target=fun_matches, name="Matches Smoker")
            #matches_smoker_thread.start()
        
        else:
            print("ERROR")
            
        active_thread.start()  
        active_thread.join()
        print("    ")
        agent.release()
           
       
def fun_tobacco():
   
    mutex_lock.acquire()  # Block until the lock is acquired
    #CS Starts
    print("Tobacco smoker is smoking...")
    time.sleep(2)
    print("Finished smoking")
    #CS Ends
    mutex_lock.release()
        
    
def fun_paper():
      
    mutex_lock.acquire()  # Block until the lock is acquired
    #CS Starts
    print("Paper smoker is smoking...")
    time.sleep(2)
    print("Finished smoking")
    #CS Ends
    mutex_lock.release()
        

def fun_matches():
    
    mutex_lock.acquire()  # Block until the lock is acquired
    #CS Starts
    print("Matches smoker is smoking...")
    time.sleep(2)
    print("Finished smoking")
    #CS Ends
    mutex_lock.release()
       


# Agent Thread
agent_thread = threading.Thread(target=fun_agent, name="Agent")

# Start the thread
agent_thread.start()

# Wait for all threads to finish
agent_thread.join()


"""
Deadlock satisfied that is:
1) Mutex is satisfied
2)No Hold and wait
3)No preemption
4)No circular wait.
"""











