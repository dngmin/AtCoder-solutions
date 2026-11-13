S = int(input())
if 1 <= S//100 <= 12: S1 = "MM"
else: S1 = "YY"
if 1 <= S%100 <= 12: S2 = "MM"
else: S2 = "YY"

if S1 != S2:
    if S1 == "MM": print("MMYY")
    else: print("YYMM")
if S1 == S2:
    if S1 == "MM": print("AMBIGUOUS")
    else: print("NA")