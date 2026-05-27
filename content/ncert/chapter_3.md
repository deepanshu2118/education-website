# Chapter 3: Matrices

> "The essence of Mathematics lies in its freedom." 
> - CANTOR

# 3.1 Introduction

The knowledge of matrices is necessary in various branches of mathematics. Matrices are one of the most powerful tools in mathematics. This tool simplifies work greatly compared to straightforward methods. The concept of matrices evolved to provide compact and simple methods for solving systems of linear equations. Their utility far exceeds representation of coefficients in such systems, being used in spreadsheets for budgeting, analyses, and applications in business, science, genetics, economics, sociology, psychology, industrial management, and cryptography. This chapter introduces fundamentals of matrix and matrix algebra.

# 3.2 Matrix

If someone possesses certain items (such as notebooks and pens), the information can be structured in a table and expressed using matrices.  
Example:  
- Notebooks: Radha has 15, Fauzia has 10, Simran has 13  
- Pens: Radha has 6, Fauzia has 2, Simran has 5

Arranged as a matrix:

|         | Notebooks | Pens  |
|---------|-----------|-------|
| Radha   | 15        | 6     |
| Fauzia  | 10        | 2     |
| Simran  | 13        | 5     |

**Definition 1:**  
A matrix is an ordered rectangular array of numbers or functions. The numbers of functions are called the elements or entries of the matrix. We denoted matrices by capital letters.

**Examples:**

<p>
\[
A = \left[
\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}
\right],  \quad
B = \left[
\begin{array}{ccc}
2+i & 3 & \tfrac{-1}{2} \\
3.5 & 6 & 3 \\
5 & 5 & 7
\end{array}
\right], \quad
C = \left[
\begin{array}{ccc}
x & x^3 & \cos{x} \\
\sin{x^2} & 3 & 1
\end{array}
\right]
\]
</p> 
<!-- <p>
\[
B = \left[
\begin{array}{ccc}
2+i & 3 & \tfrac{-1}{2} \\
3.5 & 6 & 3 \\
5 & 5 & 7
\end{array}
\right]
\]
</p>
<p>
\[
C = \left[
\begin{array}{ccc}
x & x^3 & \cos{x} \\
\sin{x^2} & 3 & 1
\end{array}
\right]
\]
</p> -->


Rows run horizontally, columns vertically.


### 3.2.1 Order of a Matrix

A matrix with \( m \) rows and \( n \) columns is an order $\( m \times n \)$ matrix.  
The total number of elements is \( mn \).

**General form:**

<p>
\[
A = \left[
\begin{array}{ccc}
a_{11} & a_{12} & ... & a_{1n} \\
a_{21} & a_{22} & ... & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & ... & a_{mn}
\end{array}
\right]
\]
</p>

### Using matrices for geometry

Consider a quadrilateral ABCD with vertices A(1,0), B(3,2), C(1,3), D(-1,2).
Now, quadrilateral ABCD in matrix form can be represented as 
<!-- \[
ABCD = \begin{bmatrix}
1 & 3 & 1 & -1 \\
0 & 2 & 3 & 2
\end{bmatrix}
\] -->


<p>
\[
X =
\left[\begin{array}{c}
    1 & 3 & 1 & -1 \\
    0 & 2 & 3 & 2
\end{array}
\right]_{2 \times 4} \quad or \quad  Y =
\left[\begin{array}{c}
    1 & 0 \\
    3 & 2 \\
    1 & 3 \\
    -1 & 2
\end{array}
\right]_{4 \times 2}
\]
</p>



**Example 1:**  
Represent worker counts in factories as a $\( 3 \times 2 \)$ matrix:

<p>
\[
A = \left[\begin{array}{c}
30 & 25 \\
25 & 31 \\
27 & 26
\end{array}
\right]_{3 \times 2}
\]
</p>


**Example 2:**   If a matrix has 8 elements, what are the possible orders it can have ? 

