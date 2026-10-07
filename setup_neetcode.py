from pathlib import Path

topics = {
    "01-arrays-and-hashing": [
        "contains-duplicate",
        "valid-anagram",
        "two-sum",
        "group-anagrams",
        "top-k-frequent-elements",
        "encode-and-decode-strings",
        "product-of-array-except-self",
        "valid-sudoku",
        "longest-consecutive-sequence",
    ],

    "02-two-pointers": [
        "valid-palindrome",
        "two-sum-ii-input-array-is-sorted",
        "3sum",
        "container-with-most-water",
        "trapping-rain-water",
    ],

    "03-sliding-window": [
        "best-time-to-buy-and-sell-stock",
        "longest-substring-without-repeating-characters",
        "longest-repeating-character-replacement",
        "permutation-in-string",
        "minimum-window-substring",
        "sliding-window-maximum",
    ],

    "04-stack": [
        "valid-parentheses",
        "min-stack",
        "evaluate-reverse-polish-notation",
        "generate-parentheses",
        "daily-temperatures",
        "car-fleet",
        "largest-rectangle-in-histogram",
    ],

    "05-binary-search": [
        "binary-search",
        "search-a-2d-matrix",
        "koko-eating-bananas",
        "find-minimum-in-rotated-sorted-array",
        "search-in-rotated-sorted-array",
        "time-based-key-value-store",
        "median-of-two-sorted-arrays",
    ],

    "06-linked-list": [
        "reverse-linked-list",
        "merge-two-sorted-lists",
        "reorder-list",
        "remove-nth-node-from-end-of-list",
        "copy-list-with-random-pointer",
        "add-two-numbers",
        "linked-list-cycle",
        "find-the-duplicate-number",
        "lru-cache",
        "merge-k-sorted-lists",
        "reverse-nodes-in-k-group",
    ],

    "07-trees": [
        "invert-binary-tree",
        "maximum-depth-of-binary-tree",
        "diameter-of-binary-tree",
        "balanced-binary-tree",
        "same-tree",
        "subtree-of-another-tree",
        "lowest-common-ancestor-of-a-binary-search-tree",
        "binary-tree-level-order-traversal",
        "binary-tree-right-side-view",
        "count-good-nodes-in-binary-tree",
        "validate-binary-search-tree",
        "kth-smallest-element-in-a-bst",
        "construct-binary-tree-from-preorder-and-inorder-traversal",
        "binary-tree-maximum-path-sum",
        "serialize-and-deserialize-binary-tree",
    ],

    "08-tries": [
        "implement-trie-prefix-tree",
        "design-add-and-search-words-data-structure",
        "word-search-ii",
    ],

    "09-heap-priority-queue": [
        "kth-largest-element-in-a-stream",
        "last-stone-weight",
        "k-closest-points-to-origin",
        "kth-largest-element-in-an-array",
        "task-scheduler",
        "design-twitter",
        "find-median-from-data-stream",
    ],

    "10-backtracking": [
        "subsets",
        "combination-sum",
        "permutations",
        "subsets-ii",
        "combination-sum-ii",
        "word-search",
        "palindrome-partitioning",
        "letter-combinations-of-a-phone-number",
        "n-queens",
    ],

    "11-graphs": [
        "number-of-islands",
        "clone-graph",
        "max-area-of-island",
        "pacific-atlantic-water-flow",
        "surrounded-regions",
        "rotting-oranges",
        "walls-and-gates",
        "course-schedule",
        "course-schedule-ii",
        "redundant-connection",
        "number-of-connected-components-in-an-undirected-graph",
        "graph-valid-tree",
        "word-ladder",
    ],

    "12-advanced-graphs": [
        "reconstruct-itinerary",
        "min-cost-to-connect-all-points",
        "network-delay-time",
        "swim-in-rising-water",
        "alien-dictionary",
        "cheapest-flights-within-k-stops",
    ],

    "13-1d-dynamic-programming": [
        "climbing-stairs",
        "min-cost-climbing-stairs",
        "house-robber",
        "house-robber-ii",
        "longest-palindromic-substring",
        "palindromic-substrings",
        "decode-ways",
        "coin-change",
        "maximum-product-subarray",
        "word-break",
        "longest-increasing-subsequence",
        "partition-equal-subset-sum",
    ],

    "14-2d-dynamic-programming": [
        "unique-paths",
        "longest-common-subsequence",
        "best-time-to-buy-and-sell-stock-with-cooldown",
        "coin-change-ii",
        "target-sum",
        "interleaving-string",
        "longest-increasing-path-in-a-matrix",
        "distinct-subsequences",
        "edit-distance",
        "burst-balloons",
        "regular-expression-matching",
    ],

    "15-greedy": [
        "maximum-subarray",
        "jump-game",
        "jump-game-ii",
        "gas-station",
        "hand-of-straights",
        "merge-triplets-to-form-target-triplet",
        "partition-labels",
        "valid-parenthesis-string",
    ],

    "16-intervals": [
        "insert-interval",
        "merge-intervals",
        "non-overlapping-intervals",
        "meeting-rooms",
        "meeting-rooms-ii",
        "minimum-interval-to-include-each-query",
    ],

    "17-math-and-geometry": [
        "rotate-image",
        "spiral-matrix",
        "set-matrix-zeroes",
        "happy-number",
        "plus-one",
        "pow-x-n",
        "multiply-strings",
        "detect-squares",
    ],

    "18-bit-manipulation": [
        "single-number",
        "number-of-1-bits",
        "counting-bits",
        "reverse-bits",
        "missing-number",
        "sum-of-two-integers",
        "reverse-integer",
    ],
}


notes_template = """# Problem

## Problem Summary

Write the problem in your own words.

---

## My Initial Approach

Explain what you first thought.

---

## Optimal Approach

Explain the best approach simply.

---

## Pattern

-

---

## Complexity

**Time:** O()

**Space:** O()

---

## What I Learned

-

---

## Mistakes

-

---

## Pattern Recognition

Think about this approach when:

-
"""


total = 0

for topic, problems in topics.items():
    topic_path = Path(topic)
    topic_path.mkdir(exist_ok=True)

    for index, problem in enumerate(problems, start=1):
        folder = topic_path / f"{index:02d}-{problem}"
        folder.mkdir(exist_ok=True)

        solution_file = folder / "solution.py"
        notes_file = folder / "notes.md"

        if not solution_file.exists():
            solution_file.write_text("")

        if not notes_file.exists():
            notes_file.write_text(notes_template)

        total += 1

print(f"Created structure for {total} NeetCode problems.")