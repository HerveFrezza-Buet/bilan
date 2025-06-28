import datetime

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

def select_fct(table, fct):
    """
    Selects the attributes for which f(data) is True
    """
    res = []
    for data in table:
        if fct(data):
            res.append(data)
    return res

def select_by_date(table, attr, period):
    """
    Selects the attribute (that has to be a date) in period=[start_time, end_time].
    if start_time or end_time is None, the bound is not considered.
    """
    start_time, end_time = period
    def selector(data):
        if attr not in data:
            return False
        date = data[attr]
        if not isinstance(date, datetime.datetime):
            return False
        if (start_time is not None) and (date < start_time):
            return False
        if (end_time is not None) and (date > end_time):
            return False
        return True
    return select_fct(table, selector)
    
def select_in_group(table, attr, group):
    """
    Selects the data for which the attribute attr belongs to group
    """
    def selector(data):
        return (attr in data) and (data[attr] in group)
    return select_fct(table, selector)

def select_not_in_group(table, attr, group):
    """
    Selects the data for which the attribute attr do not belongs to group
    """
    def selector(data):
        return (attr in data) and (data[attr] not in group)
    return select_fct(table, selector)

def get_values(table, attr, order_hint = None):
    """
    Returns the set (as a list) of values of attr (i.e. no duplication).
    order_hits is a liste of possible values. The result of get_value will respect that order for the values in that list.
    """
    values = []
    for data in table:
        if attr in data :
            value = data[attr]
            if value is not None:
                if not value in values :
                    values.append(value)
    if order_hint :
        def key_func(elem):
            if elem in order_hint:
                return order_hint.index(elem)
            else:
                return len(order_hint)
        values.sort(key = key_func)
    return values


def group_values_fct_remove(table, attr, group_of):
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
                
def group_values_dict_remove(table, attr, groups):
    """
    groups is {g1 : [val1, val2, ...], g2 : [val1, val2, ...]}
    Returns the table, where attr is replaced by its group name (or removed if no group is found).
    """
    def group_of(val):
        for g, vs in groups.items() :
            if val in vs :
                return g
    return group_values_fct_remove(table, attr, group_of)

def group_values_fct_keep(table, attr, group_of):
    """
    group_of(value) returns the group, or None
    Returns the table, where attr is replaced by its group name (or kept if None).
    """
    res = []
    for data in table:
        if attr in data :
            grp = group_of(data[attr])
            d = {k : v  for k, v in data.items()}
            if grp is not None :
                d[attr] = grp
                res.append(d)
    return res
                
def group_values_dict_keep(table, attr, groups):
    """
    groups is {g1 : [val1, val2, ...], g2 : [val1, val2, ...]}
    Returns the table, where attr is replaced by its group name (or kept if no group is found).
    """
    def group_of(val):
        for g, vs in groups.items() :
            if val in vs :
                return g
    return group_values_fct_keep(table, attr, group_of)

def group_values_fct_keep_in_attr(table, attr_in, attr_out, group_of):
    """
    group_of(value) returns the group, or None
    The group of attr_in (or the attr_in value if no group si found) is placed in attr_out.
    Returns the table, where attr is replaced by its group name (or kept if None).
    """
    res = []
    for data in table:
        if attr_in in data :
            grp = group_of(data[attr_in])
            d = {k : v  for k, v in data.items()}
            if grp is not None :
                d[attr_out] = grp
            else:
                d[attr_out] = d[attr_in]
            res.append(d)
    return res
                
def group_values_dict_keep_in_attr(table, attr_in, attr_out, groups):
    """
    groups is {g1 : [val1, val2, ...], g2 : [val1, val2, ...]}
    The group of attr_in (or the attr_in value if no group si found) is placed in attr_out.
    Returns the table, where attr is replaced by its group name (or kept if no group is found).
    """
    def group_of(val):
        for g, vs in groups.items() :
            if val in vs :
                return g
    return group_values_fct_keep_in_attr(table, attr_in, attr_out, group_of)

def decode_values(table, attr, codes):
    """
    codes is {tag1 : 'this is tag1 meaning', ...}
    Returns the table, where attr is replaced by its code expansion (or unmodified if no code is found).
    """
    res = []
    for data in table:
        if attr in data :
            d = {k : v  for k, v in data.items()}
            code = d[attr]
            if code in codes:
                d[attr] = codes[code]
            res.append(d)
    return res

