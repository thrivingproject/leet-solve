class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        columns = len(image[0])
        always_r = columns - 1
        updated_image = []
        for row in image:
            updated_row = [0] * columns
            l = 0
            r = always_r
            while l <= r:
                updated_row[l] = int(not row[r])
                updated_row[r] = int(not row[l])
                l += 1
                r -= 1
            updated_image.append(updated_row)
        return updated_image
