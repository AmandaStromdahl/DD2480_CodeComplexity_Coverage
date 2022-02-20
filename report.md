# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: TheAlgorithms/Python

URL: [Link to Github repo](https://github.com/TheAlgorithms/Python)

The project implements many different algorithms in Python from various categories of algorithms. Some examples of included categories are graphs, boolean algebra and arithmetic analysis.

## Onboarding experience

Did it build and run as documented?

See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.

## Complexity

1. **What are your results for eight complex functions?**

The eight functions are presented in the table below. Every function has a CCN of 8 or higher with the Lizard tool, which is considered high complexity according to [this source](https://www.brandonsavage.net/code-complexity-and-clean-code/).

| Function                                                            | Location                         | CCN, Lizard | CCN, manual (Student 1) | CCN, manual (Student 2) | NLOC, Lizard |
| ------------------------------------------------------------------- | -------------------------------- | ----------- | ----------------------- | ----------------------- | ------------ |
| Dijkstra(graph, V, src)                                             | graphs/dijkstra_2.py             | 8           | -                       | -                       | 15           |
| random_graph(int vertices_number, float probability, bool directed) | graphs/random_graph_generator.py | 8           | -                       | -                       | 29           |
| interpolation_search(sorted_collection, item)                       | searches/interpolation_search.py | 10        | 6                       | -                       | 30        |
| cycle_sort(list)                                                    | sorts/cycle_sort.py              | 10          | 10                       | -                       | 35           |
| spiral_print(matrix)                                                           | matrix/spiral_print.py                        | 12        | 10                | -                | NLOC5        |
| Function6                                                           | Location6                        | CCN6        | CCN6man1                | CCN6man2                | NLOC6        |
| Function7                                                           | Location7                        | CCN7        | CCN7man1                | CCN7man2                | NLOC7        |
| Function8                                                           | Location8                        | CCN8        | CCN8man1                | CCN8man2                | NLOC8        |

- **Did all methods (tools vs. manual count) get the same result?**
- **Are the results clear?**

2. **Are the functions just complex, or also long?**
3. **What is the purpose of the functions?**
4. **Are exceptions taken into account in the given measurements?**
5. **Is the documentation clear w.r.t. all the possible outcomes?**

### <a id="interpolationSearch"></a>Interpolation Search ([file](complex_functions/interpolation_search.py))
This method aims to find the index of a value in a sorted list, or `None` if the value is not in the list. The documentation of the method is very clear about the parameters and the return values.<br>
The `lizard` tool gives this method a complexity (CCN) of 10. However, while computing it manually, we were surprised to obtain a complexity of 6 (9 decisions - 5 exits + 2) ! The detailed calculation of the manual CCN can be found in [this file](complex_functions/interpolation_search.py). After few hours of researching where does this difference come from, we realized that `lizard` does not make any difference between a *normal* statement and a `return` statement. Hence, the difference of 4 levels of complexity was coming from 4 `return` statements that `lizard` has considered as *normal* statements.<br>
Concerning the length of the function, it is not so long (30 LOC). Moreover, the number of exit points tends to reduce the complexity of the function, as we saw in the last paragraph.<br>

### Cycle Sort ([file](complex_functions/cycle_sort.py))
This method aims to sort a given list using an in-place but unstable sorting algorithm. There is no documentation about the method but we easily guess that the single final output is the sorted list.<br>
The `lizard` tool gives this method a complexity (CCN) of 10. We obtained exactly the same result when computing it manually (9 decisions - 1 exit + 2). The detailed calculation of the manual CCN can be found in [this file](complex_functions/cycle_sort.py).<br>
The method is quite short (21 LOC). The complexity comes from how the algorithm needs to be implemented, i.e. it needs 9 decision points.

### Spiral Print ([file](complex_functions/spiral_print.py))
This method is used to make a spiral print of a given squared matrix. The documentation just explain what the method does and what are the conditions for the input matrix. There is no explanation about the output of the code. However, we deduce that there is no `return` values since the purpose of the method is just to make a spiral print of a matrix.<br>
The `lizard` tool gives this method a complexity (CCN) of 12. However, with the manual analysis, we obtained a complexity of 10. We've exactly the same situation as for the [interpolation search](#interpolationSearch), i.e. `lizard` does not make the difference between *normal* statements and 'return' statements. Hence the difference of 2 levels of complexity comes from the 2 `return` statements (we do not count the final `return`) that `lizard` considers as *normal* statements.<br>
This method is not so long (25 LOC). The complexity comes mainly from the fact that we've to iterate a bunch of time on a specific `Iterable`.

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

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
