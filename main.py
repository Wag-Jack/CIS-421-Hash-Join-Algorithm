import ds

R1 = ds.RelationTable('R1', 3, 'a')
R2 = ds.RelationTable('R2', 4, 'b')

R1.add((1, 2, 3))
R1.add((4, 5, 6))
R1.add((7, 8, 9))

R2.add((1, 2, 3, 4))
R2.add((11, 12, 13, 14))
R2.add((1111, 2222, 3333, 4444))
R2.add((0, 0, 0, 0))

R1.print_table()
R2.print_table()

r1 = R1.get_table_size()
r2 = R2.get_table_size()

if r1 >= r2:
    ds.hash_join(r1, r2)
else:
    ds.hash_join(r2, r1)

