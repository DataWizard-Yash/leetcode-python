class BubbleSort:
    def bubble_sort(self, l):
        n = len(l)
        for i in range(n):
            for j in range(0, n-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]

        return l


if __name__ == '__main__':
    b = BubbleSort()
    arr = list(map(int, input("Enter Elements").strip().split()))[:]
    print(b.bubble_sort(arr))

