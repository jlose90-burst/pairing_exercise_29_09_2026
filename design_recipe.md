## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# list of names 

# Return type:
# string of people of names with an & between the last pair, and seperated by commas in the lenght of returned names is less than 3

# Side Effects:
# No side effects 

def your_function():
    pass
```

## 3 exampples
```python
# scenario 1

# scenario 2

# scenario 3
```