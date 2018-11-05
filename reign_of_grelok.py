import grelok_subroutines as gs

# TODO: FSM seems like the best approach for this RPG
# TODO: Use JSON format for storing text and FSM

gs.routine_010()

key = gs.routine_100()

gs_100_mapped = gs.routine_100_map(key)
if isinstance(gs_100_mapped, str):
    print(gs_100_mapped)
else:
    if gs_100_mapped == 17:
        key = gs.routine_101()
