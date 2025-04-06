import itertools
import time


def generator_with_count(limit):
    start = time.time()
    numbers = itertools.count()
    
    for number in numbers:
        
        if number > limit:
            final = time.time()
            break
        
        print(number)
    
    final = time.time()
    total_time = round(final - start, 5)
    return f"Execution time: {total_time} seconds"
    
