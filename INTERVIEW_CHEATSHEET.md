# Coding Assessment Cheatsheet: Core Patterns

Python-focused recap for the 22 practiced NeetCode problems.

## 30-second pattern picker

| If the prompt asks for... | Reach for... | Key idea |
|---|---|---|
| duplicate / membership / lookup | `set` | Store what has been seen |
| counts / frequencies | `dict` or `Counter` | Map value → count |
| pair summing to target (unsorted) | hash map | Look for `target - x` before storing `x` |
| pair summing to target (sorted) | two pointers | Sum too small → left++; too large → right-- |
| groups with the same composition | hashable signature | Map signature → group |
| top `k` by frequency | buckets | Frequency is bounded by `n` |
| all values except current index | prefix + suffix | Combine information from both sides |
| consecutive values, unordered input | set + sequence starts | Expand only when `x - 1` is absent |
| compare from both ends | opposite pointers | Maintain an answer over `[left, right]` |
| unique triplets | sort + fixed value + two pointers | Skip duplicates at both levels |
| best area between two boundaries | greedy two pointers | Move the shorter boundary |
| longest/best contiguous range | sliding window | Expand right; shrink left when invalid |
| properly nested pairs | stack | A closer must match the latest opener |
| sorted or rotated-sorted search | binary search | Prove which half can be discarded |
| linked-list midpoint/cycle | slow + fast pointers | Fast moves twice as quickly |
| linked-list head deletion | dummy node | Make head and non-head cases identical |

## Core tools

```python
# Membership / uniqueness: average O(1)
seen = set()
if x in seen: ...
seen.add(x)

# Frequency map
count = {}
count[x] = count.get(x, 0) + 1

# Grouping
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(value)

# Fixed alphabet frequency signature (lowercase a-z)
signature = [0] * 26
for ch in word:
    signature[ord(ch) - ord("a")] += 1
key = tuple(signature)       # lists cannot be dictionary keys

# Opposite pointers
left, right = 0, len(values) - 1
while left < right:
    ...

# Variable sliding window
left = 0
for right in range(len(values)):
    add(values[right])
    while window_is_invalid:
        remove(values[left])
        left += 1
    best = max(best, right - left + 1)

# Binary search over a closed interval
left, right = 0, len(values) - 1
while left <= right:
    mid = left + (right - left) // 2
    ...
```

### Complexity instincts

- A loop with average-O(1) set/dict operations is usually **O(n)** time.
- Sorting is **O(n log n)** and often enables a simpler two-pointer scan.
- Nested-looking work can still be **O(n)** if each pointer only moves one way.
- Python slicing creates a new object proportional to the slice length.
- Hash table guarantees are average case unless the interviewer says otherwise.

## Arrays & Hashing

### 1. Contains Duplicate — seen set

Invariant: `seen` contains exactly the values before the current index.

```python
def has_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

Time **O(n)** | Space **O(n)**  
Shortcut when only the result matters: `len(nums) != len(set(nums))`.

### 2. Valid Anagram — equal frequency maps

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}
    for a, b in zip(s, t):
        count_s[a] = count_s.get(a, 0) + 1
        count_t[b] = count_t.get(b, 0) + 1
    return count_s == count_t
```

Time **O(n)** | Space **O(k)** for `k` distinct characters.  
If input is guaranteed lowercase English letters, two arrays of length 26 also work.

### 3. Two Sum — complement map

Invariant: the map holds values from earlier indices, so one element is never reused.

```python
def two_sum(nums, target):
    index_by_value = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value:
            return [index_by_value[need], i]
        index_by_value[x] = i
```

Time **O(n)** | Space **O(n)**  
Check before inserting. This correctly handles cases such as `[3, 3]`, target `6`.

### 4. Group Anagrams — canonical signature

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord("a")] += 1
        groups[tuple(freq)].append(word)
    return list(groups.values())
```

Time **O(total characters)** | Space **O(total characters)**  
Alternative key: `"".join(sorted(word))`, costing **O(m log m)** per length-`m` word. Use the count key only when the alphabet is known.

### 5. Top K Frequent Elements — frequency buckets

Observation: a value can occur only `1..n` times, so frequency itself can be an array index.

```python
def top_k_frequent(nums, k):
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for x, frequency in count.items():
        buckets[frequency].append(x)

    answer = []
    for frequency in range(len(nums), 0, -1):
        for x in buckets[frequency]:
            answer.append(x)
            if len(answer) == k:
                return answer
```

Time **O(n)** | Space **O(n)**  
A size-`k` heap is useful when distinct values are numerous or data is streaming: **O(n log k)**.

### 6. Encode and Decode Strings — length prefix

A separator alone is ambiguous because it may appear inside a string. Store the payload length, then read exactly that many characters.

```python
def encode(words):
    return "".join(f"{len(word)}#{word}" for word in words)

