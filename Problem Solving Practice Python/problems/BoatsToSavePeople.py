'''
881. Boats to Save People
Solved
Medium
Topics
Companies
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''


def numRescueBoats(people, limit: int) -> int:
    l, r = 0, len(people)-1
    people.sort()
    boats = 0 
    while l <= r:
        if people[l] + people[r] <= limit:
            boats += 1
            l += 1
            r -= 1
            
        else:
            r -= 1
            boats += 1
    return boats