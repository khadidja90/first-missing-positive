# First Missing Positive

Given an unsorted integer array `nums`, return the smallest positive integer
(`n > 0`) that is not present in `nums`.

**Example:** `[0, -2, 1, 2]` returns `3`, since `1` and `2` are already present.

## Approach

### Key idea

For an array of length `n`, the answer is always in the range `1` to `n + 1`.

By the pigeonhole principle, the array has only `n` slots, so it cannot hold
all `n + 1` candidates `1, 2, ..., n + 1`. At least one is missing. The answer
only reaches `n + 1` when the array is exactly `1, 2, ..., n`. Any zero,
negative, duplicate, or value greater than `n` wastes a slot, which forces a
gap inside `1..n`.

So values outside `1..n` can be ignored.

### Algorithm 1: Cyclic sort (`first_missing_positive`)

1. For each index `i`, while `nums[i]` is in `1..n` and is not already in its
   correct position, swap it to index `nums[i] - 1`.
2. Scan the array. The first index `i` where `nums[i] != i + 1` gives the
   answer `i + 1`.
3. If every position is correct, the answer is `n + 1`.

The check `nums[nums[i] - 1] != nums[i]` stops the loop on duplicates, so it
never loops forever. Each swap places one value permanently, so the total work
is O(n).

| | Complexity |
|---|---|
| Time | O(n) |
| Space | O(1) extra (modifies the input in place) |

### Algorithm 2: Hash set (`first_missing_positive_set`)

Put all values in a set, then count up from `1` until a number is not found.
Simpler, and it leaves the input untouched.

| | Complexity |
|---|---|
| Time | O(n) |
| Space | O(n) |

