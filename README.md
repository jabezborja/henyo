# Henyo
Henyo is an esoteric programming language inspired by Brainf*ck, an esoteric programming language too.

# Getting started
Try to run Henyo first. No framework. No other download. No gotchas. Just clone and run it. Henyo is created from raw Python 3.

To run Henyo:
`py henyo.py`

...and it will ask you what's the name of the file (henyo program [ends with `.hn`])

Input the name of the file and voila! The magic works.

If you still don't believe it's working. Try this:
```
[y++++{+}].>[y+{+}].>[y+++
+++++{+}].>[y++++++++{+}].>[yx+
{+}].>[xxx++{+}].>[yx+++++++++
{+}].>[yx+{+}].>[yx++++{+}].>[y
++++++++{+}].>[y{+}].
```

# How it works:
## Logic
Henyo consists of cells, 301 memory cells. Each cell has a 0 integer initial value which increments when you type "+".

Henyo has only 5 commands:
```
+ = increments the cell
- = decrements the cell
> = move to cell right
< = move to cell left
xy = loop expressions (x is 10, and y is 100)
```

Let's say we have:
`+++>++<+`\

So it works like this:\
We have 301 cells but the initial cell is in the middle, so it's at 150 cell.

But let's have 5 here:\

`[0][0][**0**][0][0]`\

The asterisks are the pointer. It points in the middle of the cells.

Once the compiler reads the "+", it will increment.\

`[0][0][**3**][0][0]`\

There are 3 "+" so it's 3.

Once the ">" comes in, it will move the pointer to right.\

`[0][0][3][**0**][0]`\

Increments by 2 because there are 2 "+"\

`[0][0][3][**2**][0]`\

And then go to left again with "<"\

`[0][0][**3**][2][0]`\

And increment by 1 because there is only 1 "+"\
`[0][0][**4**][2][0]`\

## Printing
So how's printing works? Glad you ask. So Henyo relies to ASCII for turning numbers into letters.

Example: The letter `a` in ASCII is 97 so you have to type 97 "+".

It's inefficient and we don't wanna put 97 "+" just to print the letter `a`. So I came up with a different idea of loop. I don't really understand how Brainf*ck loop's works so I created my own.

## Loops
So the start of the loop is the `[` or the bracket and the end is the left bracket or `]`.

So let's say we have:\
`[x++{+}]`

Now, it looks weird but it's cool (I guess).

So let's break in down into pieces.

Like I said above the x and y are loop expressions. X is 10 and Y is 100.

How many times will the loop will loop? In Henyo, there's no such thing as infinite, everything is finite.

So there's `X` in our case plus 2 which are the 2 "+" and it will loop 12 times.

Now the curly braces, what are those? Inside of those curly braces are what should Henyo do with the loop? Is it increment, decrement, or move left and right?

So inside of our curly brace is a "+" so where the current pointer is pointing will increment 12 times.

So:\
`[0][0][**12**][0][0]`\

What if different case?\
`[x++{-}]`\

It will decrement 12 times.

So:\
`[0][0][**-12**][0][0]`\

What about the ">" or "<"?\
`[x++{>}]`\

So it will jump 12 cells right and "<" left.

From:\
`[0][0][**0**][0][0]`\

To:\
`[0][0][-0-][0][0][0][0][0][0][0][0][0][0][0][**0**]`\
