# find-breakdown-Ex9
<img src="https://github.com/BarGoldman/find-breakdown-EX9/assets/93201414/72a4c4b9-fb7c-48d7-9e0e-dbc3dd94da14.png" width="100" height="100" />

### A question given to us as part of Assignment 9 in the course on Economic Algorithms
Decomposable Budget Programming:
Write a function that takes any budget and checks if it is decomposable, and if so, returns one decomposition of it.


we takes a list of `budget` amounts for certain issues and a list of `preferences` from various citizens on those issues. The function attempts to distribute the total budget among the issues based on the preferences of the citizens. It checks for three conditions:

1. The total allocated budget must match the specified budget for each issue.
2. Each citizen's allocation must sum to their equal share of the budget.
3. Allocations should only be made for the issues that each citizen supports.

The function operates as follows:

- **Initialization**: It calculates the total budget and the equal share for each citizen.
- **Support Calculation**: It computes the total number of citizens supporting each issue.
- **Allocation Calculation**: For each citizen, it identifies the issues with maximum support and allocates the equal share of the budget accordingly.
- **Verification**: Finally, it verifies if the allocations meet the three conditions mentioned.

