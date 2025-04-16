from ds import RelationTable
from hash_join import hash_join

R1 = RelationTable('R1', 3, 'a')
R2 = RelationTable('R2', 4, 'b')

R1.add((1, 4, 5))
R1.add((2, 6, 7))
R1.add((3, 8, 9))

R2.add((1, 2, 5, 6))
R2.add((2, 3, 7, 9))
R2.add((3, 1, 6, 0))
R2.add((4, 7, 3, 2))

R1.print_table()
R2.print_table()

r1 = R1.get_table_size()
r2 = R2.get_table_size()

join1 = input('Choose what column you\'re joining from R1: ')
join2 = input('Choose what column you\'re joining from R2: ')

if r1 <= r2:
    hashJoinedTable = hash_join(R1, R2, join1, join2)
else:
    hashJoinedTable = hash_join(R2, R1, join1, join2)

hashJoinedTable.print_table()