'''
================================================================================

LIST OF COMMON CONVEX OPTIMIZATION PROBLEM TYPES

================================================================================

- Linear Programming (LP)
- Linear-fractional program
- Robust Linear Programming (RLP)
- Stochastic Robust Linear Programming
- Quadratic Programming (QP)
- Quadratically Constrained Quadratic Programming (QCQP)
- Second-Order Cone Programming (SOCP)
- Deterministic Robust LP via SOCP
- Stochastic Robust LP via SOCP
- Geometric Programming (GP)
- Geometric program in convex form
- Convex optimization with generalized inequality constraints
- Semidefinite Programming (SDP)
- LP and SOCP as SDP
- Vector optimization

================================================================================
'''

#################################################################################

'''
================================================================================
LINEAR PROGRAMMING (LP)
================================================================================
Linear programming involves optimizing a linear objective function 
subject to linear equality and inequality constraints. 

It can be expressed in standard form as:

Problem:
    minimize    cᵀx + d
    subject to  Gx ≼ h
                Ax = b

Notes:
    - convex problem with affine objective and constraint functions
    - feasible set is a polyhedron

Brief explanations:
    - Linear objective function ensures constant rate of change (no curvature)
    - All constraints are linear, forming hyperplanes that intersect to create polyhedra
    - Optimal solution always occurs at vertices (extreme points) of the feasible region
    - Simplex method traverses vertices to find optimal solution in finite steps
    - Interior-point methods approach optimum through the interior of feasible region
    - Strong duality holds: primal and dual optimal values are equal (if finite)
    - Can be solved in polynomial time using interior-point algorithms
    - Widely applicable: resource allocation, transportation, production planning
    - Forms the foundation for more complex optimization problems (IP, QP, SDP)
    - Degeneracy occurs when multiple constraints are active at optimal vertex
    - Unbounded problems have no finite optimal value in the objective direction


================================================================================
Linear-fractional program
================================================================================

Problem:
    f₀(x) = (cᵀx + d)/(eᵀx + f),    dom f₀(x) = {x | eᵀx + f > 0}

Properties:
    - a quasiconvex optimization problem; can be solved by bisection
    - also equivalent to the LP (variables y, z)

Equivalent LP formulation:
    minimize    cᵀy + dz
    subject to  Gy ≼ hz
                Ay = bz
                eᵀy + fz = 1
                z ≥ 0

Brief explanations:
    - The objective function is a ratio of two affine functions, making it quasiconvex
    - Quasiconvexity means sublevel sets are convex, enabling efficient bisection methods
    - The bisection algorithm repeatedly solves convex feasibility problems to find optimal value
    - The equivalent LP uses a change of variables: y = x/(eᵀx + f), z = 1/(eᵀx + f)
    - This transformation converts the fractional problem to a standard linear program
    - The constraint eᵀy + fz = 1 normalizes the denominator to unity
    - Both formulations have the same optimal value and solution structure

=================================================================================
Robust Linear Programming (RLP)
=================================================================================

Description:
Optimization parameters often have uncertainty (e.g., in an LP, c, aᵢ, bᵢ are uncertain). 

Two common models handle uncertainty in aᵢ:

----------------------------------------------
Deterministic (worst-case) model:
Problem:
    minimize    cᵀx
    subject to  aᵢᵀx ≤ bᵢ   for all aᵢ ∈ Εᵢ, i = 1,…,m

Brief explanations:
    - Ensures constraints hold under every possible realization of aᵢ in the uncertainty set Εᵢ  
    - Converts to a convex problem if Εᵢ is a convex set (e.g., ellipsoid or polyhedron)  
    - Yields solutions that are immune to worst-case data variations  

----------------------------------------------
Stochastic (chance-constrained) model:
Problem:
    minimize    cᵀx
    subject to  Prob(aᵢᵀx ≤ bᵢ) ≥ η, i = 1,…,m

Brief explanations:
    - aᵢ is treated as a random variable with known distribution  
    - Constraints must be satisfied with confidence level η (e.g., 95%)  
    - Often approximated or relaxed to tractable convex constraints (e.g., using Chebyshev or scenario approaches)  
    - Balances risk and performance by allowing small probability of constraint violation  

'''

