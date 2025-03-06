# This program checks the availability of tables in a restaurant.
# and the subsequent rows indicate whether the table is occupied ('x') or free ('o').
restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

def get_free_tables(tables):
    free_tables = []
    for col in range(1, len(tables[0])):  # Skip the first column (headers)
        for row in range(1, len(tables)):  # Skip the first row (header)
            if tables[row][col] == 'o':  # Check if table is free
                free_tables.append(tables[0][col])  # Add table ID
    return free_tables

free_tables = get_free_tables(restaurant_tables2)
print(free_tables)
