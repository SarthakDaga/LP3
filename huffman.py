import heapq

chars = input("Enter characters separated by space: ").split()
freq = list(map(int, input("Enter frequencies: ").split()))

heap = [(freq[i], i, chars[i]) for i in range(len(chars))]
heapq.heapify(heap)

count = len(chars)

def display(node, code=""):
    if isinstance(node, str):
        print(node, ":", code)
    else:
        display(node[0], code + "0")
        display(node[1], code + "1")

while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)

    heapq.heappush(heap, (f1+f2, count, (left, right)))
    count += 1

display(heap[0][2])
