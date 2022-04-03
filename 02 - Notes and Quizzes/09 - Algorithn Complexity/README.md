# Algorithm Complexity
* Read and interpret `pseudocode`
* Describe `worst-case analysis`
* Correctly use “`Big-O`”, “`Big-Theta`”, and “`Big-Omega`” notation
* Recognize constant, *linear*, *logarithmic*, *polynomial*, *exponential*, and *factorial* `growth rates`
* Explain the problem sets `P`, `NP`, `NP-complete`, and `NP-hard`
* Discuss the `importance of the P=NP` question

---
<br>

<img src = "Images/bigOOverview.png" width = 500>

---

### ***Algorithm*** Complexities
Sorting Algorithm| Best: Time | Average: Time | Worst: Time | Worst: Space
-|-|-|-|-
`quick`| Ω(n log(n)) | Θ(n log(n)) | O(n^2) | O(log(n))
`merge`| Ω(n log(n)) | Θ(n log(n)) | O(n log(n)) | O(n)
`bucket`| Ω(n+k) | Θ(n+k) | O(n^2) | O(n)
`radix`| Ω(nk) | Θ(nk) | O(nk) | O(n+k)
`heap`| Ω(n log(n)) | Θ(n log(n)) | O(n log(n)) | O(1)
`tim`| Ω(n) | Θ(n log(n)) | O(n log(n)) | O(n)
`bubble`| Ω(n) | Θ(n^2) | O(n^2) | O(1)
`insertion`| Ω(n) | Θ(n^2) | O(n^2) | O(1)
`selection`| Ω(n^2) | Θ(n^2) | O(n^2) | O(1)
`tree`| Ω(n log(n)) | Θ(n log(n)) | O(n^2) | O(n)
`shell`| Ω(n log(n)) | Θ(n(log(n))^2) | O(n(log(n))^2) | O(1)
`counting`| Ω(n+k) | Θ(n+k) | O(n+k) | O(k)
`cube`| Ω(n) | Θ(n log(n)) | O(n log(n)) | O(n)


### `Heaps`
Type|Insert|findMin|findMax|removeMin|removeMax
-|-|-|-|-|-
`Min` Heap      | O(log(n))| O(n)| x   | O(log(n)) | x
`Max` Heap      | O(log(n))| x   | O(1)| x         | O(log(n))
`Min-Max` Heap  | O(log(n))| O(1)| O(1)| O(log(n)) | O(log(n))
`Deap`          | O(log(n))| O(1)| O(1)| O(log(n)) | O(log(n))

### `Binary Search Trees`
Type|Create|Insert|Sort
-|-|-|-
`BST` |O(n^2)|O(n^2)|O(n^2)