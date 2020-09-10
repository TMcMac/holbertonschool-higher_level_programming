#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # We need this check for a None
        my_list = list(a_dictionary.keys())
        # Making a list of keys for the for loop
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                # The above looks at the value in each key
                score = a_dictionary[i]
                # If the value is greater that whats in score, reassign
                leader = i
                # If the score was greater then that key is our new leader
        return leader
