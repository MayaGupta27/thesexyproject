###################
#	Midterm
#	Due: Tuesday, November 28 2017
###################

# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# You will lose points if your solution uses division.
# Your solution should run in O(n) time.
# Your solution should not allocate any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers, with len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#

def array_almost_product(arr):
    arr2 = [None] * len(arr)
    product = 1
    for i in range(len(arr)):
        arr2[i] = product
        product = product * arr[i]
    product = 1
    for i in range(len(arr) - 1,-1,-1):
        arr2[i] = arr2[i] * product
        product = product * arr[i]
    return arr2


# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#

def pascals_triangle(n):
    val = 1
    list = [val]
    if(n==1):
        return list
    elif(n==0 or n==None):
        return None
    else:
        for iter in range(n):
            step = n - iter
            val = (val * (step)) // (iter + 1)
            list.append(val)

        return list

# Alive People
#
# Write a function that, given a list of strings representing a person's birth year: age of death,
# will return the year that had the most people alive (inclusive). If there are multiple years that tie, return the earliest.
# You can think of a birthdate and a deathdate as a range of years. Of all the birth years in the list, find the one where the highest
# amount of people in the list were still alive.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#

def alive_people(people):
    pass


# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurences of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But the person who wrote all of your homewokrs wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the homework creator made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# the_string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.

def string_my_one_true_love(the_string):
    pass


# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest Palindrome substring

def longest_palindrome_substring(word):
    if(word == None):
        return None
    max = 1
    start = 0
    beg = 0
    end = 0
    for i in range(1, len(word)):
        beg = i - 1
        end = i
        while (beg >= 0) and (end < len(word)) and (word[beg] == word[end]):
            if (end - beg + 1) > max:
                start = beg
                max = end - beg + 1
            beg = beg - 1
            end = end + 1
        beg = i - 1
        end = i + 1
        while (beg >= 0) and (end < len(word)) and (word[beg] == word[end]):
            if (end - beg + 1) > max:
                start = beg
                max = end - beg + 1
            beg = beg - 1
            end = end + 1

    return word[start:start + max]



# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
# Do not consider case. Therefore, 'A' and 'a' are considered the same character
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "zzAabcdefFgg"
#
#   Output:
#   "abcdef"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring

def longest_unique_substring(word):
    max = ''
    current = ''

    for i, char in enumerate(word):
        if char.lower() not in current.lower():
            current = current + char
            if len(current) >= len(max):
                max = current
        else:
            current = char
    return str(max)

# Three Sum
#
# Given an array S of n integers and constant 'target', are there elements a, b, c in S such that
# a+b+c = target? Find all unique triplets in the array which gives the sum of target.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.

def three_sum(arr, target):
    result = []
    for i, i_data in enumerate(arr[0:len(arr) - 2]):
        for j, j_data in enumerate(arr[i + 1:len(arr) - 1]):
            for k, k_data in enumerate(arr[j+1:len(arr)]):
                if(i_data + j_data + k_data == target):
                    if sorted([i_data,j_data, k_data]) not in result:
                        result.append(sorted([i_data, j_data, k_data]))
    return result


# Zero Sum
#
# Return True if a subarray (not any element) summed can create 0.
# Otherwise return False.
#
# Time Complexity
# ------------
# Optimal time complexity is O(n). You can assume the running time of updating a dictionary is O(1)
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr: array
#   array of numbers

def zero_sum(arr):
    list = []
    sum = 0
    for i in arr:
        index = arr.index(i)
        sum = sum + arr[index]
        if (arr[index] == 0 or sum == 0 or sum in list != None):
            return True
        list.append(sum)
    return False



# Stair Stepping
#
# One day, Alice's power went out in her house.
# Because Alice is currently in 374, she decided to count how many distinct ways she can climb up her staircase (from the bottom to the last stair). Alice is able to skip some stairs because she has very long legs.
# Help Alice determine the number of distinct ways she can climb up the staircase given the number of stairs on the staircase (stairs) and the maximum number of stairs she can skip at each one of her steps (skip).
#
# Time Complexity
# ---------------
# Optimal time complexity is O(stairs).
# Example 1:
# stairs = 3
# skip = 0
#
#   #
#  ##
# ###
# 123
#
# Alice cannot skip any stairs, so there is only one way.
# BOTTOM -> 1 -> 2 -> 3
#
# Example 2:
# stairs = 3
# skip = 1
#
#   #
#  ##
# ###
# 123
#
# Alice can skip one stair at most, so there are 3 ways.
# BOTTOM -> 1 -> 2 -> 3
# BOTTOM -> 1 -> 3
# BOTTOM -> 2 -> 3
#
# Example 3:
# stairs = 5
# skip = 2
#
#     #
#    ##
#   ###
#  ####
# #####
# 12345
#
# Alice can skip two stairs at most, so there are 13 ways.
#
# BOTTOM -> 1 -> 2 -> 3 -> 4 -> 5
# BOTTOM -> 1 -> 2 -> 3 -> 5
# BOTTOM -> 1 -> 2 -> 4 -> 5
# BOTTOM -> 1 -> 3 -> 4 -> 5
# ...
# ...
# ...
# BOTTOM -> 3 -> 5
#
# Note that Alice must start at the "0th" step and finish exactly at the Nth step where N is the number of stairs.




def staircase_ways(stairs, skip):
    if (stairs < 1):
        return 0
    for i in range(skip + 1):
        return staircase_ways(stairs - (i +1), skip) + 1



# Odd One Out
#
# Given an array of 2n + 1 integers where each integer except one is duplicated, return the number that only appears once in the array.
#
# Time complexity
# ---------------
# Optimal time complexity is O(n). Try to only use O(1) space/memory.
#
# Example 1:
# arr = [10]
# Answer is 10.
#
# Example 2:
#
# arr = [3, 2, 1, 3, 2, 4, 4]
# Answer is 1.
#
#
# Example 3:
# arr = [-1, 1, 0, 5, 0, 2, 1, 2, 5]
# Answer is -1.

def odd_one_out(arr):
    arith = 2 * sum(set(arr)) - sum(arr)
    return arith


# Circular Shift
#
# Given an array (arr) and a shift value (k), shift the array to the
# right by k. If the rightmost element will become out of bounds, move
# it to the front of the array (hence circular shift).
#
# Time complexity
# ---------------
# Optimal complexity is O(len(arr)). Try using only O(1) space/memory
#
# Example 1:
# arr = [1, 2, 3, 4, 5]
# k = 1
# Returns [5, 1, 2, 3, 4]
#
# Example 2:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Returns [4, 5, 1, 2, 3]
#
# Example 3:
# arr = [1, 2, 3]
# k = 10
# Returns [3, 1, 2]


def circular_shift(arr, k):
    ranged = list(range(len(arr)))
    new = ranged
    newK = k % len(arr)
    for i in ranged:
        new[i] = arr[i - newK]
    return new

# Reverse Linked List
#
# Given a linked list, reverse it in-place
#
# Time Complexity
# ---------------
# Optimal time complexity is O(n). Try to use only O(1) memory.

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def reverse_list(head):
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head