Possible orders for 8-element matrix:  
- $\( 1 \times 8 \)$, $\( 8 \times 1 \)$, $\( 2 \times 4 \)$, $ \( 4 \times 2 \)$

**Example 3:**  Construct a $\( 3 \times 2 \)$ matrix whose elements are given by  $a_{ij} = \frac{1}{2} |i - 3j| $.

**Solution:** In General a $\( 3 \times 2 \)$ matrix is given by  
<p>
\[
A = \left[\begin{array}{c}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}
\right]_{3 \times 2}
\]
</p>
Now, $a_{ij} = \frac{1}{2}|i-3j|, i=1,2,3$  and $ j = 1,2. $

Therefore $a_{11} = \frac{1}{2}|1-3 \times 1| = 1$ $\quad$ $a_{12} = \frac{1}{2}|1-3 \times 2| =\frac{5}{2}$

$a_{21} = \frac{1}{2}|2-3 \times 1| = \frac{1}{2}$ $\quad$ $a_{12} = \frac{1}{2}|2-3 \times 2| = 2$

$a_{31} = \frac{1}{2}|3-3 \times 1| = 0$ $\quad$ $a_{32} = \frac{1}{2}|3-3 \times 2| =\frac{3}{2}$

Hence the required matrix is given by 
<p>
\[
A = \left[\begin{array}{c}
1 & \frac{5}{2} \\
\frac{1}{2} & 2 \\
0 & \frac{3}{2}
\end{array}
\right]_{3 \times 2}
\]
</p>

# 3.3 Types of Matrices

- **Column matrix:** A matrix is said to be a column matrix if it has only one column.
for example   
<p>
\[
A = \left[\begin{array}{c}
1  \\
\frac{1}{2} \\
0 
\end{array}
\right]_{3 \times 1}
\]
</p>

<p>
In General,
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times 1}
\]
is a column matrix of order $m \times 1$.
</p>

- **Row matrix:** A matrix is said to be a row matrix if if has only one row.
for example   
<p>
\[
A = \left[\begin{array}{c}
1  & 2 & 7 & 3
\end{array}
\right]_{1 \times 4}
\]
</p>

<p>
In General,
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{1 \times n}
\]
is a row matrix of order $1 \times n$.
</p>

- **Square matrix:** A matrix in which the number of rows are equal to the number of the columns, is said to be a square matrix. Thus an $m \times n$ matrix is said to be a square matrix if m=n and is known as a sqaure matrix of order 'n'.

<p>
For example
\[
A = \left[\begin{array}{c}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 
\end{array}
\right]_{3 \times 3}
\]
is a square matrix of order 3.
</p>

<p>
In General,
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times m}
\]
is a sqaure matrix of order m.
</p>

Number of Row = Number of column

<p>
Note: If
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]
\]
is a sqaure matrix of order n, then elements(entries) $a_{11},a_{22},a_{33},.....,a_{nn}$ are said to constitute the diagonal, of the matix A.
</p>

- **Diagonal matrix:**  
<p>
A square matrix
\[
B = \left[\begin{array}{c}
b_{ij}
\end{array}
\right]_{m \times m}
\]
is said to be a diagonal matrix if all its non diagonal elemnets are zero, that is a matrix \[
B = \left[\begin{array}{c}
b_{ij}
\end{array}
\right]_{m \times m}
\] is said to be a diagonal matrix if $b_{ij}$=0 when $i \neq j$.
</p>

<p>
For example:
\[
A = \left[\begin{array}{c}
1 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 9 
\end{array}
\right]_{3 \times 3}, \quad
B = \left[\begin{array}{c}
1 & 0  \\
0 & 5  \\ 
\end{array}
\right]_{2 \times 2}, \quad
C = \left[\begin{array}{c}
5  
\end{array}
\right]_{1 \times 1}
\]
are diagonal matrices of order 3,2,1, respectively.
</p>

Square matrix where non-diagonal elements are zero.  

- **Scalar matrix:** A diagonal matrix is sadi to be a scaler matrix if its diagonal elements are equal, that is a square matrix 
<p>
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times m}
\]
is a said to be a scaler matrix if
</p>
$b_{ij} = 0$ When $i \neq j$ 

