class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        for s in strs:
            # 1. Join the sorted list into a string so it can be a dict key
            key = "".join(sorted(s))
            
            # 2. Initialize the key if it doesn't exist
            if key not in anagram_map:
                anagram_map[key] = []
                
            anagram_map[key].append(s)
            
        return list(anagram_map.values())