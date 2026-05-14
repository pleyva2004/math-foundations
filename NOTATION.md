# Math Foundations - Notation Glossary

> Auto-generated from `notation.json` by `generate_notation.py`. **Do not edit by hand.**

This glossary indexes every distinct mathematical symbol used across the 42 concept lessons. Each row gives the LaTeX symbol, how to read it aloud, a one-line plain-English meaning, and a link to the concept folder where the symbol is first introduced.

**Total entries:** 157.  
**Source of truth:** [`notation.json`](notation.json).  
**PDF cheatsheet:** [`notation.pdf`](notation.pdf) (compiled in CI from [`notation.tex`](notation.tex)).

## Contents

- [Logic](#logic) (13 entries)
- [Sets](#sets) (18 entries)
- [Functions](#functions) (9 entries)
- [Number systems](#number-systems) (8 entries)
- [Linear algebra](#linear-algebra) (15 entries)
- [Analysis](#analysis) (11 entries)
- [Calculus](#calculus) (10 entries)
- [Series and modes of convergence](#series-and-modes-of-convergence) (8 entries)
- [Probability](#probability) (15 entries)
- [Distributions](#distributions) (9 entries)
- [Information theory](#information-theory) (9 entries)
- [Stochastic calculus](#stochastic-calculus) (8 entries)
- [Optimisation](#optimisation) (7 entries)
- [Information geometry and optimal transport](#information-geometry-and-optimal-transport) (5 entries)
- [Meta-notation](#meta-notation) (12 entries)

## Logic

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\forall$ | "for all" | Universal quantifier. 'For every x in S, the property P(x) holds.' Used to make claims about every element of a set. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\exists$ | "there exists" | Existential quantifier. 'There is at least one x in S such that P(x) holds.' | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\exists!$ | "there exists a unique" | Existence and uniqueness: there is exactly one element with the stated property. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\neg$ | "not" | Logical negation. ¬P is true iff P is false. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\wedge$ | "and" | Logical conjunction. P ∧ Q is true iff both P and Q are true. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\vee$ | "or" | Logical disjunction (inclusive). P ∨ Q is true iff at least one of P, Q is true. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\Rightarrow$ | "implies" | Material implication. P ⇒ Q means whenever P holds, Q holds. Vacuously true when P is false. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\Leftrightarrow$ | "if and only if" | Logical equivalence. P ⇔ Q means P and Q have the same truth value. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\therefore$ | "therefore" | Marks a conclusion that follows from previously stated premises. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\because$ | "because" | Marks a reason or premise supporting a conclusion. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\vdash$ | "proves" | Syntactic entailment. Γ ⊢ φ means φ is derivable from premises Γ in a formal proof system. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\vDash$ | "models / entails" | Semantic entailment. Γ ⊨ φ means every model of Γ is a model of φ. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\square$ | "QED / end of proof" | Marks the end of a proof. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |

## Sets

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\in$ | "is an element of / in" | Set membership. x ∈ S means x is an element of the set S. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\notin$ | "is not an element of" | Negated set membership. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\subset$ | "is a (proper) subset of" | A ⊂ B means every element of A is in B (often used for proper subsets). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\subseteq$ | "is a subset of (or equal)" | A ⊆ B means every element of A is in B; equality allowed. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\supseteq$ | "is a superset of (or equal)" | A ⊇ B is the reverse of B ⊆ A. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\supset$ | "is a (proper) superset of" | Reverse of ⊂. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\cup$ | "union" | A ∪ B is the set of elements in A or B (or both). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\cap$ | "intersection" | A ∩ B is the set of elements in both A and B. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\bigcup$ | "union over" | Indexed union over a collection of sets. | [18-sigma-algebras](concepts/18-sigma-algebras/README.md) |
| $\bigcap$ | "intersection over" | Indexed intersection over a collection of sets. | [18-sigma-algebras](concepts/18-sigma-algebras/README.md) |
| $\emptyset$ | "empty set" | The unique set with no elements. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\setminus$ | "set minus / without" | A ∖ B is the set of elements in A but not in B. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $A^c$ | "complement of A" | The set of elements (in some ambient universe) not in A. | [18-sigma-algebras](concepts/18-sigma-algebras/README.md) |
| $\times$ | "Cartesian product" | A × B is the set of ordered pairs (a, b) with a ∈ A, b ∈ B. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $|S|$ | "cardinality / size of" | Number of elements of a (finite) set S; more generally, its cardinal. | [02-counting](concepts/02-counting/README.md) |
| $\mathcal{P}(S)$ | "power set of" | The set of all subsets of S. \|𝒫(S)\| = 2^{\|S\|} for finite S. | [02-counting](concepts/02-counting/README.md) |
| $\{x : P(x)\}$ | "the set of x such that P(x)" | Set-builder notation: the set of all x satisfying property P. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\binom{n}{k}$ | "n choose k" | Number of k-element subsets of an n-element set. | [02-counting](concepts/02-counting/README.md) |

## Functions

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $f : A \to B$ | "f from A to B" | A function f with domain A and codomain B; for every a ∈ A there is a unique f(a) ∈ B. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mapsto$ | "maps to" | Specifies the action of a function on an element. x ↦ f(x). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\circ$ | "composed with" | Function composition: (g ∘ f)(x) = g(f(x)). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $f^{-1}$ | "f inverse" | The inverse function (when bijective): f⁻¹(f(x)) = x. Also denotes preimage of a set. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathrm{id}_A$ | "identity on A" | The function that sends every element of A to itself. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathrm{dom}(f)$ | "domain of f" | The set of inputs on which f is defined. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathrm{cod}(f)$ | "codomain of f" | The declared target set of f (not necessarily its image). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathrm{im}(f)$ | "image of f" | The set of actual outputs of f: {f(x) : x ∈ dom(f)}. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $f|_S$ | "f restricted to S" | The function f considered only on the smaller domain S ⊆ dom(f). | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |

## Number systems

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\mathbb{N}$ | "the natural numbers" | Non-negative integers (0, 1, 2, …) or positive integers, depending on convention. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathbb{Z}$ | "the integers" | All integers …, -2, -1, 0, 1, 2, …. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathbb{Q}$ | "the rationals" | Numbers expressible as p/q with p, q integers and q ≠ 0. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathbb{R}$ | "the reals" | The complete ordered field of real numbers. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\mathbb{C}$ | "the complex numbers" | Numbers a + bi with a, b ∈ ℝ and i² = -1. | [04-groups-rings-fields](concepts/04-groups-rings-fields/README.md) |
| $\mathbb{R}^n$ | "R to the n" | n-dimensional real coordinate space; vectors of n real numbers. | [05-vector-spaces](concepts/05-vector-spaces/README.md) |
| $\mathbb{R}_{+}$ | "the positive reals" | The set of non-negative (or strictly positive) real numbers. | [09-norms-and-metrics](concepts/09-norms-and-metrics/README.md) |
| $\mathbb{F}$ | "a field" | An arbitrary field (typically ℝ or ℂ); used as the scalar field of a vector space. | [04-groups-rings-fields](concepts/04-groups-rings-fields/README.md) |

## Linear algebra

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\dim V$ | "dimension of V" | Cardinality of any basis of the vector space V. | [05-vector-spaces](concepts/05-vector-spaces/README.md) |
| $\mathrm{rank}(A)$ | "rank of A" | Dimension of the image (column space) of a linear map / matrix. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\det A$ | "determinant of A" | Signed n-dimensional volume scaling factor of a square matrix; zero iff non-invertible. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\mathrm{tr}(A)$ | "trace of A" | Sum of diagonal entries of a square matrix; equals the sum of eigenvalues. | [07-eigenvalues](concepts/07-eigenvalues/README.md) |
| $\langle u, v \rangle$ | "inner product of u and v" | A bilinear (or sesquilinear) form encoding angle and length; e.g. the dot product on ℝⁿ. | [08-inner-product-spaces](concepts/08-inner-product-spaces/README.md) |
| $\|x\|$ | "norm of x" | Length of a vector; satisfies positive-definiteness, scaling, and triangle inequality. | [09-norms-and-metrics](concepts/09-norms-and-metrics/README.md) |
| $\otimes$ | "tensor product" | Tensor product of vector spaces or vectors; bilinear factorisation of multilinear maps. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\ker T$ | "kernel of T" | Set of vectors mapped to 0 by linear map T; a subspace of the domain. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\mathrm{im}\, T$ | "image of T" | Set of outputs of a linear map; a subspace of the codomain. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\mathrm{span}(S)$ | "span of S" | Set of all linear combinations of vectors in S; smallest subspace containing S. | [05-vector-spaces](concepts/05-vector-spaces/README.md) |
| $T^{*}$ | "T adjoint / T conjugate transpose" | Adjoint of a linear map; on inner-product spaces ⟨T u, v⟩ = ⟨u, T* v⟩. | [08-inner-product-spaces](concepts/08-inner-product-spaces/README.md) |
| $A^{\top}$ | "A transpose" | Matrix obtained by swapping rows and columns of A. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $\lambda_i$ | "lambda i / i-th eigenvalue" | Scalar λ such that T v = λ v for some non-zero eigenvector v. | [07-eigenvalues](concepts/07-eigenvalues/README.md) |
| $AB$ | "A times B" | Matrix product representing composition of the corresponding linear maps. | [06-linear-maps](concepts/06-linear-maps/README.md) |
| $I_n$ | "n-by-n identity" | Square matrix with ones on the diagonal, zeros elsewhere. | [06-linear-maps](concepts/06-linear-maps/README.md) |

## Analysis

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\lim_{n \to \infty} a_n$ | "limit as n goes to infinity" | The value a_n approaches as n grows without bound. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\sup S$ | "supremum of S" | Least upper bound of S; the smallest number ≥ every element of S. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\inf S$ | "infimum of S" | Greatest lower bound of S; the largest number ≤ every element of S. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\max S$ | "max of S" | Largest element of S, when it exists. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\min S$ | "min of S" | Smallest element of S, when it exists. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\to$ | "tends to / approaches" | Convergence of a sequence or value: a_n → L means a_n approaches L. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\varepsilon$ | "epsilon" | Small positive tolerance used in the ε-δ / ε-N definitions of limit and continuity. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\delta$ | "delta" | Tolerance on inputs paired with ε in the ε-δ definition of continuity. | [11-continuity](concepts/11-continuity/README.md) |
| $\infty$ | "infinity" | An idealised unbounded quantity used in limits, sums, and integrals. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $|x|$ | "absolute value" | Distance of a real number from 0; the canonical norm on ℝ. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $d(x, y)$ | "distance from x to y" | A metric: non-negative, symmetric, satisfying the triangle inequality. | [09-norms-and-metrics](concepts/09-norms-and-metrics/README.md) |

## Calculus

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\frac{d}{dx}$ | "derivative with respect to x" | Differentiation operator with respect to a single variable. | [12-derivatives](concepts/12-derivatives/README.md) |
| $f'(x)$ | "f prime of x" | Derivative of a univariate function f at x. | [12-derivatives](concepts/12-derivatives/README.md) |
| $\frac{\partial}{\partial x}$ | "partial derivative with respect to x" | Derivative of a multivariable function holding the other variables fixed. | [13-multivariate-calculus](concepts/13-multivariate-calculus/README.md) |
| $\nabla$ | "nabla / gradient" | Gradient operator: ∇f is the vector of partial derivatives of f. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $J_f$ | "Jacobian of f" | Matrix of all first-order partial derivatives of a vector-valued function. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $H_f$ | "Hessian of f" | Matrix of second partial derivatives of a scalar function f. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\int$ | "integral" | Riemann (or Lebesgue) integral; signed area / total accumulation. | [15-integration](concepts/15-integration/README.md) |
| $\iint$ | "double integral" | Integral over a 2-dimensional region. | [15-integration](concepts/15-integration/README.md) |
| $\sum$ | "sum / sigma" | Indexed summation operator. | [02-counting](concepts/02-counting/README.md) |
| $\prod$ | "product" | Indexed product operator. | [02-counting](concepts/02-counting/README.md) |

## Series and modes of convergence

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\xrightarrow{\text{a.s.}}$ | "converges almost surely to" | Almost-sure convergence: P(X_n → X) = 1. | [31-stochastic-processes](concepts/31-stochastic-processes/README.md) |
| $\xrightarrow{P}$ | "converges in probability to" | P(\|X_n − X\| > ε) → 0 for every ε > 0. | [31-stochastic-processes](concepts/31-stochastic-processes/README.md) |
| $\xrightarrow{d}$ | "converges in distribution to" | Convergence of CDFs at every continuity point of the limit. | [31-stochastic-processes](concepts/31-stochastic-processes/README.md) |
| $\limsup_{n\to\infty} a_n$ | "limit superior" | Largest accumulation value of a sequence; inf over n of sup of the tail. | [16-series-and-convergence](concepts/16-series-and-convergence/README.md) |
| $\liminf_{n\to\infty} a_n$ | "limit inferior" | Smallest accumulation value of a sequence; sup over n of inf of the tail. | [16-series-and-convergence](concepts/16-series-and-convergence/README.md) |
| $\text{Cauchy}$ | "Cauchy sequence" | Sequence whose terms eventually get arbitrarily close to each other; characterises convergence in complete spaces. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\sum_{n=1}^{\infty} a_n$ | "the series sum a_n" | Limit of partial sums S_N = ∑_{n≤N} a_n; converges if the limit exists. | [16-series-and-convergence](concepts/16-series-and-convergence/README.md) |
| $\xrightarrow{L^2}$ | "converges in mean-square / L^2" | 𝔼[\|X_n − X\|²] → 0. | [31-stochastic-processes](concepts/31-stochastic-processes/README.md) |

## Probability

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $P(A)$ | "probability of A" | Probability of event A under a probability measure P. | [19-probability-measures](concepts/19-probability-measures/README.md) |
| $P(A \mid B)$ | "probability of A given B" | Conditional probability of A given that B has occurred: P(A ∩ B)/P(B). | [20-conditional-probability](concepts/20-conditional-probability/README.md) |
| $\mathbb{E}[X]$ | "expectation of X" | Expected value (mean) of a random variable X under its distribution. | [25-expectation](concepts/25-expectation/README.md) |
| $\mathbb{E}[X \mid Y]$ | "conditional expectation of X given Y" | Best (in L²) prediction of X given the σ-algebra generated by Y. | [27-conditional-expectation](concepts/27-conditional-expectation/README.md) |
| $\mathrm{Var}(X)$ | "variance of X" | 𝔼[(X − 𝔼[X])²]; spread of X around its mean. | [26-variance-covariance](concepts/26-variance-covariance/README.md) |
| $\mathrm{Cov}(X, Y)$ | "covariance of X and Y" | 𝔼[(X − 𝔼[X])(Y − 𝔼[Y])]; signed measure of linear association. | [26-variance-covariance](concepts/26-variance-covariance/README.md) |
| $\sim$ | "is distributed as" | X ~ D means X has distribution D. | [23-distributions](concepts/23-distributions/README.md) |
| $\text{i.i.d.}$ | "independent and identically distributed" | Random variables that are mutually independent and share the same distribution. | [21-independence](concepts/21-independence/README.md) |
| $\perp\!\!\!\perp$ | "is independent of" | X ⫫ Y means X and Y are independent random variables / events. | [21-independence](concepts/21-independence/README.md) |
| $\mathcal{F}$ | "script F / sigma-algebra" | A σ-algebra: collection of measurable subsets closed under complement and countable union. | [18-sigma-algebras](concepts/18-sigma-algebras/README.md) |
| $\Omega$ | "Omega / sample space" | Sample space: set of all possible outcomes of an experiment. | [17-sample-spaces](concepts/17-sample-spaces/README.md) |
| $\mathbf{1}_A$ | "indicator of A" | Function that is 1 on A and 0 elsewhere; bridges sets and integrals. | [25-expectation](concepts/25-expectation/README.md) |
| $F_X(x)$ | "CDF of X" | Cumulative distribution function: F_X(x) = P(X ≤ x). | [23-distributions](concepts/23-distributions/README.md) |
| $p_X(x)$ | "density of X at x" | Probability density function: P(X ∈ A) = ∫_A p_X(x) dx. | [24-pdf](concepts/24-pdf/README.md) |
| $p(x)$ | "probability mass function" | p(x) = P(X = x) for a discrete random variable X. | [23-distributions](concepts/23-distributions/README.md) |

## Distributions

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\mathrm{Bern}(p)$ | "Bernoulli of p" | Distribution of a 0/1 random variable with P(X=1) = p. | [23-distributions](concepts/23-distributions/README.md) |
| $\mathrm{Bin}(n, p)$ | "Binomial of n, p" | Number of successes in n independent Bernoulli(p) trials. | [23-distributions](concepts/23-distributions/README.md) |
| $\mathrm{Poi}(\lambda)$ | "Poisson of lambda" | Counts of rare events with rate λ; P(X=k) = e^{-λ} λ^k / k!. | [23-distributions](concepts/23-distributions/README.md) |
| $U(a, b)$ | "Uniform on [a, b]" | Continuous distribution with constant density 1/(b-a) on [a, b]. | [24-pdf](concepts/24-pdf/README.md) |
| $\mathrm{Exp}(\lambda)$ | "Exponential of lambda" | Memoryless waiting-time distribution with rate λ; density λ e^{-λ x}, x ≥ 0. | [24-pdf](concepts/24-pdf/README.md) |
| $\mathcal{N}(\mu, \sigma^2)$ | "normal of mu, sigma squared" | Gaussian distribution with mean μ and variance σ². | [24-pdf](concepts/24-pdf/README.md) |
| $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ | "multivariate normal of mu, Sigma" | Joint Gaussian on ℝⁿ with mean vector μ and covariance matrix Σ. | [26-variance-covariance](concepts/26-variance-covariance/README.md) |
| $\mathrm{Cat}(\pi)$ | "categorical of pi" | Discrete distribution over k classes with probability vector π. | [23-distributions](concepts/23-distributions/README.md) |
| $\mathrm{Beta}(\alpha, \beta)$ | "Beta of alpha, beta" | Continuous distribution on [0,1]; conjugate prior to the Bernoulli/Binomial. | [24-pdf](concepts/24-pdf/README.md) |

## Information theory

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $H(X)$ | "entropy of X" | Shannon entropy: H(X) = -𝔼[log p(X)]; average uncertainty / information. | [36-shannon-entropy](concepts/36-shannon-entropy/README.md) |
| $H(X \mid Y)$ | "conditional entropy of X given Y" | Average uncertainty in X after observing Y. | [36-shannon-entropy](concepts/36-shannon-entropy/README.md) |
| $I(X; Y)$ | "mutual information of X and Y" | Reduction in uncertainty about X from observing Y; symmetric in X, Y. | [39-mutual-information](concepts/39-mutual-information/README.md) |
| $D_{\mathrm{KL}}(p \,\|\, q)$ | "KL divergence from q to p" | Relative entropy: 𝔼_p[log p − log q]; non-symmetric, non-negative. | [38-kl-divergence](concepts/38-kl-divergence/README.md) |
| $H(p, q)$ | "cross-entropy of p and q" | −𝔼_p[log q]; average code length using q on samples from p. | [37-cross-entropy](concepts/37-cross-entropy/README.md) |
| $I(x)$ | "self-information of x" | Surprisal: I(x) = -log p(x); information content of a single outcome. | [35-self-information](concepts/35-self-information/README.md) |
| $\log$ | "log" | Logarithm; in information theory typically natural (ln) or base 2 depending on units. | [35-self-information](concepts/35-self-information/README.md) |
| $\ln$ | "natural log" | Logarithm base e. | [35-self-information](concepts/35-self-information/README.md) |
| $\log_2$ | "log base 2" | Logarithm base 2; gives entropy in bits. | [36-shannon-entropy](concepts/36-shannon-entropy/README.md) |

## Stochastic calculus

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $W_t$ | "Brownian motion at time t" | Standard Wiener process: continuous, W_0 = 0, independent Gaussian increments. | [32-brownian-motion](concepts/32-brownian-motion/README.md) |
| $dW_t$ | "differential of Brownian motion" | Infinitesimal Brownian increment; the driving noise of an SDE. | [33-sde](concepts/33-sde/README.md) |
| $dX_t$ | "differential of X at t" | Infinitesimal change in a stochastic process; the LHS of an SDE in differential form. | [33-sde](concepts/33-sde/README.md) |
| $[X]_t$ | "quadratic variation of X at t" | Limit of sums of squared increments; for Brownian motion, [W]_t = t. | [34-ito-calculus](concepts/34-ito-calculus/README.md) |
| $\langle X \rangle_t$ | "predictable quadratic variation of X" | Compensator: predictable process making X² − ⟨X⟩ a martingale. | [34-ito-calculus](concepts/34-ito-calculus/README.md) |
| $\mathcal{F}_t$ | "filtration at time t" | Increasing family of σ-algebras encoding information available up to time t. | [31-stochastic-processes](concepts/31-stochastic-processes/README.md) |
| $\int_0^t \sigma_s\, dW_s$ | "Itô integral" | Stochastic integral against Brownian motion, defined as an L² limit of left-Riemann sums. | [34-ito-calculus](concepts/34-ito-calculus/README.md) |
| $df(X_t) = f'(X_t)\,dX_t + \tfrac{1}{2} f''(X_t)\, d[X]_t$ | "Itô's lemma" | Chain rule for Itô processes: includes a second-order quadratic-variation correction. | [34-ito-calculus](concepts/34-ito-calculus/README.md) |

## Optimisation

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $\operatorname*{arg\,min}_{x \in \mathcal{X}} f(x)$ | "argmin of f" | Set of inputs at which f attains its minimum value over the search domain. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\operatorname*{arg\,max}_{x \in \mathcal{X}} f(x)$ | "argmax of f" | Set of inputs at which f attains its maximum value. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\nabla L$ | "gradient of L" | Gradient of a loss / objective function; direction of steepest ascent. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\eta$ | "eta / learning rate" | Step size in gradient-based optimisation. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\mathrm{softmax}$ | "softmax" | softmax(z)_i = e^{z_i} / Σ_j e^{z_j}; turns logits into a probability vector. | [37-cross-entropy](concepts/37-cross-entropy/README.md) |
| $\mathcal{L}$ | "Lagrangian" | Lagrangian for a constrained optimisation; encodes objective plus multiplier × constraints. | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |
| $\leftarrow$ | "is updated to" | Assignment / update step (as in iterative algorithms). | [14-gradient-jacobian](concepts/14-gradient-jacobian/README.md) |

## Information geometry and optimal transport

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $W_p(\mu, \nu)$ | "p-Wasserstein distance between mu and nu" | Optimal-transport distance: inf over couplings (X,Y) of (𝔼[d(X,Y)^p])^{1/p}. | [41-optimal-transport](concepts/41-optimal-transport/README.md) |
| $F(\theta)$ | "Fisher information at theta" | Riemannian metric on a parametric statistical model; F(θ)_{ij} = 𝔼[(∂_i log p)(∂_j log p)]. | [40-information-geometry](concepts/40-information-geometry/README.md) |
| $B_{\mathrm{KL}}(p, \varepsilon)$ | "KL ball of radius epsilon around p" | Set of distributions q with D_KL(p ‖ q) ≤ ε; trust region in info-geometric methods. | [40-information-geometry](concepts/40-information-geometry/README.md) |
| $\tilde{\nabla} L(\theta)$ | "natural gradient of L" | Fisher-preconditioned gradient: F(θ)^{-1} ∇L(θ); steepest descent in KL geometry. | [40-information-geometry](concepts/40-information-geometry/README.md) |
| $\Gamma(\mu, \nu)$ | "couplings of mu and nu" | Set of joint distributions with marginals μ and ν; the feasible set in optimal transport. | [41-optimal-transport](concepts/41-optimal-transport/README.md) |

## Meta-notation

| Symbol | Read aloud as | Meaning | First seen in |
|--------|---------------|---------|---------------|
| $:=$ | "is defined as" | Introduces a definition: the LHS is defined to equal the RHS. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\equiv$ | "is equivalent / equals by definition" | Identity by definition; or logical equivalence between formulas. | [01-logic-and-proof](concepts/01-logic-and-proof/README.md) |
| $\approx$ | "is approximately equal to" | Approximate equality; used informally and in numerical statements. | [12-derivatives](concepts/12-derivatives/README.md) |
| $\propto$ | "is proportional to" | Equality up to a positive multiplicative constant; common in Bayesian posteriors. | [20-conditional-probability](concepts/20-conditional-probability/README.md) |
| $O(g(n))$ | "big O of g" | Asymptotic upper bound: f = O(g) iff \|f(n)\| ≤ C \|g(n)\| for large n. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $o(g(n))$ | "little o of g" | f = o(g) iff f(n)/g(n) → 0; strictly negligible compared to g. | [12-derivatives](concepts/12-derivatives/README.md) |
| $\Theta(g(n))$ | "Theta of g" | Tight asymptotic bound: f = Θ(g) iff f = O(g) and g = O(f). | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\Omega(g(n))$ | "big Omega of g" | Asymptotic lower bound: f = Ω(g) iff \|f(n)\| ≥ c \|g(n)\| for large n. | [10-sequences-and-limits](concepts/10-sequences-and-limits/README.md) |
| $\cong$ | "is isomorphic to / congruent to" | Structural equivalence (groups, vector spaces, …) or geometric congruence. | [04-groups-rings-fields](concepts/04-groups-rings-fields/README.md) |
| $\neq$ | "is not equal to" | Negated equality. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\leq$ | "less than or equal to" | Non-strict inequality. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |
| $\geq$ | "greater than or equal to" | Non-strict inequality. | [00-sets-and-functions](concepts/00-sets-and-functions/README.md) |