$b_{ij} = 0$ When i =j, for some constant k.


<p>
For example:
\[
A = \left[\begin{array}{c}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 
\end{array}
\right]_{3 \times 3}, \quad
B = \left[\begin{array}{c}
-1 & 0  \\
0 & -1  \\ 
\end{array}
\right]_{2 \times 2}, \quad
C = \left[\begin{array}{c}
5  
\end{array}
\right]_{1 \times 1}
\]
are scaler matrices of order 3,2,1, respectively.
</p>

Diagonal matrix where all diagonal elements equal.  

- **Identity matrix:**  A square matrix in which elements in the diagonal are all 1 and rest are all zero is called an identity matrix.
In other words, the square matrix 
<p>
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times m}
\] is an identity matrix, if
</p>
<p>
\[
a_{ij} =
\begin{cases}
1, & \text{if } i = j \\
0, & \text{if } i \neq j
\end{cases}
\]
</p>
We denote the identity matrix of order n by $I_{n}$. 
<p>
For example:
\[
A = \left[\begin{array}{c}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 
\end{array}
\right]_{3 \times 3}, \quad
B = \left[\begin{array}{c}
1 & 0  \\
0 & 1  \\ 
\end{array}
\right]_{2 \times 2}, \quad
C = \left[\begin{array}{c}
1
\end{array}
\right]_{1 \times 1}
\]
are identity matrices of order 3,2,1, respectively.
</p>

Observe that a scaler matrix is an identity matrix when k=1. But every identity matrix is clearly a scaler matrix.

Square matrix with diagonal elements 1, others zero. Denoted by \( I \).

- **Zero matrix:** A matrix is said to be zero matrix or null matrix if all its elements are zero.
<p>
For example:
\[
A = \left[\begin{array}{c}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 
\end{array}
\right]_{3 \times 3}, \quad
B = \left[\begin{array}{c}
0 & 0  \\
0 & 0  \\ 
\end{array}
\right]_{2 \times 2}, \quad
C = \left[\begin{array}{c}
0
\end{array}
\right]_{1 \times 1}
\]
are identity matrices of order 3,2,1, respectively.
</p>
We denote zero matrix by O. 

### 3.3.1 Equality of Matrices

**Definition 2:**  
Matrices A and B are equal if:

1. A and B both are Same order.

2. each element of A is equal to the corresponding element of B, that is $a_{ij}=b_{ij}$ for all i and j.

<p>
For example:
\[
\left[\begin{array}{c}
2 & 3  \\
0 & 1 \\
\end{array}
\right] and \quad
\left[\begin{array}{c}
2 & 3  \\
0 & 1  \\ 
\end{array}
\right]
\]
are equal matrices but 
</p>

<p>
\[
\left[\begin{array}{c}
2 & 3  \\
0 & 1 \\
\end{array}
\right] and \quad
\left[\begin{array}{c}
2 & 3  \\
1 & 0  \\ 
\end{array}
\right]
\]
are not equal matrices. Symbolically, if two matrices A and B are equal, we write A = B. 
</p>

**Example 4:**  

<p>
\[
\left[\begin{array}{c}
x+3 & z+4 & 2y-7  \\
-6 & a-1 & 0 \\
b-3 & -21 & 0
\end{array}
\right] = \quad
\left[\begin{array}{c}
0 & 6 & 3y-2  \\
-6 & -3 & 2c+2  \\ 
2b+4 & -21 & 0
\end{array}
\right]
\]
Find the values of a,b,c,x,y and z.
</p>

**Solution:** 
As the given matrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get
$x+3=0$,
$z+4=6$,
$2y-7=3y-2$,
$a-1=-3$,
$0=2c+2$,
$b-3=2b+4$

Simplifying, we get
$a = -2$,
$b = -7$,
$c = -1$,
$x = -3$,
$y = -5$,
$z = 2$


