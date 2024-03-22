"""
W tym miejscu wyzanczamy NIFS3y
"""

def h_list(xs):
    n = len(xs)
    h = [0]*n
    for i in range(1, n):
        h[i] = xs[i] - xs[i-1]
    return h

def l_list(xs):
    h_ls = h_list(xs)
    n = len(h_ls)
    l = [0]*n
    for i in range(n-1):
        l[i] = (h_ls[i] / (h_ls[i] + h_ls[i+1]))
    return l

def d_quotient(xs, ys):
    if len(xs) == 1:
        return ys[0]
    return (d_quotient(xs[1:], ys[1:]) - d_quotient(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

def d_calc(k, xs, ys):
    if k == 0:
        return 0
    return 6 * d_quotient(xs[(k - 1):(k + 2)], ys[(k - 1):(k + 2)])

def m_list(xs, ys):
    n = len(xs)

    p = [0]*n
    q = [0]*n                          
    u = [0]*n
    l = l_list(xs)
    d = [d_calc(k, xs, ys) for k in range(n)]

    for i in range(1, n-1):
        p[i] = l[i] * q[i - 1] + 2
        q[i] = (l[i] - 1) / p[i]
        u[i] = (d[i] - l[i] * u[i - 1]) / p[i]

    m = [0]*(n+1)
    m[n - 1] = u[n - 1]

    for i in range(n - 2, 0, -1):
        m[i] = u[i] + q[i] * m[i + 1]

    return m

def spine(xs, ys, m_ls, hk, k):
    return lambda x: (
        (m_ls[k - 1] * (xs[k] - x) ** 3) / 6 + 
        (m_ls[k] * (x - xs[k - 1]) ** 3) / 6 + 
        (ys[k - 1] - (m_ls[k - 1] * hk ** 2) / 6) * (xs[k] - x) + 
        (ys[k] - (m_ls[k] * hk ** 2) / 6) * (x - xs[k - 1])
    ) / hk

def get_s(xs, ys):
    h_ls = h_list(xs)
    m_ls = m_list(xs, ys)
    return lambda x: next(
        (
            spine(xs, ys, m_ls, h_ls[i], i)(x)
            for i in range(1, len(xs))
            if xs[i - 1] <= x <= xs[i]
        ),
        None
    )