#################################################################################

'''
================================================================================
QUADRATIC PROGRAMMING (QP)
================================================================================

Problem:
    minimize    (1/2)xᵀPx + qᵀx + r
    subject to  Gx ≼ h
                Ax = b

Properties:
    - P ∈ S₊ⁿ, so objective is convex quadratic
    - minimize a convex quadratic function over a polyhedron

Brief explanations:
    - The matrix P must be positive semidefinite (P ⪰ 0) for convexity
    - Positive semidefinite means xᵀPx ≥ 0 for all vectors x
    - This ensures the objective function has a single global minimum (no local minima)
    - The feasible region is still a polyhedron defined by linear constraints
    - Can be solved efficiently using interior-point methods or active-set methods
    - Interior-point methods have polynomial-time complexity: O(n³L) operations
    - When P = 0, the problem reduces to a linear program (LP)
    - The quadratic term (1/2)xᵀPx represents curvature in the objective function
    - Applications include portfolio optimization, machine learning, and control theory
    - KKT conditions provide necessary and sufficient optimality conditions for convex QPs

================================================================================
QUADRATICALLY CONSTRAINED QUADRATIC PROGRAMMING (QCQP)
================================================================================

Problem:
    minimize    (1/2)xᵀP₀x + q₀ᵀx + r₀
    subject to  (1/2)xᵀPᵢx + qᵢᵀx + rᵢ ≤ 0,    i = 1,...,m
                Ax = b

Properties:
    - Pᵢ ∈ S₊ⁿ: objective and constraints are convex quadratic
    - if P₁,...,Pₘ ∈ S₊ⁿ, feasible region is intersection of m ellipsoids and 
      an affine set

Brief explanations:
    - Extension of QP where constraints are also quadratic instead of just linear
    - Convexity requires ALL matrices P₀, P₁,..., Pₘ to be positive semidefinite
    - When convex, feasible region is intersection of ellipsoidal sets and hyperplanes
    - Each quadratic constraint (1/2)xᵀPᵢx + qᵢᵀx + rᵢ ≤ 0 defines an ellipsoid
    - Convex QCQP can be solved efficiently using interior-point methods
    - Non-convex QCQP is NP-hard in general (includes binary quadratic programming)
    - Common relaxation technique: Shor's semidefinite programming (SDP) relaxation
    - SDP relaxation provides lower bounds by lifting to matrix variable X = xxᵀ
    - Applications: portfolio optimization, robust optimization, signal processing
    - Can model problems with uncertainty and risk through quadratic constraints
    - Special cases include trust region subproblems and least squares with constraints
'''

#################################################################################

