class MinPriorityQueue {
    constructor() {
        this.heap = []
    }

    getParentIndex(index) {
        return Math.floor((index - 1) / 2)
    }

    getLeftChildIndex(index) {
        return 2 * index + 1
    }

    getRightChildIndex(index) {
        return 2 * index + 2
    }

    swap(i, j) {
        return [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
    }

    insert(value, priority) {
        const node = {value, priority}
        this.heap.push(node)
        this.bubbleUp()
    }

    // bubble up the element to order elements accordingly to priority
    bubbleUp() {
        let index = this.heap.length - 1
        while (index > 0 && this.heap[index].priority < this.heap[this.getParentIndex(index)].priority) {
            this.swap(index, this.getParentIndex(index))
            index = this.getParentIndex(index)
        }
    }

    extractMin() {
        if (this.heap.length === 0) {
            return null
        }
        if (this.heap.length === 1) {
            return this.heap.pop()
        }
        const min = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return min
    }

    bubbleDown() {
        let index = 0
        const length = this.heap.length

        while (true) {
            const leftChildIndex = this.getLeftChildIndex(index)
            const rightChildIndex = this.getRightChildIndex(index)
            let smallest = index

            if (leftChildIndex < length && this.heap[leftChildIndex].priority < this.heap[smallest].priority) {
                smallest = leftChildIndex
            }

            if (rightChildIndex < length && this.heap[rightChildIndex].priority < this.heap[smallest].priority) {
                smallest = rightChildIndex
            }

            if (smallest === index) break

            this.swap(index, smallest)
            index = smallest
        }
    }

    peek() {
        return this.heap.length === 0 ? null : this.heap[0]
    }
}

// Example Usage
const pq = new MinPriorityQueue();
pq.insert("Task A", 2);
pq.insert("Task B", 1);
pq.insert("Task C", 5);

console.log(pq.extractMin()); // { value: 'Task B', priority: 1 }
console.log(pq.peek());       // { value: 'Task A', priority: 2 }
console.log(pq.extractMin()); // { value: 'Task A', priority: 2 }
