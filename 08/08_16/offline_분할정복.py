def solve(start, end):
    m = (start+end) // 2
    w1 = solve(start, m)
    w2 - solve(m+1, end)