def make_single(table, attr):
    """
    Returns a selection of rows in table such as values of attribute attr are not duplicated.
    """
    res = []
    values = []
    for data in table:
        if attr in data :
            value = data[attr]
            if value is not None:
                if not value in values :
                    values.append(value)
                    res.append(data)
    return res

def get_values(table, attr):
    """
    Returns the set (as a list) of values of attr (i.e. no duplication).
    """
    values = []
    for data in table:
        if attr in data :
            value = data[attr]
            if value is not None:
                if not value in values :
                    values.append(value)
    return values


def group_values_fct(table, attr, group_of):
    """
    group_of(value) returns the group, or None
    Returns the table, where attr is replaced by its group name (or removed if None).
    """
    res = []
    for data in table:
        if attr in data :
            grp = group_of(data[attr])
            if grp is not None :
                d = {k : v  for k, v in data.items()}
                d[attr] = grp
                res.append(d)
    return res
                
def group_values_dict(table, attr, groups):
    """
    groups is {g1 : [val1, val2, ...], g2 : [val1, val2, ...]}
    Returns the table, where attr is replaced by its group name (or removed if no group is found).
    """
    def group_of(val):
        for g, vs in groups.items() :
            if val in vs :
                return g
    return group_values_fct(table, attr, group_of)

def pie_data(table, attr):
    """
    returns {'labels' : [sort1, sort2, ...], 'fracs' : [nb_sort1, nb_sort2, ...]}
    """
    count = {v:0 for v in get_values(table, attr)}
    for data in table:
        if attr in data :
            value = data[attr]
            if value is not None:
                count[value] += 1
    return {'labels' : count.keys(), 'fracs' : count.values()}
    


if __name__ == "__main__":

    table = [{'Name' : 'Pierre',  'Age': 50, 'Sex' : 'M'},
             {'Name' : 'Peter',   'Age': 40, 'Sex' : 'M'},
             {'Name' : 'Paul',    'Age': 40, 'Sex' : 'M'},
             {'Name' : 'Paul',    'Age': 20, 'Sex' : 'M'},
             {'Name' : 'Marie',   'Age': 50, 'Sex' : 'F'},
             {'Name' : 'Lucy',    'Age':  5, 'Sex' : 'F'},
             {'Name' : 'Mary',    'Age': 30, 'Sex' : 'F'},
             {'Name' : 'Rachid',  'Age': 30, 'Sex' : 'M'},
             {'Name' : 'Lucy',    'Age': 40, 'Sex' : 'F'}]

    country_of = {'FR' : ['Pierre', 'Paul', 'Marie'],
                  'US' : ['Peter', 'Mary', 'Lucy']}
    age_of = {'old' : [40, 50],
              'young' : [20, 30]}

    print('Data\n\n')
    print(table)
    print()
    print('Values')
    print(get_values(table, 'Age'))
    print(get_values(table, 'Name'))
    print()
    print('Make single')
    print(make_single(table, 'Age'))
    print(make_single(table, 'Sex'))
    print()
    print('Group values')
    print(group_values_dict(table, 'Age', age_of))
    print(group_values_dict(table, 'Name', country_of))
    print()
    print('Pie')
    print(pie_data(table, 'Age'))
    print(pie_data(table, 'Sex'))
