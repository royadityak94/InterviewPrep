# Source: https://www.hackerrank.com/challenges/luck-balance/problem

def luckBalance(k, contests):
    # Sorting based on important events, and ascending prizes
    contests.sort(key=lambda x: (x[1], x[0]), reverse=True)
    luck = 0

    for event_luck, event_rating in contests:
        print (event_luck, event_rating, luck, k)
        if k or not event_rating:
            luck += event_luck
            k -= 1
        else:
            luck -= event_luck

    return luck



if __name__ == '__main__':
    print (luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