def decode(message):
    result = []
    i = 0
    while i < len(message):
        j = i
        while message[j] != "#":
            j += 1
        length = int(message[i:j])
        start = j + 1
        result.append(message[start:start + length])
        i = start + length
    return result
```

Time **O(total characters)** | Space **O(total characters)** for output.  
Handles empty strings, digits, and `#` inside payloads.

### 7. Product of Array Except Self — prefix and suffix products

At index `i`: answer = product left of `i` × product right of `i`.

```python
def product_except_self(nums):
    answer = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

Time **O(n)** | Extra space **O(1)** excluding output.  
Initialize products to `1`, the multiplicative identity. This naturally handles zeroes and avoids division.

### 8. Longest Consecutive Sequence — expand from starts only

`x` begins a sequence exactly when `x - 1` is absent. Never expand from a middle value.

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0

    for x in values:
        if x - 1 not in values:
            length = 1
            while x + length in values:
                length += 1
            best = max(best, length)
    return best
```

Time **O(n)** average | Space **O(n)**  
Although there is a nested loop, each distinct value is expanded through once overall.

## Two Pointers

### When it works

Two pointers are useful when moving one boundary lets you safely discard candidates. Before coding, state why a pointer move cannot remove a better answer.

### 9. Valid Palindrome — inward pointers with filtering

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

Time **O(n)** | Extra space **O(1)**  
Keep `left < right` in the inner loops to avoid crossing boundaries.

### 10. 3Sum — sort, fix one, solve 2Sum II

```python
def three_sum(nums):
    nums.sort()
    result = []

    for i, x in enumerate(nums):
        if i > 0 and x == nums[i - 1]:
            continue
        if x > 0:                       # no later triplet can sum to zero
            break

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = x + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([x, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result
```

Time **O(n²)** | Extra space **O(1)** apart from output (ignoring sort internals).  
Duplicate control: skip repeated fixed values and repeated pointer values after a match. Sort mutates the input—copy first if mutation is forbidden.

### 11. Container With Most Water — move the shorter wall

Area = width × shorter height. Moving the taller wall only narrows the width while the shorter wall still caps the height, so it cannot improve the area.

```python
def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        width = right - left
        best = max(best, width * min(heights[left], heights[right]))

        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return best
```

Time **O(n)** | Extra space **O(1)**

## Sliding Window

### Window invariant

The active window is inclusive: `[left, right]`, with length `right - left + 1`.

1. Add the new right value.
2. Shrink from the left until the window is valid.
3. Update the answer at the correct moment.

Use `while`, not `if`, when multiple removals may be needed. Each pointer moves at most `n` times, so the scan is usually **O(n)**.

### 12. Best Time to Buy and Sell Stock — minimum so far

The sell day is the current day; `lowest` is the best earlier buy price.

```python
def max_profit(prices):
    lowest = prices[0]
    best = 0

    for price in prices[1:]:
        best = max(best, price - lowest)
        lowest = min(lowest, price)
    return best
```

Time **O(n)** | Extra space **O(1)**  
Update profit before/alongside the minimum; buying and selling on the same day only produces zero.

### 13. Longest Substring Without Repeating Characters — unique window

Invariant: every character in the window appears once.

```python
def length_of_longest_substring(s):
    window = set()
    left = 0
    best = 0

    for right, ch in enumerate(s):
        while ch in window:
            window.remove(s[left])
            left += 1
        window.add(ch)
        best = max(best, right - left + 1)
    return best
```

Time **O(n)** average | Space **O(k)** for the character set.  
Important: shrink until the repeated character is gone, not just once.

### 14. Longest Repeating Character Replacement — replacement budget

A window is valid when:

```text
window length - count of its most frequent character <= k
```

Keep the majority character and replace everything else.

```python
def character_replacement(s, k):
    count = {}
    left = 0
    max_frequency = 0
    best = 0

    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_frequency = max(max_frequency, count[ch])

        while (right - left + 1) - max_frequency > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)
    return best
```

Time **O(n)** | Space **O(k)** for the character set.  
`max_frequency` need not decrease while shrinking: a stale maximum may delay shrinking, but it cannot create a new, overly large answer.

## Stack

### 15. Valid Parentheses — latest opener must match

```python
def is_valid_parentheses(s):
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch not in matching_open:
            stack.append(ch)
        elif not stack or stack.pop() != matching_open[ch]:
            return False

    return not stack
```

Time **O(n)** | Space **O(n)**  
Two failure modes: a closer has no opener, or unmatched openers remain at the end.

## Binary Search

### Binary-search contract

For a closed interval `[left, right]`:

- Continue while `left <= right`.
- Discard `mid` with `left = mid + 1` or `right = mid - 1`.
- Every branch must strictly shrink the interval.

