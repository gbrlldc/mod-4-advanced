def relationship_status(from_member, to_member, social_graph):
  '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
  # Replace `pass` with your code.
  # Stay within the function. Only use the parameters as input. The function should return your answer.


social_graph = {
  "@gaebrell": {
    "first_name": "Gab",
    "last_name": "Dela Cruz",
    "following": []
  },
  "@yydc": {
    "first_name": "Yeyo",
    "last_name": "Kong",
    "following": ["@gaebrell", "@deighnyell"]
  },
  "@deighnyell": {
    "first_name": "Danielle",
    "last_name": "Dela Cruz",
    "following": ["@gaebrell", "@yydc", "@ynelara"]
  },
  "@ynelara": {
    "first_name": "Yannie",
    "last_name": "Kong",
    "following": ["@deighnyell", "@NewJeans", "@yydc"]
  },
  "@NewJeans": {
    "first_name": "New",
    "last_name": "Jeans",
    "following": ["@deighnyell", "@ADORA", "@gaebrell"]
  },
  "@ADORA": {
    "first_name": "ADORA",
    "last_name": "Entertainment",
    "following": ["@NewJeans", "@gaebrell"]
  },
}


def relationship_status(from_member, to_member, social_graph):
  follower = False
  followed_by = False

  for i in social_graph[from_member]['following']:
    if i == to_member:
      follower = True
  for i in social_graph[to_member]['following']:
    if i == from_member:
      followed_by = True

  if follower is True and followed_by is False:
    return 'follower'
  elif follower is False and followed_by is True:
    return 'followed by'
  elif follower and followed_by is True:
    return 'friends'
  else:
    return 'no relationship'


print("I. Relationship Status")
from_member = str(input('Enter First User: '))
to_member = str(input('Enter Second User: '))
print(relationship_status(from_member, to_member, social_graph))


def tic_tac_toe(board):
  '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
  # Replace `pass` with your code.
  # Stay within the function. Only use the parameters as input. The function should return your answer.


board1 = [
  ['X', 'X', 'O'],
  ['O', 'X', 'O'],
  ['O', '', 'X'],
]

board2 = [
  ['X', 'X', 'O'],
  ['O', 'X', 'O'],
  ['', 'O', 'X'],
]

board3 = [
  ['O', 'X', 'O'],
  ['', 'O', 'X'],
  ['X', 'X', 'O'],
]

board4 = [
  ['X', 'X', 'X'],
  ['O', 'X', 'O'],
  ['O', '', 'O'],
]

board5 = [
  ['X', 'X', 'O'],
  ['O', 'X', 'O'],
  ['X', '', 'O'],
]

board6 = [
  ['X', 'X', 'O'],
  ['O', 'X', 'O'],
  ['X', '', ''],
]

board7 = [['X', 'X', 'O', ''], ['O', 'X', 'O', 'O'], ['X', '', '', 'O'],
          ['O', 'X', '', '']]

print("II. Tic Tac Toe")
winner = ''


def tic_tac_toe(board):
  winner = ''
  for row in board:
    if all(i == row[0] for i in row):
      winner = row[0]
      return winner
  for col in range(len(board)):
    if all(board[i][col] == board[0][col] for i in range(len(board))):
      winner = board[0][col]
      return winner
  if all(board[i][i] == board[0][0] for i in range(len(board))):
    winner = board[0][0]
    return winner
  elif all(board[i][len(board) - i - 1] == board[0][len(board) - 1]
           for i in range(len(board))):
    winner = board[0][len(board) - 1]
    return winner
  else:
    winner = 'NO WINNER'
    return winner


winner = tic_tac_toe(board7)
print(winner)


def eta(first_stop, second_stop, route_map):
  '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
  # Replace `pass` with your code.
  # Stay within the function. Only use the parameters as input. The function should return your answer.


legs = {
  ("upd", "admu"): {
    "travel_time_mins": 15
  },
  ("admu", "dlsu"): {
    "travel_time_mins": 40
  },
  ("dlsu", "upd"): {
    "travel_time_mins": 60
  }
}

print("III. Expected Time of Arrival")

first_stop = str(input('Enter Origin: '))
second_stop = str(input('Enter Destination: '))


def eta(first_stop, second_stop, route_map):
  origin = [x[0] for x in route_map]
  destination = [y[1] for y in route_map]
  time = list(route_map.values())
  minutes = 0
  minutes += time[origin.index(first_stop)]["travel_time_mins"]

  if first_stop == 'upd' and second_stop == 'admu':
    print('It will take', minutes, 'minutes to travel from', first_stop, 'to',
          second_stop)
    return minutes
  elif first_stop == 'admu' and second_stop == 'dlsu':
    print('It will take', minutes, 'minutes to travel from', first_stop, 'to',
          second_stop)
    return minutes
  elif first_stop == 'dlsu' and second_stop == 'upd':
    print('It will take', minutes, 'minutes to travel from', first_stop, 'to',
          second_stop)
    return minutes
  else:

    while second_stop != destination[origin.index(first_stop)]:
      first_stop = destination[origin.index(first_stop)]
      minutes += time[origin.index(first_stop)]["travel_time_mins"]
      print('It will take', minutes, 'minutes to travel from', first_stop,
            'to', second_stop)
      return minutes


eta(first_stop, second_stop, legs)
