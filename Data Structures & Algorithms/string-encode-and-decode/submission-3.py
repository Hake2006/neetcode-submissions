class Solution:

    def encode(self, strs: List[str]) -> str:
        # We don't need the empty check anymore; an empty list 
        # naturally loops zero times and returns just "#"
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz) + ','
        res += '#'
        for s in strs:
            res += s
        return res
    
    def decode(self, s: str) -> List[str]:
        sizes, res, i = [], [], 0
        
        # Read the sizes until we hit the marker
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1 # skip the comma
            
        i += 1 # skip the '#' marker
        
        # Slice out the strings using our saved sizes
        for sz in sizes:
            res.append(s[i : i + sz]) # Fixed the double-nested append!
            i += sz
            
        return res