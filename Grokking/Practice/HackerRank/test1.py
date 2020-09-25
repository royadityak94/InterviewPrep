import bisect

def find_preferential_index(arr, candidate):
    for idx in range(1, len(arr)-1):
        if ''.join(arr[idx-1:idx+2]) == candidate*3:
            return idx
        print ("Didn't match: ", arr[idx-1:idx+2])

    print ("Sending -1 for candidate: ", arr, candidate)
    return -1

def is_possible_deletion(colors, pattern):
    try:
        colors.index(pattern)
    except:
        return -1
    return 1

def auto_delete(colors, ptr1, ptr2):
    pattern1 = ptr1*3
    pattern2 = ptr2*3

    while is_possible_deletion(colors, pattern1) > 0:
        colors = colors.replace(pattern1, pattern1[:2])

    while is_possible_deletion(colors, pattern2) > 0:
        colors = colors.replace(pattern2, pattern2[:2])

    return colors

def gameWinner(colors):
    # Write your code here
    # players: Wendy and Bob
    players = ['wendy', 'bob']
    turn = [1, 0]
    ptr = 0
    new_colors = auto_delete(colors, players[0][0], players[1][0])
    print ("Pre-formatting: ", colors, " -> ", new_colors)
    colors = list(new_colors)

    while True:
        next_idx = find_preferential_index(colors, players[ptr][0])
        if next_idx == -1:
            return players[turn[ptr]]

        print (">>> ", next_idx, colors, ptr)
        del colors[next_idx]
        ptr = turn[ptr]

        print (">>> ", next_idx, colors[next_idx],)

        if len(colors) == 0:
            break

    return -1




def main():
    #print (encryptionValidity(100000, 100, [8, 4, 2, 2], ))
    print (gameWinner('wwwbbbbwww'))


main()
