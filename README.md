# Prime-Search-Algorithm
An algorithm that makes prime numbers, base+prime, by utilizing the lines that form when you look at the base as a matrix, and improved efficiency of higher bases that are made from a combination of the lowest value primes. 

In Base 10 [2\*5] 
> they will appear in [1, 3, 7, 9] (4/10 = 40% of all numbers in base 10)

In Base 6 [2\*3] 
> they will appear in [1, 5] (2/6 = 33.34% of all numbers in base 6)

In Base 30 [2\*3\*5] 
> they will appear in [1, 7, 11, 13, 17, 19, 23, 29] (8/30 = 26.67% of all numbers in base 30)

Why do they appear like this? lets take a look at Base 10, and Base 6 as an example.

## Base 10
|Int|Composite|In Base[2, 5]|
|-|-|-|
|0/10|2\*5|true|
|1|Prime|false => line|
|2|Prime|true|
|3|Prime|false => line|
|4|2\*2|true|
|5|Prime|true|
|6|3\*2|true|
|7|Prime|false => line|
|8|2\*2\*2|true|
|9|3\*3|false => line|

## Base 6
|Int|Composite|In Base[2, 3]|
|-|-|-|
|0|2\*3|true|
|1|Prime|false => line|
|2|Prime|true|
|3|Prime|true|
|4|2\*2|true|
|5|Prime|false => line|


Pattern exmple: In Base 30 [2, 3, 5], lines form at [1, ~~2~~, ~~3~~, ~~5~~, 7, 11, 13, 17, 19, 23, 29] and not on any primes that are included inside the base. And in Base 210 [2, 3, 5, 7] we will beginn to see what happened to 3 again (in base 10) 11\*11=121 and 11 is not included in the base, therefore a line will form from it.

But there is still one other issue. The lines are just potential primes.
If you write base 6 and base 30 down and add values in just the lines you will see primes, and another pattern of non primes.
these nonprimes have composites made only from primes that are not in the base.
Example: base 6 [2, 3] - 5x5=25, 5x7=30...  7x7=49... and so on. This means we have a pattern, and we need to make a blacklist function to remove them.

|Base|Lines|Lines/Base|
|-|-|-|
|6|2|33,33%|
|30|8|26,67%|
|210|47|22,38%|
|2310|478|20,69%|

As we can see over higher bases produces more lines, but the ratio of lines compared to all numbers means we check less numbers in total for each iteration. The only issue is that we need all primes, and nonprimes that form lines, that have a value less than the next base in order to change to a more efficient base.
