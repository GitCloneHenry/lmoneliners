from sys import stdin
from decimal import Decimal as dec, getcontext, ROUND_HALF_UP
getcontext().rounding = ROUND_HALF_UP

with open("twinkle-twinkle-samples\\1.in", "r") as source:

    def read_source() -> str:
        return source.readline().rstrip()
    
    cases: int = int(read_source())
    for casenum in range(cases):
        pass