def isInList(_list, item):
    for list_item in _list:
        if item == list_item:
            return True
    return False


class diap_board_state:
    @staticmethod
    def isDiap(state):
        if len(state) != 9:
            return False
        return True

    def state_to_string(self):
        result = ""
        for symbol in self.state:
            result = result + symbol
        return result

    def __eq__(self, other):
        if isinstance(other, diap_board_state):
            return (self.state == other.state)

    def __init__(self, state):
        if diap_board_state.isDiap(state):
            self.state = state.copy()
        else:
            raise

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i * 3 + j], ' ', end='')
            print()

    def get_possible_moves(self):
        for i in range(len(self.state)):
            if self.state[i] == ' ':
                break;
        possible = [1, -1, 3, -3]
        result = list()
        for j in range(len(possible)):
            if 0 <= i + possible[j] < len(self.state) and abs(i % 3 - (i + possible[j]) % 3) < 2:
                move = diap_board_state(self.state)
                temp = move.state[i]
                move.state[i] = move.state[i + possible[j]]
                move.state[i + possible[j]] = temp
                result.append(move)
        return result

    @staticmethod
    def best_move_sequence(start_state, goal_state):
        checked = dict()
        checked[start_state.state_to_string()] = 1
        to_check = list()
        temp = list()
        to_check.append(start_state)
        isFound = False
        while not isFound:
            for pos in to_check:
                if pos == goal_state:
                    isFound = True
                    break
            if not isFound:
                temp.clear()
                temp = to_check.copy()
                to_check.clear()
                for pos in temp:
                    for next_move in pos.get_possible_moves():
                        if checked.get(next_move.state_to_string()) == None:
                            # Values in dict are previous board_states
                            checked[next_move.state_to_string()] = pos
                            to_check.append(next_move)
        result = list()
        result.append(goal_state)
        current = goal_state
        while not current == start_state:
            current = checked.get(current.state_to_string())
            result.insert(0, current)
        return result


goal_pos = diap_board_state(['d', 'i', 'a', 'p', 'a', 'z', 'o', 'n', ' '])
start_state = list()
user_input = input("Enter initial board state:\n")
for i in range(len(user_input)):
    start_state.append(user_input[i])
start_pos = diap_board_state(start_state)
res = diap_board_state.best_move_sequence(start_pos, goal_pos)
print()
print(len(res) - 1, " moves needed\n")
for state in res:
    state.print()
    print()
