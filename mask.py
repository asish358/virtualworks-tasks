class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        row_masks = {}

        # Build bitmask for rows with reserved seats
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_masks[row] = row_masks.get(row, 0) | (1 << (col - 2))

        # Entirely empty rows contribute 2 groups each
        max_groups = (n - len(row_masks)) * 2

        # Masks representing seat checks:
        # Left: seats 2,3,4,5   -> 0b00001111 (15)
        # Middle: seats 4,5,6,7 -> 0b00111100 (60)
        # Right: seats 6,7,8,9  -> 0b11110000 (240)
        left_mask = 0b00001111
        middle_mask = 0b00111100
        right_mask = 0b11110000

        for mask in row_masks.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            middle_free = (mask & middle_mask) == 0

            if left_free and right_free:
                max_groups += 2
            elif left_free or right_free or middle_free:
                max_groups += 1

        return max_groups
