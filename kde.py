import settings as sett

def densityF(x, y, t, xi, yi, ti):
    u = (x-xi) / sett.p1 
    v = (y-yi) / sett.p1 
    w = (t-ti) / sett.p2 
    Ks = sett.ct1 * (1 - pow(u, 2) - pow(v, 2))
    Kt = 0.75 * (1 - pow(w, 2))
    spaceTimeKDE = sett.ct2 * Ks * Kt
    return spaceTimeKDE

