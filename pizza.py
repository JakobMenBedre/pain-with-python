def vanlig_pizza():
    vann = 100
    mel = 0.5
    gjær = 0.3
    salt = 2
    skinke = 0.3
    tomat=0.2
    ost=0.5
    deig = vann+mel+gjær+salt
    return deig

def oven():
    temp = 200
    tid = 20
    brett = vanlig_pizza()
    grandiosa = temp+tid+brett
    return grandiosa

middag=oven()
print(middag)


