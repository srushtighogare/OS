import threading
import time
import random

# Buffer size
BUFFER_SIZE = 5

# Shared buffer (queue)
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Initially, buffer has BUFFER_SIZE empty slots
full = threading.Semaphore(0)             # Initially, buffer has 0 full slots

# Mutex lock for mutual exclusion on buffer
mutex = threading.Lock()

# Producer thread
def producer(producer_id, items_to_produce=10):
    for i in range(items_to_produce):
        item = f'item-{producer_id}-{i}'
        
        empty.acquire()         # Wait if no empty slots
        mutex.acquire()         # Enter critical section
        
        buffer.append(item)     # Produce (add item to buffer)
        print(f"Producer {producer_id} produced {item}. Buffer size: {len(buffer)}")
        
        mutex.release()         # Exit critical section
        full.release()          # Signal that buffer has one more full slot
        
        time.sleep(random.uniform(0.1, 0.5))  # Simulate production time

# Consumer thread
def consumer(consumer_id, items_to_consume=10):
    for _ in range(items_to_consume):
        full.acquire()          # Wait if no full slots
        mutex.acquire()         # Enter critical section
        
        item = buffer.pop(0)    # Consume (remove item from buffer)
        print(f"Consumer {consumer_id} consumed {item}. Buffer size: {len(buffer)}")
        
        mutex.release()         # Exit critical section
        empty.release()         # Signal that buffer has one more empty slot
        
        time.sleep(random.uniform(0.1, 0.5))  # Simulate consumption time

# Main function
def main():
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer, args=(1, 20))
    consumer_thread = threading.Thread(target=consumer, args=(1, 20))
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print("Producer-Consumer simulation completed.")

if __name__ == "__main__":
    main()
