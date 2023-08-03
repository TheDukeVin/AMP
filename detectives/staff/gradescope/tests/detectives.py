#!/usr/bin/env python3

def dezero(deg_seq):
    return [degree for degree in deg_seq if degree != 0]

def decrement(deg_seq):
    return [d - 1 for d in deg_seq]

def detect(deg_seq):
    """
    Validate whether the sequence of numbers is a valid degree sequence
    """
    deg_seq = dezero(deg_seq)
    deg_seq.sort(reverse=True)
    if len(deg_seq) > 0:
        head = deg_seq[0]
        deg_seq = deg_seq[1:]
        if head > len(deg_seq):
            return False
        else:
            next_deg_seq = decrement(deg_seq[0:head]) + deg_seq[head:]
            return detect(next_deg_seq)
    else:
        return True