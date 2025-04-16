from ds import RelationTable, HashTable
import re

#column = 'a2'
def build(table, column):
    buildTable = HashTable() #default size currently 3, should I change?

    index = int(re.search(r'\d+', column).group()) - 1

    for row in table.get_table():
        key = row[index]
        buildTable.insert(key, row)

    return buildTable


def probe(initialBuild, probe, build, j1, j2):
    resultant_size = initialBuild.get_table_size() + probe.get_table_size()
    resultant_identifier = initialBuild.get_identifier() + probe.get_identifier()
    resultant = RelationTable('R12', resultant_size, resultant_identifier)
    
    right_index = int(re.search(r'\d+', j2).group()) - 1

    for row in probe.get_table():
        key = row[right_index]
        if build.get_value(key) is not None:

            left_index = int(re.search(r'\d+', j1).group()) - 1
            buildRef = build.get_value(key)

            for t in buildRef:
                insertRelation = list()
                
                if t[left_index] == key:    
                    for i in t: #initial buildTable
                        insertRelation.append(i)
                
                    for i in row: #probeTable
                        insertRelation.append(i)
                
                if len(insertRelation) > 0:
                    resultant.add(tuple(insertRelation))

    return resultant


def hash_join(s, l, j1, j2):
    buildTable = build(s, j1)

    result = probe(s, l, buildTable, j1, j2)

    return result