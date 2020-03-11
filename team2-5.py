import random 

choices= ["b", "c"]

team_name = 'The Rainbow Sparkle Fairies of death'
strategy_name =  'yeah'
strategy_description = 'it do be like dat'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    
    '''

    c = 0
    b = 0   
    # for letter in my_history:
    #   print("My history: ")
    #   if letter.lower() == "c":
    #     c = c + 1
    #   elif letter.lower() == "b":
    #     b = b + 1

    for letter in their_history:
      if letter.lower() == "c":
        c = c + 1
      elif letter.lower() == "b":
        b = b + 1
    if c >= b :
      return 'c'
    elif b >= c:
      return random.choice(choices)
    else:
      return 'b'
