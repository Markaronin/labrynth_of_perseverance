
num_rows, num_cols = [int(x) for x in input().split(' ')]

# Indexing should be [row][col]
tiles = [[c for c in input()] for _ in range(num_rows)]

possible_states = [[[] for _ in range(num_cols)] for _ in range(num_rows)]

for row in range(num_rows):
    for col in range(num_cols):
        if row == 0 and col == 0:
            input_states = [(100, 0)]
        elif row == 0:
            input_states = possible_states[row][col - 1]
        elif col == 0:
            input_states = possible_states[row - 1][col]
        else:
            input_states = possible_states[row -
                                           1][col] + possible_states[row][col - 1]

        input_states = set(input_states)

        filtered_input_states = []
        for state in set(input_states):
            bad = False
            for state_2 in input_states:
                if state_2[0] >= state[0] and state_2[1] > state[1]:
                    bad = True
                elif state_2[0] > state[0] and state_2[1] >= state[1]:
                    bad = True
            if not bad:
                filtered_input_states.append(state)

        for state in filtered_input_states:
            tile = tiles[row][col]
            if tile == '.':
                possible_states[row][col] += [state]
            elif tile == '@':
                pass
            elif tile == '%':
                possible_states[row][col] += [(min(100,
                                               state[0] + 25), state[1])]
            elif tile == '=':
                possible_states[row][col] += [(min(100,
                                               state[0] + 50), state[1])]
            elif tile == '^':
                new_state = (state[0] - 5, state[1])
                if new_state[0] > 0:
                    possible_states[row][col] += [new_state]
            elif tile == '~':
                new_state = (state[0] - 10, state[1])
                if new_state[0] > 0:
                    possible_states[row][col] += [new_state]
            elif tile == '#':
                new_state = (state[0] - 25, state[1])
                if new_state[0] > 0:
                    possible_states[row][col] += [new_state]
            elif tile == '*':
                possible_states[row][col] += [(state[0], state[1] + 5)]
            elif tile == '&':
                possible_states[row][col] += [(state[0], state[1] + 25)]
            elif tile == '$':
                possible_states[row][col] += [(state[0], state[1] + 50)]
            else:
                raise ValueError(f"Error: Unrecognized tile {tile}")


end_state = possible_states[num_rows - 1][num_cols - 1]
if len(end_state) > 0:
    best_end_state = sorted(
        end_state, key=lambda x: (x[1], x[0]), reverse=True)[0]
    print(f"{best_end_state[1]} {best_end_state[0]}")
else:
    print("-1 -1")