# 3.4 Operations on Matrices

### 3.4.1 Addition of Matrices

Sum is defined only if both matrices have the same order.

<p>
In general, if 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times m}
\] 
</p>
and 
<p> 
\[
B = \left[\begin{array}{c}
b_{ij}
\end{array}
\right]_{m \times m}
\] 
</p>
are two matrices of the same order, say $ m \times n$. Then the sum of the two matrices A and B is defined as a matrix 
<p> 
\[
C = \left[\begin{array}{c}
c_{ij}
\end{array}
\right]_{m \times m}
\] 
</p>
Where $c_{ij}= a_{ij} + b_{ij}$, for all possible values of i and j.

**Example 6:**  
<p>
\[
A = \left [ \begin{array}{c}
 3 & 1 & 2 \\ 
 5 & 2 & 3 \end{array}
 \right], \quad
B = \left [ \begin{array}{c}
1 & 2 & 3 \\ 
2 & 3 & 0 \end{array}
\right]
\]  
</p>

<p>
\[
A + B = \left [ \begin{array}{c}
 3+1 & 1+2 & 2+3 \\ 
 5+2 & 2+3 & 3+0
\end{array}
\right] = \quad
\left [\begin{array}{c}
4 & 3 & 5 \\
7 & 5 & 3
\end {array}
\right]
\]
</p>

#### Properties of Matrix Addition

- **Commutative:**  A + B = B + A 
- **Associative:**  (A + B) + C = A + (B + C) 
- **Additive identity:** Zero matrix \( O \), is the additive identity. 

    So,  A + O = A = O + A

- **Additive inverse:** If A is a matrix then -A is the additive inverse of the matrix A.

    So, A + (-A) = O = -A + A

### 3.4.2 Scalar Multiplication

In general, we may define multiplication of a matrix by a scaler as follows: if 
<p> 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
is a matrix and K is scaler, then KA is another matrix which is obtained by multiplying each element of A by the scaler K.

In other words 
<p> 
\[
KA = K\left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n} = \quad
\left[\begin{array}{c}
K(a_{ij})
\end{array}
\right]_{m \times n}
\] 
</p>
that is (i,j)th element of KA is $ka_{ij}$ for all possible values of i and j.

Multiply each matrix element by a scalar value.

<p>
For example:
\[
A=\left[\begin{array}{c}
1 & 2 & 3  \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}
\right]
\]
then
</p>

<p>
\[
3A=3\left[\begin{array}{c}
1 & 2 & 3  \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}
\right] = \quad

\left[\begin{array}{c}
3 & 6 & 9  \\
12 & 15 & 18 \\
21 & 24 & 27
\end{array}
\right]
\] 
</p>

### 3.4.3 Difference of Matrices
<p> 
If
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n} \quad,

B = \left[\begin{array}{c}
b_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
are two matrices of the same order then difference A-B is defined as a matrix 
<p>
\[
D = \left[\begin{array}{c}
d_{ij}
\end{array}
\right]_{m \times n}
\]
</p>
Where $d_{ij}=a_{ij}-b_{ij}$ for all value of i and j.

Defined like addition: subtraction is element-wise for matrices of the same order.

### 3.4.4 Properties of Scalar Multiplication

<p> 
If
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n} \quad,

