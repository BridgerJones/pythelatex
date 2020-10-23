# Overview
Providing useful python commands to generate useful LaTex

## Commands

### base10
Usage `base10 [base] [number]`
Example: `base10 2 1110.1111` should return `(1 \times 2^3)+(1 \times 2^2)+(1 \times 2^1)+(0 \times 2^0)+(1 \times 2^{-1})+(1 \times 2^{-2})+(1 \times 2^{-3})+(1 \times 2^{-4})`.

This can then be inserted in LaTex Document in $$ or \begin{equation}...
