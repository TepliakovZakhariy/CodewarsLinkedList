def linked_list_from_string(s):
    lst=s.split(' -> ')[::-1]
    lst[0]=None
    for i, elem in enumerate(lst):
        if not i:
            continue
        elem=Node(int(elem),lst[i-1])
        lst[i]=elem
    return lst[-1]