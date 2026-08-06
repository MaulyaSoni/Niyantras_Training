import sys

def high_and_low(records):
    t_max = 0
    res = sys.maxsize
    for row in records:
        amt = int(row.Total_Amount)

        t_max = max(t_max ,amt)
        res = res if res < amt else amt

    return t_max , res