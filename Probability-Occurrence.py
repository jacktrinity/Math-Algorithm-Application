"""
Probability of an event occuring at least once.

Given a probability of an event occuring and n amount of trials,
find the probability that it will occur at least once.
    
i.e. What is the probability of getting head, at least once, if given 4 coins?
p(at least one head | 4 trials) = 0.9375

CodeSkulptor: https://py3.codeskulptor.org/#user306_qjCERiGxA3_0.py
Written in Python 3
"""

def event_outcome(p_chance, n):
    """
    Take two arguments
    p_chance is the probability of an event occuring
    n amount of given trials
    
    return a float of the probability of the event occuring at least once
    """
    whole_space = float(1)
    p_not_occuring = (1 - p_chance) ** n
    
    # p(occuring at least once) = p(whole space) - p(not occuring)
    return whole_space - p_not_occuring
    