B = \left[\begin{array}{c}
b_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
are two matrices of the same order and k and l are scalers, then

-  (k + l)A = kA + lA 
-  k(A + B) = kA + kB , $\quad$ k  scalar
-  k(lA) = (kl)A 

**Example 8:**  

<p>
If
\[
A = \left [ \begin{array}{c}
 8 & 0  \\ 
 4 & -2 \\
 3 & 6\end{array}
 \right], and \quad
B = \left [ \begin{array}{c}
2 & -2  \\ 
4 & 2  \\ 
-5 & 1\end{array}
\right]
\] 
then find the matrix X such that 2A + 3X = 5B.
</p>

**Solution:**
We have  2A + 3X = 5B

2A + 3X - 2A = 5B - 2A   

2A - 2A + 3X = 5B - 2A   $\quad $ (Matrix addition is commutative)$\quad$ (-2A is the additive inverse of 2A)

O + 3X = 5B -2A  $\quad $ (Matrix addition is commutative) 

3X = 5B - 2A $\quad$ (O is the additive identity)

X = $\frac{1}{3}$(5B - 2A)
<p>
\[
X = \frac{1}{3} \left( 5\left [ \begin{array}{c}
 2 & -2  \\ 
 4 & 2 \\
 -5 & 1\end{array}
 \right] - 
 2\left [ \begin{array}{c}
8 & 0  \\ 
4 & -2  \\ 
3 & 6\end{array}
\right] \right)
\] 
</p>
<p>
\[
X = \frac{1}{3} \left( \left [ \begin{array}{c}
 10 & -10  \\ 
 20 & 10 \\
 -25 & 5\end{array}
 \right] + 
 \left [ \begin{array}{c}
-16 & 0  \\ 
-8 & 4  \\ 
-6 & -12\end{array}
\right] \right)
\] 
</p>
<p>
\[
X = \frac{1}{3}\left [ \begin{array}{c}
 10-16 & -10+0  \\ 
 20-8 & 10+4 \\
 -25-6 & 5-12 \end{array}
 \right] 
\] 
</p>
<p>
\[
X = \frac{1}{3}\left [ \begin{array}{c}
 -6 & -10  \\ 
 12 & 14 \\
 -31 & -7 \end{array}
 \right] 
\] 
</p>
<p>
\[
X = \left [ \begin{array}{c}
 -2 & \frac{-10}{3}  \\ 
 4 & \frac{14}{3} \\
 \frac{-31}{3} & \frac{-7}{3} \end{array}
 \right] 
\] 
</p>


### 3.4.5 Multiplication of Matrices

The product of two matrices A and B is defined if the number of columns of A is equal to the number of rows of B.
<p> 
If
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n}  and \quad,
B = \left[\begin{array}{c}
b_{jk}
\end{array}
\right]_{n \times p}
\] 
are two matrix.
</p>
Then the product of the matrices A and B is the matrix C of order $m \times p$. To get the $(i,k)^{th}$ element $c_{ik}$ of the matrix C, we take the $i^{th}$ row of A and $k^{th}$ of column of B, multiply them elementwise and take the sum of all these products. 

In other words, if 
<p> 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n} \quad,

B = \left[\begin{array}{c}
b_{jk}
\end{array}
\right]_{n \times p}
\] 
</p>
then the $i^{th}$ row of A is 
<p>
\[
\left [ \begin{array}{c}
 a_{i1} & a_{i2} & a_{i3} & ... & a_{in}   
 \end{array}
 \right] 
\] 
</p>
and the $k^{th}$ column of B is 
<p>
\[
\left [ \begin{array}{c}
 b_{1k} \\
 b_{2k} \\
 b_{3k} \\
 . \\
 . \\
 . \\
 b_{nk}
 \end{array}
 \right] 
\] 
</p>
then $c_{ik}= a_{i1}b_{1k} + a_{i2}b_{2k} + a_{i3}b_{3k} + ..... + a_{in}b_{nk} $ = $\sum a_{ij}b_{jk}$

The matrix 
<p> 
\[
C = \left[\begin{array}{c}
c_{ik}
\end{array}
\right]_{m \times p} 
\] 
is the product of A and B.
</p>

In General matrix multiplication is not commutative. i.e  $\( AB \neq BA \)$

Zero matrix as the product of two non zero matrices.
we know that, for real number a,b if ab = 0, then either a = 0 or b = 0. This need not be true for matrices.

**Example**
Find AB, if 
<p>
\[
A = \left [ \begin{array}{c}
 0 & 1  \\ 
 0 & 2\end{array}
 \right], and \quad
B = \left [ \begin{array}{c}
2 & -2  \\ 
0 & 0 
\end{array}
\right]
\] 
</p>

