A, B, D, K, T = map(int, input().split())

def make_table(A, B, D, K, T):
    # table : dict, table[date] = dict{employee: working periods}

    from collections import defaultdict

    one = [1, 3, 5, 7, 8, 10, 12]
    zero = [4, 6, 9, 11]

    table = {}
    for _ in range(D):
        table[(A, B)] = defaultdict(list)
        if A in one:
            if B + 1 > 31:
                A += 1
                B = 0
        elif A in zero:
            if B + 1 > 30:
                A += 1
                B = 0
        else:
            if B + 1 > 28:
                A += 1
                B = 0
        B += 1
    return table



def submit(table):
    id = input()
    S = int(input())
    dates = list(input().split())
    dates = [dates[idx] + ' ' + dates[idx+1] for idx in range(len(dates)-1)]
    #example: dates = ['01/31 09:00-12:00', '02/01 10:00-12:00', '02/02 08:00-10:00']
    if len(dates) != S:
        return 'wrong format'
    for date_key in table:
        for id in table[date_key]:
            table[date_key][id] = []
    for date in dates:
        month, day = int(date[:1]), int(date[2:4])
        s_time, s_min = int(date[6:8]), int(date[9:11])
        e_time, e_min = int(date[12:14]), int(date[15:17])
        if len(table[date]) < K:
            if e_time <= s_time:
                table[(month, day)][id].append((s_time, s_min, 0, 0))
                if (month, day+1) in table:
                    table[(month, day+1)][id].append((0, 0, e_time, e_min))
                else:
                    table[(month+1, 1)][id].append((0, 0, e_time, e_min))


def salary(id):
    id = input()
    salary = 0
    for date_key in table:
        s_time, s_min, e_time, e_min = table[date_key][id][0]
        if s_time >=4 and e_time < 22:
            salary += ((e_time*60+e_min) - (s_time*60+s_min))*900/60
        else:
