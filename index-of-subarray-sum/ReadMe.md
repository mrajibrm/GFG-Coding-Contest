# Find Indexes of a subarray with given sum

Given an unsorted ``array`` ``A`` of ``size`` ``N`` that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

**Note :-** Code needs to return an ``ArrayList`` consisting of two elements left and right. In case no such subarray exists return an array consisting of element ``-1``.

### Example 1:

``Input:`` <br>
``N = 5, S = 12`` <br>
``A[] = {1,2,3,7,5}`` <br>

``Output:`` <br>
``2 4`` <br>

***Explanation :*** <br> The sum of elements 
from $2nd$ position to $4th$ position 
is $12$.


### Example 2:

``Input:`` <br>
``N = 10, S = 15`` <br>
``A[] = {1,2,3,4,5,6,7,8,9,10}`` <br>

``Output:`` <br> ``1 5`` <br>
***Explanation :*** <br>
The sum of elements 
from $1st$ position to $5th$ position
is $15$.

## Task:
Write the function ``subarraySum()`` which takes ``arr, N,`` and ``S`` as input parameters and returns an ``ArrayList`` containing the starting and ending positions of the first such occurring subarray from the left where sum equals to ``S``. The two indexes in the array should be according to $1$-based indexing. If no such subarray is found, return an array consisting of only one element that is $-1$.

**Expected Time Complexity :** $ O(N)$ <br>
**Expected Auxiliary Space :** $ O(1)$

*Constraints:* <br>
$1 <= N <= 10^5$ <br>
$0 <= A_i <= 10^9$ <br>
$0<= S <= 10^9$