'''
================================================================================
SECOND-ORDER CONE PROGRAMMING (SOCP)
================================================================================

Problem:
    minimize    fᵀx
    subject to  ‖Aᵢx + bᵢ‖₂ ≤ cᵢᵀx + dᵢ,    i = 1,...,m
                Fx = g

(Aᵢ ∈ ℝⁿⁱˣⁿ, F ∈ ℝᵖˣⁿ)

Properties:
    - inequalities are called second-order cone (SOC) constraints:
      (Aᵢx + bᵢ, cᵢᵀx + dᵢ) ∈ second-order cone in ℝⁿⁱ⁺¹
    - for nᵢ = 0, reduces to an LP; if cᵢ = 0, reduces to a QCQP
    - more general than QCQP and LP

Brief explanations:
    - Each SOC constraint defines a convex cone: {(u,t) | ‖u‖₂ ≤ t} in ℝⁿⁱ⁺¹
    - The feasible region is intersection of multiple cones with an affine subspace
    - SOC constraints generalize linear constraints (when nᵢ = 0) and quadratic constraints
    - Convex optimization problem solvable by interior-point methods with polynomial complexity
    - Efficient primal-dual algorithms achieve O(√n log(1/ε)) iteration complexity
    - Can represent many practical constraints: robust optimization, norm minimization
    - Special case of semidefinite programming (SDP) but computationally more efficient
    - Applications include portfolio optimization, robust linear programming, filter design
    - When cᵢ = 0, constraint becomes ‖Aᵢx + bᵢ‖₂ ≤ dᵢ (simple norm bound)
    - Bridges the gap between linear programming (simple) and semidefinite programming (general)
    - Can model sum-of-norms objectives and max-of-norms constraints efficiently

    
================================================================================
Deterministic robust LP via SOCP
================================================================================

Uncertainty set (ellipsoidal):
    Εᵢ = {āᵢ + Pᵢu  |  ‖u‖₂ ≤ 1}    (āᵢ ∈ ℝⁿ, Pᵢ ∈ ℝⁿˣⁿ)

Original robust LP:
    minimize    cᵀx
    subject to  aᵢᵀx ≤ bᵢ   ∀ aᵢ ∈ Εᵢ,    i = 1,…,m

Equivalent SOCP:
    minimize    cᵀx
    subject to  āᵢᵀx + ‖Pᵢᵀx‖₂ ≤ bᵢ,    i = 1,…,m

Brief explanations:
    - Ellipsoid Εᵢ captures uncertainty around nominal āᵢ with shape Pᵢ  
    - Worst-case constraint sup₍‖u‖₂≤1₎(āᵢ + Pᵢu)ᵀx = āᵢᵀx + ‖Pᵢᵀx‖₂  
    - Reformulates infinite constraints into m convex SOC constraints  
    - SOCP can be solved efficiently with interior-point methods  
    - Robust solution x is safeguarded against all aᵢ within ellipsoids  
    - Trade-off between robustness and conservatism controlled by Pᵢ  

================================================================================
Stochastic robust LP via SOCP
================================================================================

Assumptions:
    aᵢ ~ 𝒩(āᵢ, Σᵢ)  
    ⇒ aᵢᵀx ~ 𝒩(āᵢᵀx, xᵀΣᵢx)  

Chance-constrained robust LP:
    minimize    cᵀx  
    subject to  Prob(aᵢᵀx ≤ bᵢ) ≥ η,    i = 1,…,m  

Probability expression:
    Prob(aᵢᵀx ≤ bᵢ) = Φ( (bᵢ - āᵢᵀx) / ‖Σᵢ¹ᐟ² x‖₂ )  
    where Φ(t) = (1/√(2π)) ∫₋∞ᵗ e^(-u²/2) du  

Equivalent SOCP (η ≥ ½):
    minimize    cᵀx  
    subject to  āᵢᵀx + Φ⁻¹(η) ‖Σᵢ¹ᐟ² x‖₂ ≤ bᵢ,    i = 1,…,m  

Brief explanations:
    - Φ⁻¹(η) is the Gaussian quantile for confidence level η  
    - Reformulates chance constraint into a single SOC constraint per i  
    - Ensures constraint holds with at least probability η  
    - Higher η ⇒ more conservative (larger Φ⁻¹(η))  
    - Solvable efficiently by interior-point SOCP solvers  
    - Balances risk (violation probability) against optimality  
'''

##################################################################################

