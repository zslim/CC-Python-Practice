

def draw_diamond (sorok):
    if sorok%2 == 0 or sorok<1:
        return None
    diamond = []
    kozepso_sor = sorok//2 +1
    for i in range(0, kozepso_sor):
        csillag_szam = sorok - (i*2)
        hossz = csillag_szam + 1
        sor = ("*"*csillag_szam).rjust(hossz)
        diamond.append(sor)
        if i > 0:
            diamond.insert(0, sor)
    return "\n".join(diamond) + "\n"


print(draw_diamond(15))
