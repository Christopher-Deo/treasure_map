row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# assigning user's choice to variable to be able select the position on the map
selected_column = int(position[0])
selected_row = int(position[1])
# placing the treasure on the map
map[selected_row - 1][selected_column-1] = 'X'
# creating a new map with the treasure marked
print(f"{row1}\n{row2}\n{row3}")
