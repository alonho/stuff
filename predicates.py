import time

def time_predicate(timeout):
    finish_time = time.time() + timeout
    while time.time() < finish_time:
        yield

def test_time_predicate():
    stime = time.time()
    for _ in time_predicate(0.5):
        pass
    assert time.time() - stime >= 0.5 


        
