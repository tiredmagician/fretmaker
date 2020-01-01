
#dictionary with mappings of all the red dots
finger_positions = {
    'A0': [67,8,81,22],
    'A1': [143,8,157,22],
    'A2': [220,8,234,22],
    'A3': [295,8,309,22],
    'A4': [373,8,387,22],
    'B0': [67,43,81,57],
    'B1': [143,43,157,57],
    'B2': [220,43,234,57],
    'B3': [295,43,309,57],
    'B4': [373,43,387,57],
    'C0': [67,78,81,92],
    'C1': [143,78,157,92],
    'C2': [220,78,234,92],
    'C3': [295,78,309,92],
    'C4': [373,78,387,92],
    'D0': [67,113,81,127],
    'D1': [143,113,157,127],
    'D2': [220,113,234,127],
    'D3': [295,113,309,127],
    'D4': [373,113,387,127],
    'E0': [67,148,81,162],
    'E1': [143,148,157,162],
    'E2': [220,148,234,162],
    'E3': [295,148,309,162],
    'E4': [373,148,387,162],
    'F0': [67,183,81,197],
    'F1': [143,183,157,197],
    'F2': [220,183,234,197],
    'F3': [295,183,309,197],
    'F4': [373,183,387,197],
    }

#dictionaries with scale positions
min_pent_positions = {
    '1': ['A1','A3','B1','B3','C0','C3','D0','D3','E1','E3','F1','F3'],
    '2': ['A0','A3','B0','B3','C0','C2','D0','D2','E0','E2','F0','F3'],
    '3': ['A1', 'A3','B1','B3','C0','C2','D0','D3','E0','E3','F1','F3'],
    '4': ['A1','A3','B1','B4','C0','C3','D1','D3','E1','E3','F1','F3'],
    '5': ['A0','A3','B1','B3','C0','C2','D0','D2','E0','E3','F0','F3'],
    }

#dictionary of fret marker mappings
def make_list(x):
    if x >= 12:
        x = (x-12)
    list = []
    for value in range(6):
        list.append(str(x + value))
    return list

fret_marker_mappings = {}
list = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
for note in list:
    fret_marker_mappings[note + "_min_pent_1"] = make_list(list.index(note) + 1)
    fret_marker_mappings[note + "_min_pent_2"] = make_list(list.index(note) + 4)
    fret_marker_mappings[note + "_min_pent_3"] = make_list(list.index(note) + 6)
    fret_marker_mappings[note + "_min_pent_4"] = make_list(list.index(note) + 8)
    fret_marker_mappings[note + "_min_pent_5"] = make_list(list.index(note) + 11)