def decode_values_in_attr(table, attr_in, attr_out, codes):
    """
    codes is {tag1 : 'this is tag1 meaning', ...}
    Returns the table, where attr_out is filled with attr_in decoding is replaced by its code expansion (or unmodified if no code is found).
    """
    res = []
    for data in table:
        if attr_in in data :
            d = {k : v  for k, v in data.items()}
            code = d[attr_in]
            if code in codes:
                d[attr_out] = codes[code]
            res.append(d)
    return res
                

def pie_data(table, attr, order_hint=None):
    """
    returns {'sorts' : [sort1, sort2, ...], 
             'data'  : [nb_sort1, nb_sort2, ...]}, total_amount_of_data
    """
    count = {v:0 for v in get_values(table, attr, order_hint)}
    total = 0
    for data in table:
        if attr in data :
            value = data[attr]
            if value is not None:
                count[value] += 1
                total        += 1
    return {'sorts' : count.keys(), 'data' : count.values()}, total

def histo_data(table, category_attr, order_hint=None):
    """
    Data for displaying a histo graph. Each bar corresponds to a category,
    for each bar, the amount of values is given.
    returns {'categories : [cat1, cat2, ...],
             'data'      : [nb_for_cat1, nb_for_cat2, ...]}, total
    """
    res = {'categories' : get_values(table, category_attr, order_hint),
           'data'       : []}
    nb_categories = len(res['categories'])
    
    category_idx = {s:i for i, s in enumerate(res['categories'])}
    res['data'] = [0]*nb_categories

    total = 0
    for data in table:
        if category_attr in data:
            category = data[category_attr]
            if category is not None:
                res['data'][category_idx[category]] += 1
                total                               += 1
    return res, total
    
def bar_data(table, category_attr, sort_attr, category_order_hint = None, sort_order_hint = None):
    """
    Data for displaying a bar graph. Each bar corresponds to a category,
    for each bar, the amount of values of each sort is stacked.
    returns {'sorts'     : [sort1, sort2, ...], 
             'categories : [cat1, cat2, ...],
             'data'      : [[nb_sort1_for_cat1, nb_sort1_for_cat2, ...],
                            [nb_sort2_for_cat1, nb_sort1_for_cat2, ...],
                            ...]}, total
    """
    res = {'sorts'      : get_values(table, sort_attr, sort_order_hint),
           'categories' : get_values(table, category_attr, category_order_hint),
           'data'       : []}
    nb_sorts      = len(res['sorts'])
    nb_categories = len(res['categories'])
    
    sort_idx     = {s:i for i, s in enumerate(res['sorts'])}
    category_idx = {s:i for i, s in enumerate(res['categories'])}
    for i in range(nb_sorts) :
        res['data'].append([0]*nb_categories)

    total = 0
    for data in table:
        if sort_attr not in data:
            print(f'Warning : bar_data : sorting attribute {sort_attr} is not in {data}')
        elif category_attr not in data:
            print(f'Warning : bar_data : category attribute {category_attr} is not in {data}')
        else:
            sort     = data[sort_attr]
            category = data[category_attr]
            if sort is not None and category is not None:
                res['data'][sort_idx[sort]][category_idx[category]] += 1
                total                                               += 1
                
    return res, total
    


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

    decode_sex = {'M': 'Male', 'F': 'Female'}

    print('Data\n\n')
    print(table)
    print()
    print('Values')
    print(get_values(table, 'Age'))
    print(get_values(table, 'Name'))
    print()
    print('Decode')
    print(decode_values(table, 'Sex', decode_sex))
    print()
    print('Make single')
    print(make_single(table, 'Age'))
    print(make_single(table, 'Sex'))
    print()
    print('Group values')
    print(group_values_dict_keep(table, 'Age', age_of))
    print(group_values_dict_keep(table, 'Name', country_of))
    print()
    print('Select in group')
    print(select_in_group(table, 'Age', [30, 50]))
    print()
    print('Pie')
    print(pie_data(table, 'Age'))
    print(pie_data(table, 'Sex'))
    print()
    print('Histo')
    print(histo_data(table, 'Age'))
    print()
    print('Bar')
    print(bar_data(table, 'Sex', 'Age'))

