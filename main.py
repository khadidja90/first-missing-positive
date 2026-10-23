"""First Missing Positive.

Given an unsorted integer array, return the smallest positive integer (n > 0)
that is not present in it.

Example:
    [0, -2, 1, 2] -> 3
"""


def first_missing_positive(nums):
    """O(n) time, O(1) extra space (cyclic sort).

    Note: this rearranges `nums` in place. Pass a copy if you need the
    original order preserved.
    """
    n = len(nums)

    # Place each value v (1 <= v <= n) at index v - 1.
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    # The first index holding the wrong value reveals the answer.
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # Array contains exactly 1..n, so the answer is n + 1.
    return n + 1


def first_missing_positive_set(nums):
    """O(n) time, O(n) space. Simpler, does not modify the input."""
    seen = set(nums)
    candidate = 1
    while candidate in seen:
        candidate += 1
    return candidate


def main():
    tests = [
        ([0, -2, 1, 2], 3),
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1, 1, 1], 2),
        ([1, 2, 3], 4),
        ([], 1),
        ([1], 2),
        ([2], 1),
    ]

    all_passed = True
    for nums, expected in tests:
        # Copy, because the cyclic-sort version modifies its input.
        result = first_missing_positive(list(nums))
        result_set = first_missing_positive_set(nums)
        ok = result == expected and result_set == expected
        all_passed &= ok
        print(f"{'PASS' if ok else 'FAIL'}  input={nums!s:<22} "
              f"expected={expected}  got={result}")

    print("\nAll tests passed." if all_passed else "\nSome tests failed.")


if __name__ == "__main__":
    main()
