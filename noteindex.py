note_names_list = []

for number in range(1,8):
    note_names_list.append("Sub " + str(number))
for number in range(1,8):
    note_names_list.append("Low " + str(number))
for number in range(1,8):
    note_names_list.append("Middle " + str(number))
for number in range(1,8):
    note_names_list.append("High " + str(number))

min_pent_note_list = []
for number in (0,2,3,4,6,7,9,10,11,13,14,16,17,18,20,21,23,24,25,27):
    min_pent_note_list.append(note_names_list[number])

maj_pent_note_list = []
for number in (0,1,2,4,5,7,8,9,11,12,14,15,16,18,19,21,22,23,25,26):
    maj_pent_note_list.append(note_names_list[number])

min_pent_note_dictionary = {}
for number in range(0,5):
    min_pent_note_dictionary[str(number + 1)] = min_pent_note_list[(number+4):(number+16)]
