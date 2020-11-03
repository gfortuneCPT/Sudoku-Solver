# Sudoku Solver

> Backtracking Algorithm

> Solves Easy - Hard Puzzles

> #SudokuSolver, #Python, #Backtracking

## Table of Contents (Optional)

> If your `README` has a lot of info, section headers might be nice.

- [Usage](#Usage)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## Usage 

- Enter puzzle row by row, space seperated and use '0' for blank spaces.
```python
#Bactrack Implementation
def solve ():
        for y in range(9):
            for x in range(9):
                    if grid[y][x] == 0:
                        for n in range(1,10):
                            if check(y,x,n):
                                grid[y][x] = n
                                solve()
                                grid[y][x] = 0
                        return
        printgrid(grid)
#row by row grid
row = 9
grid = []
```

### Clone

- Clone this repo to your local machine using `https://github.com/grantf28/SudokuSolver/`

---

## Tests
- Tested With sudoku.com Easy - Hard Puzzles.
- Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree). 

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/joanaz/HireDot2.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/grantf28/SudokuSolver/pulls" target="_blank">`https://github.com/grantf28/SudokuSolver/pulls`</a>.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://www.grantf.co.za" target="_blank">Grantf28 </a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://www.grantf.co.za" target="_blank">Grantf28 </a>.