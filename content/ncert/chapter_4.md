# Chapter 4: Determinants

> "All Mathematical truths are relative and conditional."
> - C.P. STEINMETZ

# 4.1 Introduction

In the previous chapter, we have studied matrices and the algebra of matrices. We have also learnt that a system of algebraic equations can be expressed using matrices. This means, a system of linear equations like  

$a_1x + b_1y = c_1$ 

$a_2x + b_2y = c_2$

can be represented as 
<p>
\[
\left[\begin{array}{c}
a_1 & b_1 \\
a_2 & b_2 
\end{array}
\right]
\left[\begin{array}{c}
x  \\
y 
\end{array}
\right] \quad = \quad 
\left[\begin{array}{c}
c_1  \\
c_2 
\end{array}
\right].
\]
</p>
Now, this system of equations has a unique solution or not, is determined by the number $a_1b_2 - a_2b_1$. (Recall that if $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ or $a_1b_2 - a_2b_1 \neq 0$
then the system of linear equations has a unique solution). The number of $a_1b_2 - a_2b_1$ which determines uniqueness of solution is associated with the matrix 
<p>
\[
A=\left[\begin{array}{c}
a_1 & b_1 \\
a_2 & b_2 
\end{array}
\right]
\]
</p>
and is called the determinat of A or det A.
Determinants have wide applications in engineering, science, economics, and social sciences.

---

# 4.2 Determinant

A determinant is associated with every square matrix $A = [a_{ij}]_{n \times n}$.

<p>
If
\[
A=\left[\begin{array}{c}
a_1 & b_1 \\
a_2 & b_2 
\end{array}
\right]
\]
</p>
<p>
then the determinant of \( A \) is written as 
\[
|A| = 
\left|\begin{array}{cc}
a_1 & b_1 \\
a_2 & b_2
\end{array}\right|
\]
</p>

**Notes**

1. |A| is the determinat of A and not modulus of A.

2. Only square matrices have determinants.


### 4.2.1 Determinant of matrix of order one

Let A = [a] be the matrix of order 1, then determinant of A is defined to be equal to a.

### 4.2.2 Determinant of matrix of order two

<p>
Let
\[
A=\left[\begin{array}{c}
a_1 & b_1 \\
a_2 & b_2 
\end{array}
\right]
\]
be a matrix of order $2 \times 2$, then the determinant of A is defined as :

</p>
<p> 
\[
\det(A) = |A| = 
\left|\begin{array}{cc}
a_1 & b_1 \\
a_2 & b_2
\end{array}\right|
= a_1b_2 - a_2b_1
\]
</p>

### Determinant of a matrix of order 3

<p>
Let
\[
A=\left[\begin{array}{c}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3
\end{array}
\right]
\]
be a matrix of order $3 \times 3$, then the determinant of A is defined as :
</p>
<p> 
\[
\det(A) = |A| = 
\left|\begin{array}{cc}
a_1 & b_1 & c_1\\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3
\end{array}\right|
= a_1b_2c_3 - a_1b_3c_2 - b_1a_2c_3 + b_1a_3c_2 + c_1a_2b_3 - c_1a_3b_2
\]
</p>

In above matrix we are finding the determinant by using first row.

**Notes:**

1. The value remains the same by expansion along any row or column. For easier calculation, expand along the row or column which contains the maximum number of zeroes.

2. While expanding, instead of multiplying by $(-1)^{i+j}$, we can multiply by +1 or -1 according as (i+j) is even or odd.

3. In general, if A = kB where A and B are square matrices of order n, then $|A| = k^n |B|$, Where n = 1,2,3

---

# 4.3 Properties of Determinants

**Property 1** The values of the determinant remains unchanged if its rows and columns are interchanged.

**Property 2** If any two rows (or columns) of a determinants are interchanged, then gives of determinant changes.

**Property 3** If any two rows (or columns) of a determinant are identical (all corresponding elements are same), then value of determinant is zero.

**Property 4** If each element of a row(or a column) of a determinant is multiplied by a constant k, then its value gets multipled by k.

**Notes:** 

1. By this property, we can take out any comman factor from any one row or any one column of a given determinat.

2. If corresponding elements of any two rows ( or columns) of a determinant are proportional (in the same ratio), then its value is zero.

**Property 5** If some or all elements of a row or column of a determinant are expressed as sum of two (or more) terms, then the determinant can be expressed as sum of two ( or more) determinants.

**Property 6** If, to each element of any row or column of a determinants, the equimultiples of corresponding elements of other row(or column) are added, then value of determinant remains the same.
i.e. the value of determinant remain same if we apply the operation 
$R_{i} \\rightarrow R_{i} + kR_{i}$ or $C_{j} \\rightarrow C_{j} + kC_{j}$

---

# 4.4 Area of a Triangle

The area of triangle whose vertices are $(x_1, y_1), (x_2,y_2)$ and $(x_3, y_3)$ is given by the expression $\frac{1}{2}[x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)]$. Now this expression can be written in the form of a determinant as 
<p> 
\[
\Delta  = \frac{1}{2}
\left|\begin{array}{cc}
x_1 & y_1 & 1\\
x_2 & y_2 & 1 \\
x_3 & y_3 & 1
\end{array}\right|
\]
</p>

**Note:**

1. We know that area is a positive quantity, we always take the absolute value of the determinant.

2. If area is given, use both positive and negative values for the determinant for calculation.

3. This area of the triangle formed by three collinear points is zero.

---

# 4.5 Minors and Cofactors

