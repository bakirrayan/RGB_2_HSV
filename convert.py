

from pyrsistent import v


def convert(r, g, b):
    """
    Convert RGB to HSV
    """
    R, G, B = r/255, g/255, b/255

    Cmax = max(R, G, B)
    Cmin = min(R, G, B)

    delta = Cmax - Cmin

    if delta == 0:
        H = 0
    elif Cmax == R:
        H = 60 * (((G - B) / delta) % 6)
    elif Cmax == G:
        H = 60 * (((B - R) / delta) + 2)
    elif Cmax == B:
        H = 60 * (((R - G) / delta) + 4)
    
    if Cmax == 0:
        S = 0
    elif Cmax != 0:
        S = delta / Cmax
    
    V= Cmax
    
    return f"H= {H}°, S= {S*100:.3f}, V= {V*100:.3f}"


a,b,c = input("Enter the value R, G and B with coma between them: \n").split(",")
print("HSV == >", convert(int(a), int(b), int(c)))
