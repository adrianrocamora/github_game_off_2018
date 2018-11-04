import grelok_subroutines as gs

# TODO: FSM seems like the best approach for this RPG

gs.routine_010()

key = gs.routine_100()


# TODO assign f(key) to a variable and remove the input output

if isinstance(gs.routine_100_map(key), str):
    print(gs.routine_100_map(key))
else:
    if gs.routine_100_map(key) == 17:
        key = gs.routine_101()
