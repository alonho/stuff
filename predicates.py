import time

def time_predicate(timeout):
    """
    replaces the a common pattern of retrying things within a timeout,
    what used to go like this:

    finishtime = time.time() + TIMEOUT
    while time.time() < finishtime:
        pass
    
    replaced with:
    
    for _ in time_predicate(TIMEOUT):
        pass
    """
    finish_time = time.time() + timeout
    while time.time() < finish_time:
        yield

def test_time_predicate():
    timeout = 0.3
    stime = time.time()
    for _ in time_predicate(timeout):
        pass
    assert time.time() - stime >= timeout