- **Minor:** Minor of an element $a_{ij}$ of a determinant is the determinant obtained by deleting its ith row and jth column in which element a_{ij} lies. Minor of an element $a_{ij}$ is denoted by $M_{ij}$.

**Notes:** Minor of an element of a determinant of order n$(n \geq 2)$ is a determinant of order n-1.

- **Cofactor:** Cofactor of an element $ a_{ij}$, denoted by $A_{ij}$ is defined by 

$A_{ij} = (-1)^{i+j}M_{ij}$, Where $M_{ij}$ is minor of $a_{ij}$

- The expansion of the determinant is the sum of elements of any row (or column) multiplied by their respective cofactors. i.e.

$\Delta = a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13}$

- If elements of a row ( or column) are multiplied with cofactors of any other row ( or column), then their sum is zero. i.e.

$\Delta = a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13} = 0$

---

# 4.6 Adjoint and Inverse of a Matrix

- **Adjoint** The adjoint of a square matrix 
$$A = [a_{ij}]_{n \times n}$$

is defined as the transpose of the matrix
$$[A_{ij}]_{n \times n}$$

where $A_{ij}$
is the cofactor of the element $a_{ij}$. Adjoint of the matrix A is denoted by adj A.

<p>
Let
\[
A=\left[\begin{array}{c}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}
\right]
\]
</p>
Then 
<p>
\[
adjA= Transpose of \left[\begin{array}{c}
A_{11} & A_{12} & A_{13} \\
A_{21} & A_{22} & A_{23} \\
A_{31} & A_{32} & A_{33}
\end{array}
\right] \quad = \quad
\left[\begin{array}{c}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}
\right]
\]
</p>

**Theorem 1** If A be any given square matrix of order n then
$$A(adj A) = (adj A) A =|A|\mathbf{I}$$
Where $\mathbf{I}$ is the identity matrix of order n.

**Definition:** A square matrix A is said to be singular if $|A|=0$

**Definition:** A square matrix A is said to be non-singular if $|A| \neq 0$

**Theorem 2** If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.

**Theorem 3** The determinant of the product of matrices is equal to product of their repesctive determinants, that is |AB| = |A||B|, Where A and B are square matrices of the same order.

**Notes:** we know that $A(adj A) = (adj A) A =|A|\mathbf{I}$

so, $$|(adj A)| = |A|^2$$

In general, if A is a square matrix of order n, then $|(adj A)| = |A|^{n-1}$

**Theorem 4** A square matrix A is invertible if and only if A is nonsingular matrix.

So, $$A^{-1} = \frac{1}{|A|}adj A$$

---

# 4.7 Applications of Determinants and Matrices

- **Consistent system:** A system of equation is consistent if a solution exists (unique or infinite).

- **Inconsistent system:** A system of equations is inconsistent if its solution does not exists.

### 4.7.1 Solution of system of linear equations using inverse of a matrix: 

Consider the system of equations
$$a_1 \hspace{0.1cm} x + b_1 \hspace{0.1cm} y + c_1 \hspace{0.1cm} z = d_1$$
$$a_2 \hspace{0.1cm} x + b_2 \hspace{0.1cm} y + c_2 \hspace{0.1cm} z = d_2$$
$$a_3 \hspace{0.1cm} x + b_3 \hspace{0.1cm} y + c_3 \hspace{0.1cm} z = d_3$$

<p>
Let
\[
A=\left[\begin{array}{c}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}
\right], \quad 
X =\left[\begin{array}{c}
x  \\
y \\
z
\end{array}
\right] \quad and \quad
B =\left[\begin{array}{c}
d_{1}  \\
d_{2} \\
d_{3}
\end{array}
\right]
\]
</p>

Then, the system of equations can be written as AX = B, i.e.
<p>
\[
\left[\begin{array}{c}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}
\right] 
\left[\begin{array}{c}
x  \\
y \\
z
\end{array}
\right] \quad = \quad
\left[\begin{array}{c}
d_{1}  \\
d_{2} \\
d_{3}
\end{array}
\right]
\]
</p>

**Case 1** If A is a nonsingular matrix, then its inverse exists. Now
$$AX = B$$

$$A^{-1}\hspace{0.1cm}(AX) = B$$

$$(A^{-1}A)\hspace{0.1cm}X = A^{-1}B$$

$$\mathbf{I}  \hspace{0.1cm}X = A^{-1}B$$

$$X = A^{-1}B$$

This matrix equation provides unique solution for the given system of equations as inverse of a matrix is unique. This method of solving of equations is known as Matrix Method.

**Case 2** If A is a singular matrix, then |A| = 0.

In this case, we calculate (adj A) B.

If $(adj A) B \neq  O$, (O being zero matrix), then solution does not exist and the system of equations is called inconsistent.

If $(adj A) B = O$, then system may be either consistent or inconsistent according as the system have either infinitely many solutions or no solution. 

---

## Exercises

The chapter contains exercises to:
- Evaluate determinants,
- Find areas of triangles,
- Calculate minors and cofactors,
- Check consistency and solve linear systems by matrix methods,
- Miscellaneous proofs and applications.

---

## Summary

- Determinant is a unique number associated to any square matrix.
- Helps determine the uniqueness and existence of solutions of linear equation systems.
- Triangle area can be found using determinants.
- Minors and cofactors simplify expansions.
- Adjoint and inverse are useful for matrix equations.
- Consistency and solution properties depend on determinants.

---

## Historical Note

Early Chinese and Japanese mathematicians developed elimination methods similar to determinants. Laplace introduced systematic expansion; Lagrange, Gauss, Binet, Cauchy, and Jacobi contributed refinements and major results to the theory.