'''
================================================================================
Geometric Programming (GP)
================================================================================

Definitions:
    Monomial function:
        f(x) = c·x₁ᵃ¹ x₂ᵃ² … xₙᵃⁿ,    dom f = ℝ₊₊ⁿ
        with c > 0; exponents aᵢ can be any real number
    Posynomial function:
        f(x) = ∑ₖ₌₁ᴷ cₖ·x₁ᵃ₁ₖ x₂ᵃ₂ₖ … xₙᵃₙₖ,    dom f = ℝ₊₊ⁿ
        sum of monomials

Problem (GP):
    minimize    f₀(x)
    subject to  fᵢ(x) ≤ 1,    i = 1,…,m
                hᵢ(x) = 1,    i = 1,…,p
    where fᵢ are posynomial, hᵢ are monomial

Brief explanations:
    - Variables and functions must be positive (x ∈ ℝ₊₊ⁿ)  
    - Posynomials are log-log convex: under change of variables u = log x, objective and ≤ constraints become convex  
    - Equality constraints hᵢ(x)=1 (monomials) become affine in u-space  
    - GP can be transformed into a convex optimization problem via logarithmic change of variables  
    - Solvable efficiently by interior-point methods after transformation  
    - Applications: circuit design, resource allocation, chemical engineering  
    - Allows modeling of power-law relationships and multiplicative trade-offs  

================================================================================
Geometric program in convex form
================================================================================

Change of variables and log transformation:
    yᵢ = log xᵢ,    bₖ = log cₖ

Monomial:
    f(x) = c·x₁ᵃ¹ … xₙᵃⁿ  
    ⇒ log f(eʸ) = aᵀy + b

Posynomial:
    f(x) = ∑ₖ₌₁ᴷ cₖ·x₁ᵃ₁ₖ … xₙᵃₙₖ  
    ⇒ log f(eʸ) = log(∑ₖ₌₁ᴷ exp(aₖᵀy + bₖ))

Convex form GP:
    minimize    log(∑ₖ₌₁ᴷ exp(a₀ₖᵀy + b₀ₖ))  
    subject to  log(∑ₖ₌₁ᴷ exp(aᵢₖᵀy + bᵢₖ)) ≤ 0,    i = 1,…,m  
                Gy + d = 0

Brief explanations:
    - Log-sum-exp is convex and represents posynomial ≤1 constraints  
    - Equality constraints Gy + d = 0 are affine in y  
    - Entire problem is a convex optimization in y-space  
    - Solvable by standard interior-point or first-order methods  
    - Transformation leverages log-log convexity of posynomials  
    - Guarantees globally optimal solution for original GP  
'''

##################################################################################

'''
================================================================================
Convex optimization with generalized inequality constraints
================================================================================

Problem (general form):
    minimize    f₀(x)
    subject to  fᵢ(x) ≼_{Kᵢ} 0,    i = 1,…,m
                Ax = b

    • f₀: ℝⁿ → ℝ is convex  
    • fᵢ: ℝⁿ → ℝᵏⁱ is Kᵢ-convex w.r.t. proper cone Kᵢ  
    • “≼_{Kᵢ} 0” means fᵢ(x) ∈ -Kᵢ  

Conic form special case:
    minimize    cᵀx
    subject to  Fx + g ≼_{K} 0
                Ax = b

    • Extends LP (K = ℝ₊ᵐ) to nonpolyhedral cones (SOC, SDP, etc.)

Brief explanations:
    - Generalized inequalities replace scalar ≤ with vector inequalities over cones  
    - Proper cone Kᵢ defines a partial order: u ≼_{Kᵢ} v ⇔ v-u ∈ Kᵢ  
    - Conic form has affine objectives/constraints, unifies LP, SOCP, SDP  
    - Convex feasible set; any local minimum is global  
    - Duality theory extends: conic duals give strong duality under Slater's condition  
    - Cone examples: nonnegative orthant (LP), second-order cone (SOCP), positive semidefinite cone (SDP)  
    - Enables modeling of a wide range of convex constraints in a unified framework  
'''

