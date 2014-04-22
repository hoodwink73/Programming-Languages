This is a repo for all the relevant problems and reads I come accross in
the MOOC, [**Programming Languages**](https://www.udacity.com/course/cs262) offered at [Udacity](https://www.udacity.com) by Westley Weimer.


# Unit 1

Introduction to basic regualar expressions and finite state machines.

-  *Strings* are sequences of characters
-  *Regular Expressions* are concise notation for specifying sets o strings. More flexible than string matching
-  *Finite State Machine* are pictorial equivalent to re.
-  *Every regular expression* has a finte state machine and vic versa
-  Every FSM can be converted to a deterministic FSM(no epsilon, no ambiguity).

A finite-state machine (FSM) or finite-state automaton (plural: automata), or simply a state machine, is a mathematical model of computation used to design both computer programs and sequential logic circuits. It is conceived as an abstract machine that can be in one of a finite number of states. The machine is in only one state at a time; the state it is in at any given time is called the current state. It can change from one state to another when initiated by a triggering event or condition; this is called a transition. A particular FSM is defined by a list of its states, and the triggering condition for each transition.
[Credit: Wikipedia](http://en.wikipedia.org/wiki/Finite-state_machine)

A finite state machine with epsilon transitions or multiple outgoing edges leaving the same state with the same label is ambiguous. A finite state machine accepts a string if there is any path for that string that leads to an accepting state. 

## Matching Phone Number

A regexp for matching a phone number with a group of numbers which may seperated
by a `-`

For example, the regexp should match these:

123-4567  
1234567  
08-78-88-88-88  
0878888888  

but not this   
-6  

```python
regexp = r'(?:[0-9]+-)*[0-9]'
```

A finite state machine with epsilon transitions or multiple outgoing edges is called **non-deterministic**. By contrast, a "lock-step" finite state machine is called **deterministic**.

*Every non-deterministic FSM has a correspondingly deterministic FSM that accepts exactly the same string*

Non-deterministic finite state machines are **NOT MORE POWERFUL**, they are just more convinient.
