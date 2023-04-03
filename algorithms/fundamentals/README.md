# Fundamental Algorithms
Algorithms treated under this section are classified as "fundamental" based on the level of implementation 
difficulty. Please note, this label is entirely subjective and must not be treated as a generic convention. 
Time and space complexity are quantified using the **Big Oh Notation**, this quantity enables the programmer 
estimate the cost of their program runtime at the backdrop of available computing resources.
The notation has origin from the discipline of mathematics.
## Search
Search for items in a defined space has existed pre-stone age, objects and data representations defined in collections
in computer science are not new this concept. The conventional data structures allows the freedom to look for data in 
a systematic order. There are a handful basic search algorithm established in computer science, and we are going to treat
in under this section. :hamster:
#### Linear Search
Linear search also termed as a sequential search is a relatively simple search algorithm that traverses through a 
collection/data structure.  
It steps through each space in the structure and compares the elements there with the desired search target.  
**BIG O: O(N)**  

#### Sentinel Linear Search
Sentinel linear is a variant of linear search where the number of comparison in reduced compared to 
traditional linear search. The basic idea behind this algorithm is to add a sentinel to the end of 
the array which is equal to the target value we are looking for.This helps to avoid checking the array
boundary condition during each iteration of the loop, as the sentinel acts as the stopper for the loop.  
**BIG O: O(N)**  

#### Binary Search
Don't think much, reduce the search space of the array by half at each iteration and perform
search comparison,that is all, you've made yourself the binary search algorithm.
The binary search algorithm is efficient and effective yet simple to implement.  
**BIG O: Log(N)**  

## Sort
#### Bubble Sort

#### Insertion Sort
#### Merge Sort
#### Quick Sort
#### Selection Sort
