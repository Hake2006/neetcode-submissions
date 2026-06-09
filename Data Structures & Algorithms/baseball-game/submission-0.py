class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for op in operations:
            if op == "+":
                rec.append(rec[-1] + rec[-2])
            elif op == "C":
                rec.pop()
            elif op == "D":
                rec.append(rec[-1] * 2)
            else:
                rec.append(int(op))
        return sum(rec)