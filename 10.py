class MaxHeap:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self._heapify_up(parent)

    def delete(self):
        if not self.heap:
            print("Heap is empty!")
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self._heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def display(self):
        print("Heap:", self.heap)

h = MaxHeap()
n = int(input("Enter number of jobs to insert: "))
for _ in range(n):
    val = int(input("Enter priority: "))
    h.insert(val)
print("\nCurrent Heap:")
h.display()
print("\nPeek Max Priority:", h.peek())
print("\nDeleting Max Priority:", h.delete())
print("Heap after Deletion:")
h.display()
