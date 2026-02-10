# Bitmask Subset Enumeration

## The Pattern

```python
for i in range(2**n):
    for j in range(n):
        if (i >> j) & 1:
            # nums[j] is in the subset
```

## How It Works

Every integer from `0` to `2^n - 1` has a unique binary representation of `n` bits. Each bit position maps to an element in the array — if the bit is `1`, the element is included in the subset.

For `n = 3` (elements `[a, b, c]`):

| `i` | Binary | Subset      |
|-----|--------|-------------|
| 0   | `000`  | `[]`        |
| 1   | `001`  | `[a]`       |
| 2   | `010`  | `[b]`       |
| 3   | `011`  | `[a, b]`    |
| 4   | `100`  | `[c]`       |
| 5   | `101`  | `[a, c]`    |
| 6   | `110`  | `[b, c]`    |
| 7   | `111`  | `[a, b, c]` |

## Breaking Down `(i >> j) & 1`

This expression checks whether bit `j` is set in `i`.

1. **`i >> j`** — Right-shift `i` by `j` positions, moving bit `j` into the least-significant position.
2. **`& 1`** — Mask off everything except the least-significant bit, yielding `0` or `1`.

### Example: `i = 5`, `j = 2`

```
i = 5       →  1 0 1
i >> 2 = 1  →      1
& 1         →      1  ← bit 2 is set, so nums[2] is included
```

### Example: `i = 5`, `j = 1`

```
i = 5       →  1 0 1
i >> 1 = 2  →    1 0
& 1         →      0  ← bit 1 is not set, so nums[1] is excluded
```
