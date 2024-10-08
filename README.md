### Matrix multiplication problem by ChapGPT

### Task:
You are given two matrices `A` and `B` (both of size `n x n`), and an integer `k`. Your task is to perform matrix multiplication and then extract all the values from the resulting matrix that are divisible by `k`, but only if the value is greater than a given threshold.

### Details:
- `A` and `B` are two matrices represented as lists of lists (2D lists), where each matrix element is an integer.
- The multiplication of two matrices `A` (size `n x n`) and `B` (size `n x n`) results in a matrix `C` (size `n x n`).
- The formula for matrix multiplication is:

  \[
  C_{ij} = \sum_{p=0}^{n-1} A_{ip} \times B_{pj}
  \]

  where \(C_{ij}\) is the element in row `i` and column `j` of the resulting matrix `C`.

- After computing the resulting matrix `C`, you need to filter out the elements that:
  - Are divisible by `k`.
  - Are greater than a given threshold `t`.

### Input:
- The integer `n` representing the size of the matrices.
- Matrix `A` of size `n x n`.
- Matrix `B` of size `n x n`.
- Integer `k` (divisibility factor).
- Integer `t` (threshold value).

### Output:
A list of the values that meet the criteria (divisible by `k` and greater than `t`), sorted in ascending order.