**Solution**

<p>
\[
AB = \left [ \begin{array}{c}
 0 & 1  \\ 
 0 & 2 \end{array}
 \right]
\left [ \begin{array}{c}
2 & -2  \\ 
0 & 0 
\end{array}
\right] = \quad
\left [ \begin{array}{c}
0 & 0  \\ 
0 & 0 
\end{array}
\right]
\] 
</p>

#### Properties of Matrix Multiplication

- **Associative:**  (AB)C = A(BC) 
- **Distributive:** 

(i) A(B+C) = AB + AC 

(ii) (A+B)C = AC + BC

- **Multiplicative identity:** 

For every square matrix A, there exist an identity matrix of same order such that IA = AI = A.

# 3.5 Transpose of a Matrix

<p> 
If
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
then the matrix obtained by interchanging the rows and columns  of A is called the transpose of A. Transpose of the matrix A is denoted by $A^{'}$ or $A^{T}$.

**Example:**

if 
<p>
\[
A=\left[\begin{array}{c}
1 & 2   \\
4 & 5  \\
7 & 8 
\end{array}
\right]_{3 \times 2}
\]
</p>
then
<p>
\[
A=\left[\begin{array}{c}
1 & 4 & 7  \\
2 & 5 & 8  \\
\end{array}
\right]_{2 \times 3}
\]
</p>

**Properties:**

- $ (A^T)^T = A $

- $ (kA)^T = kA^T$   $\quad$ for scalar  k

- $ (A + B)^T = A^T + B^T $

- $ (AB)^T = B^T A^T $

# 3.6 Symmetric and Skew Symmetric Matrices

- **Symmetric:**  A square matrix 
<p> 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
is said to be symmetric if $A^T = A$, that is $a_{ij}$ = $a_{ji} for all possible values of i and j. 

$A^T = A$ 

**Example**

<p>
\[
A=\left[\begin{array}{c}
1 & 4 & 7  \\
4 & 5 & 8 \\
7 & 8 & 9  
\end{array}
\right]_{3 \times 3}
\]
</p>
is a symmetric matrix as $A^T = A$

- **Skew-symmetric:**  A square matrix 
<p> 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times n}
\] 
</p>
is said to be skew symmetric matrix if $A^T = -A $ that is $a_{ij}$ = - $a_{ji}$ for all possible values of i and j. Now if we put i = j, we have $a_{ii}$ = - $a_{ii}$ . Therefore 2$a_{ii}$ = 0 or $a_{ii}$ = 0 for all i's.

This means that all the diagonal elements of a skew symmetric martix are zero.

**Example:**

<p>
\[
A=\left[\begin{array}{c}
0 & 4 & 7  \\
-4 & 0 & 8 \\
-7 & -8 & 0  
\end{array}
\right]_{3 \times 3}
\]
</p>
is a skew symmetric matrix as $A^T = -A $.

**Theorem 1**

For any square matrix A with real number entries, $A + A^T$ matrix and $A - A^T$ is a skew symmetric matrix.

**Proof:**

Let $ B = A +$ $A^T$

$B^T$ = $(A+A^T)^T$

$B^T$ = $A^T$ + $(A^T)^T$  $\quad$ as $(A+B)^T = A^T + B^T$

$B^T$  = $A^T + A $  $\quad$ as $(A^T)^T = A$

$B^T$ = $ A + A^T $  $\quad$ as $(B + A) = (A+ B) $

$B^T$  = $B$ 

Therefore $B = A + A^T$ is a symmetric matrix

Now let  $C = A - A^T$

$C^T = (A - A^T)^T$ = $A^T -(A^T)^T $

$C^T = A^T - A $ 

$C^T = -(A - A^T) = - C $

Therefore   $C = A - A^T $ is a skew symmetric matrix.


**Theorem 2**

For any square matrix can be expressed as the sum of a symmetric and a skew-symmetric matrix.

**Proof:** Let A be a square matrix, then we can matrix

