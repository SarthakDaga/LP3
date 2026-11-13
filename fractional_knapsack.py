def knapsack(values, weights, W):
    items = sorted(zip(values, weights),
                   key=lambda x: x[0]/x[1], reverse=True)

    total = 0

    for value, weight in items:
        if W >= weight:
            total += value
            W -= weight
        else:
            total += value * W / weight
            break

    return total

n = int(input("Enter number of items: "))
values = list(map(int, input("Enter profits: ").split()))
weights = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter knapsack capacity: "))

print("Maximum Profit:", knapsack(values, weights, W))
