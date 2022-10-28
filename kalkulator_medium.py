lån = int(input('Oppgi lån verdien'))
rente = float(input('oppgi rente i desimaltall'))
nedbetalingstid_mnd = int(input('oppgi nedbetalingstid'))
lån_oppdatert = lån
avdrag = lån/nedbetalingstid_mnd
år = 1
renter = lån_oppdatert*rente
terminbeløp = renter + avdrag

while lån_oppdatert != 0:
    renter = lån_oppdatert*rente
    print('år', år, lån_oppdatert, renter, avdrag, terminbeløp)
    lån_oppdatert = lån_oppdatert - avdrag
    renter = lån_oppdatert*rente
    terminbeløp = renter + avdrag
    år = år + 1