##################################################################################
'''
================================================================================
Semidefinite Programming (SDP)
================================================================================

Problem:
    minimize    cᵀx  
    subject to  x₁F₁ + x₂F₂ + … + xₙFₙ + G ≼ₛ₊ 0  
                Ax = b  
    (Fᵢ, G ∈ Sᵏ)

Notes:
    - Inequality constraint is a linear matrix inequality (LMI): X ≼ₛ₊ 0 ⇔ X is positive semidefinite  
    - Can include multiple LMIs by block-diagonal aggregation into a single LMI  

Brief explanations:
    - Extends conic form to the positive semidefinite cone S₊ᵏ  
    - LMI constraints model requirements on eigenvalues of affine matrix expressions  
    - Convex problem: feasible set is an intersection of affine “slices” of the PSD cone  
    - Solvable by interior-point methods with polynomial-time complexity  
    - Duality yields semidefinite dual problem with strong duality under Slater’s condition  
    - Applications: control system design (Lyapunov inequalities), covariance estimation, quantum information  
    - Special cases: when k=1 reduces to an SOCP (scalar PSD cone), when Fᵢ are diagonal reduces to an LP  
    - SDP relaxations provide tractable bounds for hard combinatorial problems (e.g., Max-Cut)  
'''

##################################################################################

'''
================================================================================
LP and SOCP as SDP
================================================================================

LP and equivalent SDP:
    LP:
        minimize    cᵀx  
        subject to  Ax ≼ b  
    SDP:
        minimize    cᵀx  
        subject to  diag(Ax - b) ≼ₛ₊ 0  

SOCP and equivalent SDP:
    SOCP:
        minimize    fᵀx  
        subject to  ‖Aᵢx + bᵢ‖₂ ≤ cᵢᵀx + dᵢ,    i = 1,…,m  
    SDP:
        minimize    fᵀx  
        subject to  [ (cᵢᵀx + dᵢ) I      Aᵢx + bᵢ  
                      (Aᵢx + bᵢ)ᵀ   (cᵢᵀx + dᵢ) ] ≽ₛ₊ 0,    i = 1,…,m  

Brief explanations:
    - LP can be viewed as an SDP over the diagonal PSD cone (scalar constraints become one-by-one LMIs)  
    - diag(Ax-b)≼ₛ₊0 enforces each component (Ax-b)ᵢ ≤ 0 via 1x1 PSD blocks  
    - SOCP constraints ‖u‖₂ ≤ t are equivalent to 2x2 PSD constraints on [ tI u; uᵀ t ]  
    - Embedding LP and SOCP in SDP unifies all as conic problems over the PSD cone  
    - Enables use of general-purpose SDP solvers for a wider class of problems  
'''

##################################################################################

'''
================================================================================
Vector optimization
================================================================================

General vector optimization problem:
    minimize (w.r.t. K)    f₀(x)
    subject to             fᵢ(x) ≼ 0,    i = 1,…,m  
                            hᵢ(x) = 0, i = 1,…,p  

    • f₀: ℝⁿ → ℝᵠ is vector‐valued  
    • “minimize w.r.t. K” means find x such that f₀(x) is minimal under the partial order defined by proper cone K ⊆ ℝᵠ  
    • fᵢ: ℝⁿ → ℝ are scalar convex functions  

Convex vector optimization problem:
    minimize (w.r.t. K)    f₀(x)
    subject to             fᵢ(x) ≤ 0,   i = 1,…,m  
                            A x = b  

    • f₀ is K‐convex: for all x,y and θ∈[0,1],  
        f₀(θx+(1–θ)y) ≼ θ f₀(x)+(1–θ) f₀(y)  
    • scalar constraints fᵢ convex, equality constraints affine  

Brief explanations:
    - Objectives are vector‐valued; optimality means no other feasible point yields a strictly smaller vector in cone ordering  
    - Trade‐offs between objectives characterized by Pareto frontier (set of nondominated solutions)  
    - Proper cone K (e.g., nonnegative orthant) defines preference direction in objective space  
    - Can be scalarized via weighted sums or ε‐constraint methods to compute Pareto‐optimal points  
    - Convexity ensures convex Pareto frontier and tractable computation of supported efficient points  
    - Applications: multi‐criteria decision making, game theory, economics, engineering design  
'''