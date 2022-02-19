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
| interpolation_search(sorted_collection, item)                       | searches/interpolation_search.py | CCN3        | -                       | -                       | NLOC3        |
| cycle_sort(list)                                                    | sorts/cycle_sort.py              | 10          | -                       | -                       | 35           |
| Function5                                                           | Location5                        | CCN5        | CCN5man1                | CCN5man2                | NLOC5        |
| Function6                                                           | Location6                        | CCN6        | CCN6man1                | CCN6man2                | NLOC6        |
| Function7                                                           | Location7                        | CCN7        | CCN7man1                | CCN7man2                | NLOC7        |
| Function8                                                           | Location8                        | CCN8        | CCN8man1                | CCN8man2                | NLOC8        |

- **Did all methods (tools vs. manual count) get the same result?**
- **Are the results clear?**

2. **Are the functions just complex, or also long?**
3. **What is the purpose of the functions?**
4. **Are exceptions taken into account in the given measurements?**
5. **Is the documentation clear w.r.t. all the possible outcomes?**

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
