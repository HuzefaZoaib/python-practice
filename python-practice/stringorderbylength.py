
lst = ['cat','tiger','lion']

def sort_by_length():
    _sorted = sorted(lst, key=len)
    print(_sorted)

if __name__ == '__main__':
    sort_by_length()

