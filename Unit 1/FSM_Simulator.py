# FSM Simulation

# edges are how an FSM is represented as a data unit
# Every edge is a key value pair
# A key is a tuple of (current_state, character)
# The value is the next state achieved after the previous 
# state consumes a particular character

# r'a+1+'
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



def test():
    # r'a+1+'
    plus_edges = {(1, 'a') : 2,
             (2, 'a') : 2,
             (2, '1') : 3,
             (3, '1') : 3}

    # a list of accepting states
    plus_accepting = [3]

    #r'q*'
    star_edges = {
        (1, 'q'): 1
    }

    # a list of accepting states
    star_accepting = [1]

    assert fsmsim("aaa111", 1, plus_edges, plus_accepting) == True
    assert fsmsim("a1a1a1", 1, plus_edges, plus_accepting) == False
    assert fsmsim("", 1, star_edges, star_accepting) == True
    assert fsmsim("q", 1, star_edges, star_accepting) == True
    assert fsmsim("qqqq", 1, star_edges, star_accepting) == True
    assert fsmsim("a", 1, star_edges, star_accepting) == False

    print "All test passed"



test()
# print fsmsim("aaa111",1,edges,accepting)
# >>> True