# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: TheAlgorithms/Python

URL: [Link to Github repo](https://github.com/TheAlgorithms/Python)

The project implements many different algorithms in Python from various categories of algorithms. Some examples of included categories are graphs, boolean algebra and arithmetic analysis.

## Onboarding experience

1. How easily can you build the project? Briefly describe if everything worked as documented or not:\
**(a).** Did you have to install a lot of additional tools to build the software?\
In order to utilize most of the functions presented in the library all that was needed was the python programming language. No specialized software was need to use the functions. This is primarily due to the fact that each function is a stand alone function that doesn't depend on large sections of other code and thus did not need a large build system to work. However, some algorithms are dependent on certain standard packages for machine learning and statistics. In total the entire library has 19 dependencies listed.

**(b).** Were those tools well documented?\
No large degree of documentation is needed for the project as a whole. The different algorithms however are indivudally documented with a short summary of their purpose and links to further reading. There was a substantial amount of documentation for contributors, specifying everything from coding style to how to write tests.

**(c).** Were other components installed automatically by the build script?\
There is no build script.

**(d).** Did the build conclude automatically without errors?\
See above.

**(e).** How well do examples and tests run on your system(s)?\
I've tried several algorithms and they seem to be working without issue. The project uses pytest for its testkit. This was not well described in the original repository but quite apparent given some of the top-level files in the repository. For a newcomer who has never used pytest before this could prove to be somewhat of a hinderance.

2. Do you plan to continue or choose another project?
We are planning to continue with this project as it is suitable for complexity analysis and refactoring.

## Complexity

1. **What are your results for eight complex functions?**

The eight functions are presented in the table below. Every function has a CCN of 8 or higher with the Lizard tool, which is considered high complexity according to [this source](https://www.brandonsavage.net/code-complexity-and-clean-code/).

| Function                                      | Location                                             | CCN, Lizard | CCN, manual (Student 1) | CCN, manual (Student 2) | NLOC, Lizard |
| --------------------------------------------- | ---------------------------------------------------- | ----------- | ----------------------- | ----------------------- | ------------ |
| dj_oracle(case, num_qubits)                   | quantum/deutsch_jozsa.py                             | 9           | 9                       | 9                       | 25           |
| strassen(matrix1, matrix2)                    | divide_and_conquer/strassen_matrix_multiplication.py | 12          | 10                      | 10                      | 39           |
| interpolation_search(sorted_collection, item) | searches/interpolation_search.py                     | 10          | 6                       | 6                       | 30           |
| cycle_sort(list)                              | sorts/cycle_sort.py                                  | 10          | 10                      | 10                      | 35           |
| spiral_print(matrix)                          | matrix/spiral_print.py                               | 12          | 10                      | 10                      | NLOC5        |
| simulated_annealing(search)                   | searches/simulated_annealing.py                      | 16          | 16                | 16                | 79        |
| hill_climber(search_prob)                     | searches/hill_climber.py                             | 16          | 16                      | 16                      | 68           |
| next_generation(cells)                        | cellular_automata                                    | 19          | 19                      | 19                      | 38           |

- **Did all methods (tools vs. manual count) get the same result?**
- **Are the results clear?**

1. **Are the functions just complex, or also long?**
2. **What is the purpose of the functions?**
3. **Are exceptions taken into account in the given measurements?**
4. **Is the documentation clear w.r.t. all the possible outcomes?**

### <a id="dj_oracle"></a>Deutsch Jozsa ([file](complex_functions/deutsch_jozsa.py))

The Deutsch-Jozsa problem features an oracle function that takes an n-bit input and outputs 0 or 1. The function is either constant (returns a constant value) or balanced (meaning it returns 0 half of the time and 1 the rest of the time). The purpose of the examined method is to create a Quantum Circuit (a model) of an oracle function which is either balanced or constant depending on the parameter `case`, and that handles `num_qubits`-bit input values.

The function handles multiple cases and needs to iterate through `num_qubits` when setting the output values for the model. At the same time, the only way to exit the function is to return the model. This is why the cyclomatic complexity is so high. The documentation is clear about the only possible outcome of the function, which is to return the model. There are no exceptions or alternative return values.

Compared to the high cyclomatic complexity, the function has relatively few lines (only 25 according to Lizard). This is because the branches are quite dense and there is only one `return` statement. Lizard's cyclomatic complexity also aligns with both of the manual complexity calculations. This is not surprising since the function is relatively straightforward in terms of complexity; there are no exceptions or logical `&&` or `||`.

### <a id="strassen"></a>Strassen ([file](complex_functions/strassen.py))

The purpose of this method is to perform a matrix multiplication of two given matrices using the Strassen algorithm. This task requires checking that the dimensions of the matrices are compatible and using nested loops to iterate through the values in the matrices. That, in turn, causes a high complexity.

Lizard's complexity evaluation differs from the manual evaluations by 2 (both manual evaluations yielded the same results). Part of the reason for this could be that Lizard does not consider exceptions to be exits. If exceptions are included in the calculations as exit points, the function is deemed less complex.

The number of code lines is relatively small compared to the high complexity. This is because the function is quite dense in terms of nested loops and if-statements.

There is very little documentation describing the function. The exception and the last `return` statement are self-explanatory, but the first `return` statement requires some description.

### <a id="interpolationSearch"></a>Interpolation Search ([file](complex_functions/interpolation_search.py))

This method aims to find the index of a value in a sorted list, or `None` if the value is not in the list. The documentation of the method is very clear about the parameters and the return values.<br>
The `lizard` tool gives this method a complexity (CCN) of 10. However, while computing it manually, we were surprised to obtain a complexity of 6 (9 decisions - 5 exits + 2) ! The detailed calculation of the manual CCN can be found in [this file](complex_functions/interpolation_search.py). After few hours of researching where does this difference come from, we realized that `lizard` does not make any difference between a _normal_ statement and a `return` statement. Hence, the difference of 4 levels of complexity was coming from 4 `return` statements that `lizard` has considered as _normal_ statements.<br>
Concerning the length of the function, it is not so long (30 LOC). Moreover, the number of exit points tends to reduce the complexity of the function, as we saw in the last paragraph.<br>

### Cycle Sort ([file](complex_functions/cycle_sort.py))

This method aims to sort a given list using an in-place but unstable sorting algorithm. There is no documentation about the method but we easily guess that the single final output is the sorted list.<br>
The `lizard` tool gives this method a complexity (CCN) of 10. We obtained exactly the same result when computing it manually (9 decisions - 1 exit + 2). The detailed calculation of the manual CCN can be found in [this file](complex_functions/cycle_sort.py).<br>
The method is quite short (21 LOC). The complexity comes from how the algorithm needs to be implemented, i.e. it needs 9 decision points.

### Spiral Print ([file](complex_functions/spiral_print.py))

This method is used to make a spiral print of a given squared matrix. The documentation just explain what the method does and what are the conditions for the input matrix. There is no explanation about the output of the code. However, we deduce that there is no `return` values since the purpose of the method is just to make a spiral print of a matrix.<br>
The `lizard` tool gives this method a complexity (CCN) of 12. However, with the manual analysis, we obtained a complexity of 10. We've exactly the same situation as for the [interpolation search](#interpolationSearch), i.e. `lizard` does not make the difference between _normal_ statements and 'return' statements. Hence the difference of 2 levels of complexity comes from the 2 `return` statements (we do not count the final `return`) that `lizard` considers as _normal_ statements.<br>
This method is not so long (25 LOC). The complexity comes mainly from the fact that we've to iterate a bunch of time on a specific `Iterable`.

### Simulated Annealing ([file](complex_functions/simulated_annealing.py))

The simulated annealing method aims to find a global optimum for a given function. It avoid getting stuck in local optima by having a "temperature" variable that controls the degree of randomness that impacts the choices of the algorithm. The function has a high measured complexity by Lizard (CCN = 16) but is not overly long as it consists of 79 lines. Manual counting of the complexity gives a complexity of 16. The majority of the complexity in this function comes from the fact that the simulated annealing algorithm demands a certain degree of complexity, but also slightly from the coding style.

### Hill Climber ([file](complex_functions/hill_climber.py))
This function implements the **Hill Climber** heuristic for optimization of search problems. The documentation explains the general idea of the algorithm that it is implementing, that is that we start in a state in the search tree and move to neighboring states that provide maximum or minimum change. The documentation (which is the function docstring) also details the input parameters to the function. There are total 8 input parameters which of 7 are optional (in the table above the only required parameter is listed for brevity). As the algorithm is essentially a simulation there are a bunch of "knobs" that can be tweaked, like the bounds and depth of the simulation. The function makes use of a general interface for search problems implemented as a class called `SearchProblem`. The function takes in an instance of `SearchProblem` which is a representation of the initial state, and returns an instance of `SearchProblem` as a representation of the final state.

Despite being a relatively simple algorithmic idea, the implementation is quite complex with regard to CNN. The reason for the high complexity (16) is the high density of `if` statements, which are needed both for error handling (checking bounds for instance), applying logic specified by the optional parameters (plotting the results for instance) and the main logic of checking values of states. The reason for identical `lizard` and manual scores is the fact that there is a single `return` statement of the function, so the difference of modeling cyclomatic complexity does not matter.

### Conway's Game of Life ([file](complex_functions/conways_game_of_life.py))
The function we are interested in is called `new_generation` and it performs a single iteration of **Conway's Game of Life**, which is an implementation of a **cellular automata**. It is a simulation that is only influenced by its initial value which is run of a grid of cells that can either be **on** or **off**. I each iteration, the state of every cell is updated simultaneously in accordance to a set of rules. 

The documentation is quite sparse, it only covers the overall purpose of the function, that it generates a new generation of *Conway's Game of Life* along with a simple usage example. The single parameter is not documented, but described well by the type-annotation and its name. There is also a recounting of the rules of *Conways's Game of Life* later in the code as a comment.

Once again the complexity is high (19) due to many `if` statements. The main source of cyclomatic complexity is the need for checking the boundaries of the grid, which has to be done for 8 distinct cells for each cell in the grid. The `lizard` tool and out own manual calculations of the CNN are identical as there is only one exit point of the function so the difference of modelling cyclomatic complexity does not matter.

## Refactoring

### <a id="dj_oracle"></a>Deutsch Jozsa ([file](refactored_functions/deutsch_jozsa.py))

A simple way to reduce the cyclomatic complexity of dj_oracle() is to move a complex block of code into a helper function. Seeing as dj_oracle() handles two cases (constant and balanced) and the latter of them is rather complex, this case can be moved to a separate function `H()`. `H()` would be called once from dj_oracle() and would return a Quantum Circuit (a model) of the balanced oracle function.

A possible drawback is that the code might become less readable, as it would require the programmer to jump between functions when analysing the code.

The refactoring was carried out in [this file](refactored_functions/deutsch_jozsa.py) and the cyclomatic complexity was reduced from 9 to 4 according to Lizard.

### <a id="strassen_refactored"></a>Strassen ([file](refactored_functions/strassen.py))

Parts of the strassen() function could be moved to helper functions to reduce complexity. Two examples of such parts are the appending of zeros to the matrices `matrix1` and `matrix2`, as well as the removal of additional zeros in `final_matrix`. These code snippets could be moved to helper functions `F()` and `H()`, which would require `F()` to be called twice and `H()` to be called once from strassen(). Both of these helper functions would return a modified matrix.

Depending on how this type of refactoring is executed, `matrix1` and `matrix2` would not necessarily share the same loop in `F()`. This could affect the efficiency negatively, but at the same time the cyclomatic complexity would be reduced and the program would be easier to understand.

The refactoring was carried out in [this file](refactored_functions/strassen.py) and the cyclomatic complexity was reduced from 12 to 4 according to Lizard.

### <a id="cycleSort_refactored"></a>Cycle Sort ([file](refactored_functions/cycle_sort.py))

The first thing to note in this method is that a lot of code snippets are repeated in the [original version](complex_functions/cycle_sort.py):
- LOC 15-20 and 33-38: these lines can be moved into a new function called `find_pos()`. The purpose of this method is to find in which position to place the `item` value in the array;
- LOC 27-30 and 41-44: these lines can also be moved into a new function called `place_item()`. Its purpose is to place the given `item` in the position found by the `find_pos()` function. Note that the while is here to place the `item` after possible duplicates if any.

Finally, we notice that the `while` statement line 32 is there to repeat to sequence of finding position for a given `item` (using `find_pos()`) and place it there (using `place_item()`). We can move this cycle into a new function called `do_cycle()` which will execute this procedure.

With all these changes, and according to `lizard`, we managed to reduce the cyclomatic complexity of `cycle_sort()` from 10 to 3 ! Which is a reduction of 70%. Detailed calculations can be found in [this file](refactored_functions/cycle_sort.py).

One advantage of this refactoring is that, with the call of the new functions, the algorithm should be easier to understand. However, for someone who want to read the code, it would be a bit annoying to jump from function to function to read the whole code.


### Conway's Game of Life ([file](refactored_functions/conways_game_of_life.py))


The function we are refactoring is `new_generation`. We start of by identify the areas we can improve upon. The outer two `for` loops cannot really be avoided. However, the following code snippet that counts the active neighbours can be improved upon.

```python
 ...
if i > 0 and j > 0:
    neighbour_count += cells[i - 1][j - 1]
if i > 0:
    neighbour_count += cells[i - 1][j]
if i > 0 and j < len(cells[i]) - 1:
    neighbour_count += cells[i - 1][j + 1]
if j > 0:
    neighbour_count += cells[i][j - 1]
if j < len(cells[i]) - 1:
    neighbour_count += cells[i][j + 1]
if i < len(cells) - 1 and j > 0:
    neighbour_count += cells[i + 1][j - 1]
if i < len(cells) - 1:
    neighbour_count += cells[i + 1][j]
if i < len(cells) - 1 and j < len(cells[i]) - 1:
    neighbour_count += cells[i + 1][j + 1]
 ...
```

The obvious solution is to extract this sequence into a helper function `active_neighbours(cells, i, j)`. This has pretty dramatic improvement of the cyclomatic complexity, the CNN of `new_generation` drops from 19 to 7 and the NLOC drops from 38 to 22. This refactor also have the two-fold benefit of improving the readability of the function. When you think about it the crux of the `new_generation` function is to apply the rules for each cell, the number of active neighbours is merely a dependency of the rules so it makes sense that it should be a separate function.

Although a good start, this refactor is very surface level. We have not actually solved the complexity issue by extracting this logic to a helper function, we just moved it a bit out of sight. Actually we have increased the total CCN to 20 from 19 (`active_neighbors` have a CCN of 13 and `next_generation` have a CCN of 7). The code is way to explicit, we check each of the 8 surrounding cells with an individual `if` statement. To reduce the complexity we want to loop over the different cells instead of checking each one-by-one. We accomplish this by looping over a set of offsets (`dx`, `dy`) in the `x` and `y` direction. The result is:

```python
def active_neighbours(cells, x, y):
    neighbour_count = 0

    # loop over offsets
    for (dx, dy) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, -1),
    ]:
        if x + dx < 0 or x + dx > len(cells[x]) - 1:
            continue
        if y + dy < 0 or y + dy > len(cells) - 1:
            continue
        neighbour_count += cells[y + dy][x + dx]
    return neighbour_count
```
> Note: variables `i` and `j` have been renamed to `y` and `x`.

This change brings the down the CCN of `active_neighbours` from 13 to 6, which is a good improvement, and the solution is much more elegant.

The last area of improvement is the code that applies the rules, currently it looks like this:

```python
...

alive = cells[y][x] == 1
if (
    (alive and 2 <= neighbour_count <= 3)
    or not alive
    and neighbour_count == 3
):
    next_generation_row.append(1)
else:
    next_generation_row.append(0)

...
```

A good idea in this scenario is to extract the condition in the `if` statement out to a function with a good name, like `cell_should_be_on(alive, neighbour_count)`. This improves readability at a glance, and will reduce the CCN of the `new_generation` function. The end result will then be,

```python
def cell_should_be_on(alive, neighbour_count):
    return (alive and 2 <= neighbour_count <= 3) or not alive and neighbour_count == 3
    

def new_generation(cells):

...

alive = cells[y][x] == 1
if cell_should_be_on(alive, neighbour_count):
    next_generation_row.append(1)
else:
    next_generation_row.append(0)
...
```

This change brings down the CCN of `new_generation` to 4, approximately a 79% decrease from the original CCN of 19. Although the total CCN of all functions is 14 (6 + 4 + 4) we have managed to refactor this function into very digestible chunks. From a readability perspective it is also very improved, as you can easily spot the main steps at a glance. Although someone who reads this function would have to "jump around" a bit to understand every detail, but you have the opportunity to unravel the necessary details on demand instead of trying to understand everything at once.



### <a id="simulated_annealing"></a>Simulated Annealing ([file](refactored_functions/simulated_annealing.py))

The simulated annealing function contains a lot of conditionals that drives up the cyclomatic complexity. Large chunks of conditionals can result in the code being more difficult to read. The most obvious way to decrease the complexity was to move some of the more obtuse conditional chains to separate helper functions. This should improve the readability of the code. 

The refactored version of the code can be found in [this file](refactored_functions/simulated_annealing.py). Lizard now rates the complexity as 10 and manual analysis gives a complexity of 10 (9+2-1). This corresponds to a complexity reduction of ~33%.

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
