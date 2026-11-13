N = 8
pos = [-1] * N

def safe(row, col):
    for i in range(row):
        if pos[i] == col or abs(pos[i]-col) == row-i:
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            pos[row] = col

            if solve(row+1):
                return True

            pos[row] = -1

    return False

first = int(input("Enter first queen column (0-7): "))
pos[0] = first

if solve(1):
    for i in range(N):
        for j in range(N):
            print("Q" if pos[i] == j else ".", end=" ")
        print()
else:
    print("No solution")
