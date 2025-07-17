'''

'''"""
================================================================================
CONVEX OPTIMIZATION PROBLEM STANDARD FORM
================================================================================

Standard Form Convex Optimization Problem

minimize f₀(x)
subject to fᵢ(x) ≤ 0,  i = 1, ..., m
          aᵢᵀx = bᵢ,  i = 1, ..., p

Key Requirements for Convexity:
- f₀, f₁, ..., fₘ are CONVEX functions
- Equality constraints are affine (linear functions)

Alternative Compact Form:
minimize f₀(x)
subject to fᵢ(x) ≤ 0,  i = 1, ..., m
          Ax = b

where A is an m×n matrix and b is an m-dimensional vector.

Quasiconvex Extension:
The problem is quasiconvex if f₀ is quasiconvex (and f₁, ..., fₘ remain convex).

Why This Form Matters:

1. Convex Feasible Set: The feasible set of a convex optimization problem is always convex. This is because:
   - Each constraint fᵢ(x) ≤ 0 defines a convex set (sublevel set of convex function)
   - Each equality constraint aᵢᵀx = bᵢ defines a convex set (hyperplane)
   - The intersection of convex sets is convex

2. Global Optimality: Any local minimum is guaranteed to be a global minimum for convex problems.

3. Efficient Algorithms: This standard form enables polynomial-time algorithms with convergence guarantees.

4. Duality Theory: The standard form provides a clean foundation for developing dual problems and strong duality results.

5. Practical Implementation: Most convex optimization solvers expect input in this standard form.

Important Property: The feasible set of a convex optimization problem is convex

This fundamental property ensures that:
- The problem has no "holes" or disconnected regions
- Line segments between any two feasible points remain feasible
- Gradient-based methods can navigate the feasible region efficiently
- The geometry supports powerful theoretical results

================================================================================
EXAMPLE
================================================================================

#######################
#### WRONG example ####
#######################
    minimize f₀(x) = x₁⁴ + x₂⁵
    subject to f₁(x) = x₁/(1 + x₂²) ≤ 0
            h₁(x) = (x₁ + x₂)² = 0

• f₀ is convex; feasible set {(x₁,x₂) | x₁ = -x₂ ≤ 0} is convex

• not a convex problem (according to our definition): f₁ is not convex, h₁ 
  is not affine

#######################
#### RIGHT example ####
#######################

Equivalent (but not identical) to the convex problem

    minimize x₁² + x₂²
    subject to x₁ ≤ 0 (this is a convex constraint)
               x₁ + x₂ = 0 (this is an affine constraint)

================================================================================
LOCAL AND GLOBAL OPTIMA
================================================================================

any locally optimal point of a convex problem is (globally) optimal

proof: suppose x is locally optimal, but there exists a feasible y with
f₀(y) < f₀(x)

x locally optimal means there is an R > 0 such that

z feasible, ||z - x||₂ ≤ R  ⟹  f₀(z) ≥ f₀(x)

consider z = θy + (1 - θ)x 
with θ = R/(2||y - x||₂)

• ||y - x||₂ > R, so 0 < θ < 1/2
• z is a convex combination of two feasible points, hence also feasible
• ||z - x||₂ = R/2 and

f₀(z) ≤ θf₀(y) + (1 - θ)f₀(x) < f₀(x)

which contradicts our assumption that x is locally optimal

================================================================================
"""
