## DSA Practice
Coding problems based on DSA for AI with one file per problem with patterns and complexity.

---

## Complexity Analysis

### Arrays and Lists

| Operation | Array | Python List |
|---|---|---|
| Traversal | O(n) | O(n) |
| Insertion/Deletion at the end | O(1) | O(1) Amortised |
| Insertion/Deletion at an arbitary position | O(n) | O(n) |
| Accessing/Indexing | O(1) | O(1) |
| Searching | O(n) | O(n) |
| Updating | O(1) | O(1) |
| Sorting | O(n log n) | O(n log n) |
| Merging | O(n + m) | O(n + m) |
| Splitting | O(n) | O(n) |

---

### Strings

| Operation | Complexity |
|---|---|
| Accessing/Indexing | O(1) |
| Length | O(1) |
| Concatenation | O(n + m) |
| Slicing | O(k) |
| Substring Search | O(n * m) |
| Joining/Merging | O(length) |

---

### Linked Lists

| Operation | SLL | CSLL | DLL | CDLL |
|---|---|---|---|---|
| Insert at beginning | O(1) | O(n) | O(1) | O(1) |
| Insert at end | O(n)| O(n) | O(1) | O(1) |
| Insert at position | O(n) | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) | O(n) |
| Delete at beginning | O(1) | O(n) | O(1) | O(1) |
| Delete at end | O(n) | O(n) | O(1) | O(1) |
| Delete at position | O(n) | O(n) | O(n) | O(n) |
| Space per node | O(1) | O(1) | O(1) | O(1) |

---

### Stacks

| Operation | Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| isEmpty | O(1) |
| Space per Node | O(n) |

1. The doubly-linked variants get O(1) at both ends because prev and tail pointers remove the traversal adding an extra pointer per node of the linked list.
2. Circular singly linked list is the worst among both: O(n) at the beginning and the end, it is because there's no None value to stop and no prev pointer to step back.
3. The maintained counters and the tail references aren't free in a second way meaning they're the invariants which every method has to update, and getting it wrong produces silently wrong answers rather than crashes.

---

