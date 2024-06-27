'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    from_member_following = social_graph[from_member]['following']
    to_member_following = social_graph[to_member]['following']
    if to_member in from_member_following and from_member in to_member_following:
        return 'friends'
    elif to_member in from_member_following:
        return 'follower'
    elif from_member in to_member_following:
        return 'followed by'
    else:
        return 'no relationship'
    
    

def tic_tac_toe(board):
    '''Tic Tac Toe.

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
    grid_count = len(board)
    rows = board
    cols = [[board[i][j] for i in range(grid_count)] for j in range(grid_count)]
    fwd_diag = [board[grid_count-1-i][i] for i in range(grid_count)]
    bwd_diag = [board[i][i] for i in range(grid_count)]
    lines = rows + cols + [fwd_diag] + [bwd_diag]
    for line in lines:
        if len(set(line)) == 1 and line[0] in {'X', 'O'}:
            return line[0]    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
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
    leg_list = list(route_map)
    leg_count = len(leg_list)
    for leg in leg_list:
        if leg[0] == first_stop:
            start_leg = leg
            break
    travel_time = 0
    current_leg = start_leg
    while True:
        travel_time += route_map[current_leg]["travel_time_mins"]
        if current_leg[1] == second_stop:
            break
        next_leg_index = (leg_list.index(current_leg) + 1) % leg_count
        current_leg = leg_list[next_leg_index]
    return travel_time