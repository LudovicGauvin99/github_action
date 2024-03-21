values = (5, 6, 8, 1, 50, 32, 42, 51, 6, 8)

def job(table):
    if  (len(table) == 0):
        return 0

    total = 0
    for n in table:
        total += n

    return total / len(table)
