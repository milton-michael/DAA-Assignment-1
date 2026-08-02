# DAA-Assignment-1
Insertion Sort Algorithm

Algorithm Steps:
1. Start with the second element assuming the first is already sorted.
2. Compare the current element with the sorted elements on its left.
3. Shift elements greater than the current element to the right.
4. Insert the current element in its correct place.
5. Repeat this until the array is completely sorted.

Sample Input and Output:
Input: [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
<img width="647" height="427" alt="image" src="https://github.com/user-attachments/assets/f2c90950-8f5a-4e99-9da8-e7901bb8c3da" />

Time Complexity:
Best Case: Ω(n) (When the array is already sorted)
Average Case: Θ(n^2) (When elements are in random order)
Worst Case: O(n^2) (When the array is in reverse order)

Space Complexity:
Space Complexity is O(1) because it sorts the array in-place without needing extra memory.
