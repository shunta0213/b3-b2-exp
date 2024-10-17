# My LaTeX Project Templates

Use with Visual Studio Code, Dev Container

Features
- lualatex
- some pre-defined sections
- pre-commit hook to format, lint, etc.


## Snippets Usage

Both dynamic and static snippets are available with vscode inhereted snippets and [Hyper Snips](https://marketplace.visualstudio.com/items?itemName=draivin.hsnips).

The list of the snippets


| Trigger |  Snippet  | Description             |
| :-----: | :-------: | :---------------------- |
|   ;;    |  \\( \\)  | inline math environment |
|   tit   | \textit{} | italic                  |
|   tbf   | \textbf{} | bold                    |

In the math envrionment,
|   Trigger   |       Snippet        | Description                                                                                                                                                                                                                                        |
| :---------: | :------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     10/     |     \drac{10}{}      | insert dfrac (fraction). when the denominator has the parentheses, they will be removed.                                                                                                                                                           |
|   (10)rt    |      \sqrt{10}       | insert square root. higher root is also possible with the below snippet.                                                                                                                                                                           |
| \sqrt{10}3  |     \sqrt[3]{10}     | make the square root to the n-th root.                                                                                                                                                                                                             |
|     div     |         \div         | le, ge, div, to, not, in, sup, dim, deg, ker, range, grad, rot, Div, rank, diag, det, arg, max, min, argmax, argmin, sin, cos, tan, cot, ln, log, exp, perp, cup, cap, sim, pm, iff, mind, Im, Re, succ, prec, circ, neq, ni, lim, sum, prod const |  |
|     za      |        \alpha        | convert za to \alpha, zb to \beta etc.                                                                                                                                                                                                             |
|     lr)     |    \left( \right)    | add braces                                                                                                                                                                                                                                         |
|     R#      |      \mathbb{R}      | Black Board                                                                                                                                                                                                                                        |
|    Acal     |     \mathcal{A}      | Caligraphy                                                                                                                                                                                                                                         |
|     A@      |       \mathscr       | Script                                                                                                                                                                                                                                             |
| \mathbb{A}# |     \mathcal{A}      | \mathbb → \mathcal → \mathscr → \mathbb                                                                                                                                                                                                            |
|     ^^      |         ^{}          | superscript                                                                                                                                                                                                                                        |
|     __      |         _{}          | subscript                                                                                                                                                                                                                                          |
|     sq      |          ^2          | square                                                                                                                                                                                                                                             |
|     cb      |          ^3          | cubic                                                                                                                                                                                                                                              |
|     x1      |         x_1          | convert to subscript automatically                                                                                                                                                                                                                 |
|   ubrace    | \underbrace{$1}_{$2} | underbrace                                                                                                                                                                                                                                         |
|     dsp     |    \displaystyle     | displaystyle                                                                                                                                                                                                                                       |
