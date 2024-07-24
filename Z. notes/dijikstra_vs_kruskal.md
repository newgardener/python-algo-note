# dijikstra's vs kruskal's

|      Aspect      |                            Dijikstra's                            |                     Kruskal's                     |
|:----------------:|:-----------------------------------------------------------------:|:-------------------------------------------------:|
|     Purpose      | find the shortest path from a single source to all other vertices |                   find the MST                    |
|      Graph       |                          weighted graph                           |            weighted, undirected graph             |
|  Data Structure  |                         use PQ (min-heap)                         |                  use Union-Find                   |
|  Handle Cycles   |                     not concerned with cycles                     |               avoid creating cycles               |
| Time Complexity  |             O((V+E)logV) with heap, O(V^2) with array             | O(ElogE) or O(ElogV) because E can be at most V^2 |
| Space Complexity |                               O(V)                                |                       O(V)                        |
