ptiny("cmmdc" cu euclid prin scaderi)
def cmmdc(n, m):
    if n! = m:
        if n > m:
            return(cmmdc(n - m, m))
        else:
            return(cmmdc(n, m-n))
        eslse
