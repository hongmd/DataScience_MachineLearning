'''
4.2 "Hello World" in CVXPY. 
Use CVXPY to verify the optimal values you obtained (analytically) for exercise 4.1 in Convex Optimization.

==================================

4.1 Consider the optimization problem

minimize    f₀(x₁, x₂)
subject to  2x₁ + x₂ ≥ 1
            x₁ + 3x₂ ≥ 1
            x₁ ≥ 0,    
            x₂ ≥ 0.

Make a sketch of the feasible set. For each of the following objective functions, 
give the optimal set and the optimal value.

(a)  f₀(x₁, x₂) = x₁ + x₂.
(b)  f₀(x₁, x₂) = -x₁ - x₂.
(c)  f₀(x₁, x₂) = x₁.
(d)  f₀(x₁, x₂) = max{x₁, x₂}.
(e)  f₀(x₁, x₂) = x₁² + 9x₂².
'''

import cvxpy as cp
import numpy as np

#--------------------------------
## Define the variables
#--------------------------------

x1 = cp.Variable()
x2 = cp.Variable()

#--------------------------------
## Define the constraints
#--------------------------------

# Normal way
opt_constraints = [
    -2*x1 - x2 <= -1, # 2x₁ + x₂ ≥ 1
    -x1 - 3*x2 <= -1, # x₁ + 3x₂ ≥ 1
    -x1 <= 0, # x₁ ≥ 0
    -x2 <= 0  # x₂ ≥ 0
]

# Matrix way
left_side = np.array([[-2, -1], # 4x2
                      [-1, -3],
                      [-1, 0],
                      [0, -1]])

variable_vector = cp.vstack([x1, x2]) # 2x1

right_side = [-1, -1, 0, 0]

opt_constraints_matrix = [
    left_side[i, :] @ variable_vector <= right_side[i]
    for i, _ in enumerate(right_side)
]

#-----------------------------------
## (a) f₀(x₁, x₂) = x₁ + x₂.
#-----------------------------------

# Define objective
objective_a = cp.Minimize(x1 + x2)

# Define problem: objective + constraints
problem_a = cp.Problem(
    objective = objective_a,
    constraints = opt_constraints
)

# Solve the problem
problem_a.solve()

print(f"Status: {problem_a.status}") # Status: optimal
print(f"Optimal Value: {problem_a.value}") # Optimal Value: 0.6000000001640435
print(f"Optimal variables: {x1.value, x2.value}") # Optimal variables: (array(0.4), array(0.2))


''''''''''''''''''''''''''''''''''''
''' Try with constraints matrix '''
''''''''''''''''''''''''''''''''''''

objective_a = cp.Minimize(x1 + x2)

problem_a_matrix = cp.Problem(
    objective = objective_a,
    constraints = opt_constraints_matrix
)

problem_a_matrix.solve()

print(problem_a_matrix.value) # 0.6000000001640435
print(x1.value, x2.value) # 0.4000000000142378 | 0.20000000014980568