# Distinct occurrences

- Given two `strings` `s` and `t` of length ``n`` and ``m`` respectively. Find the count of distinct occurrences of t in s as a sub-sequence $modulo$ $10^9 + 7$

### Example 1:

``Input:``<br>
``s = "banana" , t = "ban"``<br>
``Output: ``<br>
``3`` <br>
***Explanation:***<br>
There are 3 sub-sequences:``[ban], [ba n], [b an]``.

### Example 2:

``Input:`` <br>
``s = "geeksforgeeks" , t = "ge"`` <br>
``Output: `` <br>
``6`` <br>
***Explanation:*** <br>
There are 6 sub-sequences:``[ge], [ge], [g e], [g e] [g e] and [g e]``.

## Task:
Write a function which takes two ``strings`` as argument ``s`` and ``t`` and returns the count of the sub-sequences $modulo$  $10^9 + 7.$

**Expected Time Complexity :**  $O(n*m)$. <br>
**Expected Auxiliary Space :** $O(n*m)$.

*Constraints :* <br>
$1 ≤ n,m ≤ 1000$

