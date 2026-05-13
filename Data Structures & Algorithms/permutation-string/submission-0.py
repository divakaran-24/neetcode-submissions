class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1count = {}
        window = {}

        # build hashmap for s1
        for c in s1:
            s1count[c] = s1count.get(c, 0) + 1

        l = 0

        for r in range(len(s2)):

            # add right character
            window[s2[r]] = window.get(s2[r], 0) + 1

            # maintain fixed window size
            if r - l + 1 > len(s1):

                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            # compare hashmaps
            if window == s1count:
                return True

        return False