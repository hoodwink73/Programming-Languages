# FSM Simulation

# edges are how an FSM is represented as a data unit
# Every edge is a key value pair
# A key is a tuple of (current_state, character)
# The value is the next state achieved after the previous 
# state consumes a particular character
edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

# a list of accepting states
accepting = [3]

def fsmsim(string, current, edges, accepting):
    # if the string is exhausted and we the current state is
    # an accepting state, then we have a match
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        if (current, letter) in edges:
            # trim off the consumed character from the string
            remaining_string = string[1:]
            
            # get the next step from the provided hash
            # after the current state consumes a particular character
            next_step = edges[(current, letter)]
            
            return fsmsim(remaining_string, next_step, edges, accepting)
        else:
            # if the current state does not consume the given letter
            # we have a fall off
            return False


print fsmsim("aaa111",1,edges,accepting)
# >>> True