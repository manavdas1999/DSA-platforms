
# Very Pythonic code, can be done in a more elaborative way suitable for other languages
# Time: O(n2) maybe


def minLength(self, s: str) -> int:
    while ("AB" in s) or ("CD" in s):
       s = s.replace("AB", "")
       s = s.replace("CD", "")
    return len(s)
