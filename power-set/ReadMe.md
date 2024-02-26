# Power Set


Given a string ``s`` of length ``n``, find all the possible subsequences of the ``string s`` in lexicographically-sorted order.

### Example 1:

``Input :`` <br> 
``s = "abc"`` <br>
``Output:`` <br>
``a ab abc ac b bc c`` <br>
***Explanation :*** <br>
There are a total 7 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.


### Example 2:

``Input :`` <br>
``s = "aa"`` <br>
``Output : `` <br>
``a a aa`` <br>
***Explanation :*** <br>
There are a total 3 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.

## Task:
Write the function ``AllPossibleStrings()`` which takes a ``string s`` as the input parameter and returns a list of all possible subsequences (non-empty) that can be formed from ``s`` in lexicographically-sorted order.

**Expected Time Complexity :** <br> $O( n*2^n  )$ <br>
**Expected Space Complexity :** <br> $O( n * 2^n )$

*Constraints :* <br>
$1 <= n <= 16$ <br>
``s`` will constitute of lower case english alphabets