# Fundamental Algorithms
Algorithms treated under this section are classified as "fundamental" based on the level of implementation 
difficulty. Please note, this label is entirely subjective and must not be treated as a generic convention. 
Time and space complexity are quantified using the **Big Oh Notation**, this quantity enables the programmer 
estimate the cost of their program runtime at the backdrop of available computing resources.
The notation has origin from the discipline of mathematics.
## Search
### Linear Search
Linear search also termed as a sequential search is a relatively simple search algorithm that traverses through a collection/data structure.  
It steps through each space in the structure and compares the elements there with the desired search target.  
**Big OH: O(N)**  
![ls_img](https://cdn.programiz.com/sites/tutorial2program/files/linear-search-found.png)  
Image Credit: _Programmiz_

### Sentinel Linear Search
Sentinel linear is a variant of linear search where the number of comparison in reduced compared to 
traditional linear search. The basic idea behind this algorithm is to add a sentinel to the end of 
the array which is equal to the target value we are looking for.This helps to avoid checking the array
boundary condition during each iteration of the loop, as the sentinel acts as the stopper for the loop.  
**Big OH: O(N)**  

### Binary Search
Don't think much, reduce the search space of the array by half at each iteration and perform
search comparison,that is all, you've made yourself the binary search algorithm.
The binary search algorithm is efficient and effective yet simple to implement.  
**Big OH: Log(N)**  
![binary_search_image](https://media.geeksforgeeks.org/wp-content/uploads/20220309171621/BinarySearch.png)  
Image Credit: _Geeks for Geeks_
## Sort