$A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T)
$
From the Theorem 1, we know that $(A+A^T)$ is a symmetric matrix and $(A_A^T)$ is a skew symmetric matrix. Since for any matrix A, $(kA)^T = kA^T$, it follow that $\frac{1}{2}(A+A^T)$ is a symmetric matrix and $\frac{1}{2}(A-A^T)$ is skew symmetric matrix. Thus any square matrix can be expressed as the sum of a symmetric and a skew symmetric matix.

# 3.7 Invertible Matrices

A square matrix  A of order m and if there exists another square matrix B of the same order m, such that AB = BA = I, then B is called the inverse matrix of A and it is denoted by $A^{-1}$. In that case A is said to be invertible. 

**Example**
<p>
\[
A=\left[\begin{array}{c}
2 & 3   \\
1 & 2   
\end{array}
\right]
 \quad and \quad
B=\left[\begin{array}{c}
2 & -3   \\
-1 & 2   
\end{array}
\right]
\]
be two matrices.
</p>
Now
<p>
\[
AB=\left[\begin{array}{c}
2 & 3   \\
1 & 2   
\end{array}
\right]
\left[\begin{array}{c}
2 & -3   \\
-1 & 2   
\end{array}
\right]
\]
</p>
<p>
\[
AB=\left[\begin{array}{c}
4-3 & -6+6   \\
2-2 & -3+4   
\end{array}
\right] \quad = \quad
\left[\begin{array}{c}
1 & 0   \\
0 & 1   
\end{array}
\right] \quad = \quad I
\]
</p>
Also
<p>
\[
BA=\left[\begin{array}{c}
1 & 0   \\
0 & 1   
\end{array}
\right] \quad = \quad I
\]
</p>
Thus B is the inverse of A, in other words $B = A^{-1}$ and A is inverse of B, i.e. $A = B^{-1}$

**Note:**

1. A rectangular matrix does not posses inverse matrix, since for products BA and AB to be defined and to be equal, it is necessary that matrices A and B should be square matrices of the same order.

2. If B is the inverse of A, then A is also the inverse of B.

**Theorem 3** (Uniqueness of inverse) Inverse of a square matrix, if it exists, is unique.

**Proof** Let
<p> 
\[
A = \left[\begin{array}{c}
a_{ij}
\end{array}
\right]_{m \times m}
\] 
</p>
be a square matrix. If possible, let B and C be two inverse of A. we shall that B = C.

Since B is the inverse of A

AB = BA = I    --------(1)

Since C is also the inverse of A

AC = CA = I    --------(2)

Thus   B = BI = B(AC) = BA(C) = IC = C 

**Theorem 4**

If A and B are invertible matrices of the same order, then $(AB)^{-1} = B^{-1}A^{-1}.$

**Proof** From the definition of inverse of a matrix, we have

$(AB)(AB)^{-1} = I$

$A^{-1}(AB)(AB)^{-1} = A^{-1}I$  $\quad$ pre multiplying both sides by $A^{-1}$

$(A^{-1}A)(AB)^{-1}  = A^{-1} $  $\quad$ Since $A^{-1}I = A^{-1}$

$IB(AB)^{-1} = A^{-1}$

$B(AB)^{-1} = A^{-1}$

$B^{-1}B(AB)^{-1} = B^{-1}A^{-1}$

$I(AB)^{-1} = B^{-1}A^{-1} $ 

Hence

$(AB)^{-1} = B^{-1}A^{-1}$

# Summary

- Matrices are ordered rectangular arrays of numbers or functions.
- Square, diagonal, scalar, identity, zero, row, and column matrices are defined by structure.
- Operations include: addition, scalar multiplication, subtraction, product, and transpose.
- Matrix equations and properties are widely used in basic and advanced mathematics.

# Exercises

Several exercises and examples are provided throughout the chapter, including:
- Constructing matrices of given orders
- Solving equations involving matrices
- Proving properties of matrix addition and multiplication
- Finding transpose, symmetric and skew-symmetric matrices
- Solving real-world applications through matrix algebra
