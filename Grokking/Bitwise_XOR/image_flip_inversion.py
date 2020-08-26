# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

def test(expected, output, msg):
    if expected == output:
        print ("Test Successful: %s" % msg)
    else:
        print ("Test Failed: %s" % msg)

def flip_inverse(mat):
    # Time Complexity = O(N), Space Complexity : O(1)
    # Horizontal flip impacts only column from the mid, while inversion is nothing but xor with 1
    dim = len(mat)
    for row in mat:
        for cell in range((dim+1)//2):
            row[cell], row[dim-cell-1] = row[dim-cell-1] ^ 1, row[cell] ^ 1

    return mat

def main():
    inp1 = [[1,0,1], [1,1,1], [0,1,1]]
    op1 = [[0,1,0], [0,0,0], [0,0,1]]
    test(op1, flip_inverse(inp1), "Test - 1")

main()
