# A* shortest path through multiple points
Given an N*N grid with N alphabetically-ordered stops, find the shortest path that passes through each point without intersecting itself.

# Results
Given the starting grid:
```python
grid = Grid(10)
grid.add_stop((1, 1), 'A')
grid.add_stop((5, 3), 'B')
grid.add_stop((2, 8), 'C')
grid.add_stop((4, 1), 'D')

0 0 0 0 0 0 0 0 0 0 
0 A 0 0 D 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 B 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 C 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
```

The following grid shows the solution:
```python
0 0 0 0 0 0 0 0 0 0 
0 X X X D X X 0 0 0 
0 0 0 X X X X 0 0 0 
0 0 0 0 0 X X 0 0 0 
0 0 0 0 X X X 0 0 0 
0 0 0 X X X X 0 0 0 
0 0 0 X 0 X 0 0 0 0 
0 0 X X X X 0 0 0 0 
0 0 X X X 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
```

Which took the path:
```python
[['e', 'e', 's', 'e', 'e', 's'], ['s', 'w', 's', 'w', 's', 's', 'w', 's'], ['e', 'e', 'n', 'e', 'n', 'n', 'e', 'n', 'n', 'n', 'n', 'w', 'w']]
```

![Solution Path](https://nathanaburgess.com/images/astar_solution.png)
