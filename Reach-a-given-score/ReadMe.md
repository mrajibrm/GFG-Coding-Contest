# Reach a given score


Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

### Example 1:

``Input`` <br>
``n = 10`` <br>
``Output``  <br>
``2`` <br>
***Explanation :*** <br>
There are two ways: $ \{5,5\} ~~\& ~~{10}$. <br>

### Example 2:

``Input``<br>
``n = 20`` <br>
``Output`` <br>
``4`` <br>
***Explanation :*** <br>
There are four possible ways:$ \{5,5,5,5\},~~\{3,3,3,3,3,5\},~~ \{10,10\},~~ \{5,5,10\}$. <br>

## Task:  
Write the function ``count( )`` which takes ``n`` as input parameter and returns the answer to the problem. <br>

**Expected Time Complexity :** $~~O(n)$ <br>
**Expected Auxiliary Space :** $~~O(n)$ <br>

*Constraints:*

$1 ≤ n ≤ 10^6$