Rotated sorted-array problems here assume **distinct values**. With duplicates, identifying the sorted half may require extra handling.

### 16. Find Minimum in Rotated Sorted Array — compare with right edge

Invariant: the minimum remains inside `[left, right]`.

```python
def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1       # minimum is strictly right of mid
        else:
            right = mid          # mid might be the minimum

    return nums[left]
```

Time **O(log n)** | Extra space **O(1)**  
Notice `right = mid`, not `mid - 1`, because `mid` is still a candidate.

### 17. Search in Rotated Sorted Array — identify the sorted half

At least one half is normally sorted. Check whether the target lies inside that half; otherwise discard it.

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:             # left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                                   # right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

Time **O(log n)** | Extra space **O(1)**  
The boundary inequalities matter: left range is `[left, mid)`, right range is `(mid, right]`.

## Linked List

### Pointer rules

- Save `curr.next` **before** overwriting it.
- Compare nodes by identity, not by value, for cycle logic.
- A dummy node removes special handling when the head may change.
- Drawing three nodes and arrows is often faster than debugging pointer order.

Assume the platform provides `ListNode`.

### 18. Reverse Linked List — redirect one edge at a time

Invariant: `prev` is the reversed processed prefix; `curr` starts the untouched suffix.

```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

Time **O(n)** | Extra space **O(1)**

### 19. Merge Two Sorted Lists — dummy head

```python
def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next
```

Time **O(n + m)** | Extra space **O(1)**  
Attach the remaining suffix directly; it is already sorted.

### 20. Linked List Cycle — Floyd's tortoise and hare

If a cycle exists, the faster pointer eventually laps the slower pointer.

```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False
```

Time **O(n)** | Extra space **O(1)**  
Guard both `fast` and `fast.next` before taking two steps.

### 21. Reorder List — middle, reverse, weave

Transform `L0 → L1 → ... → Ln` into `L0 → Ln → L1 → Ln-1 → ...`.

```python
def reorder_list(head):
    if not head or not head.next:
        return

    # 1. Find end of first half
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Split and reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node

    # 3. Alternate nodes from both halves
    first, second = head, prev
    while second:
        next_first, next_second = first.next, second.next
        first.next = second
        second.next = next_first
        first, second = next_first, next_second
```

Time **O(n)** | Extra space **O(1)**  
Critical step: cut the first half with `slow.next = None` before merging.

### 22. Remove Nth Node From End — fixed pointer gap

Start `left` at a dummy. Move `right` `n` nodes ahead, then move both until `right` is `None`; `left` is immediately before the deletion.

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    left, right = dummy, head

    for _ in range(n):
        right = right.next

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
```

Time **O(n)** | Extra space **O(1)**  
The dummy makes removing the original head identical to every other deletion.

## Assessment checklist

Before coding:

1. Restate input, output, and whether indices or values are required.
2. Ask about empty input, duplicates, character set, integer range, and input mutation.
3. Give the brute-force approach, then identify the repeated work to remove.
4. State the invariant or why each pointer move is safe.

Before submitting:

- Test empty/minimum input and all-identical values.
- Test duplicates at the answer boundary (`[3, 3]`, repeated 3Sum values).
- Check `<` versus `<=`, pointer crossing, and off-by-one slice endpoints.
- Confirm dictionary keys are hashable (`tuple`, not `list`).
- For windows, confirm whether to update the answer before or after shrinking.
- For linked lists, save the next node before rewiring and check the new head.
- Verify the claimed time and space complexity.
- Confirm all paths return the required type.

## One-line recall

- **Contains Duplicate:** seen before?
- **Valid Anagram:** same counts?
- **Two Sum:** have I seen the complement?
- **Group Anagrams:** same immutable frequency signature?
- **Top K Frequent:** values grouped by bounded frequency?
- **Encode/Decode:** length tells where payload ends.
- **Product Except Self:** left product × right product.
- **Longest Consecutive:** expand only from the first number.
- **Valid Palindrome:** skip noise, compare ends.
- **3Sum:** sort, fix, squeeze, deduplicate.
- **Max Water:** compute area, move the shorter wall.
- **Stock:** cheapest earlier buy; best profit so far.
- **Longest Unique Substring:** shrink until the duplicate leaves.
- **Character Replacement:** window length − majority count ≤ `k`.
- **Valid Parentheses:** every closer matches the stack top.
- **Find Rotated Minimum:** compare middle with right.
- **Search Rotated Array:** find the sorted half, then range-check.
- **Reverse List:** save next, reverse edge, advance.
- **Merge Sorted Lists:** dummy + tail; attach the remainder.
- **Linked List Cycle:** slow one step, fast two.
- **Reorder List:** find middle, reverse second half, weave.
- **Remove Nth From End:** dummy + `n`-node gap.
