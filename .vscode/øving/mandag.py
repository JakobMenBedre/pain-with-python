''''
Oppgave 1



Opprett en klasse 'bil' med følgende egenskaper:

1.- motor  ##
2.- antall_seter
3.- farge
4.- speed
5.- max_speed
6.- dimensjon_dekk (størrelse)
7.- drivstoff
8.- dimensjon_bil
9.- konsum
10.- distance_vision

i tillegg må du implementere følgende metoder:
## lag egne variabler som påvirker egenskaper 

weather_condition()
## været påvirker mange egenskaper f.eks: konsum, max_speed, distance_vision
## lag egne variabler som påvirker egenskaper 

daylight()
## megden av lys påvirker max_speed og andre egenskaper

Hurry_up()
## Speed påvirker distnace_vision, konsum osv.


'''
weather_condition = 0
rain = 1
snow = 2
sun = 0
blizzard = 4
fog = 3

hvit = 1
blå = 1
rød = 1

motor = 4
antall_seter = 5
farge = blå
speed = 60
max_speed = 120
dimensjon_dekk = 15
drivstoff = 30
dimensjon_bil = 70
konsum = 13
distance_vision = 1

if weather_condition == rain:
    motor = 3
    antall_seter = 3
    farge = rød
    speed = 50
    max_speed= 100
    dimensjon_dekk = 30
    drivstoff = 30
    dimensjon_bil = 100
    konsum = 14
    distance_vision = 0.8
elif weather_condition == snow:
    motor = 3
    antall_seter = 3
    farge = hvit
    speed = 50
    max_speed= 100
    dimensjon_dekk = 30
    drivstoff = 30
    dimensjon_bil = 100
    konsum = 14
    distance_vision = 0.8
elif weather_condition == fog:
    motor = 3
    antall_seter = 3
    farge = rød
    speed = 50
    max_speed= 100
    dimensjon_dekk = 30
    drivstoff = 30
    dimensjon_bil = 60
    konsum = 12
    distance_vision = 0.4
elif weather_condition == blizzard:
    motor = 0
    antall_seter = 0
    farge = rød
    speed = 0
    max_speed= 0
    dimensjon_dekk = 0
    drivstoff = 0
    dimensjon_bil = 0
    konsum = 0
    distance_vision = 0




'''
Oppgave 2

opprett en klasse motorsykkel som har følgende egenskaper:
1.- speed
2.- max_speed
3.- motorstørrelse
4.- konsum



i tillegg må du implementere følgende metoder:

asfalt_in_badConditions()
#veitilstand vil påvirke speed, max_speed og andre egenskaper.
## lag egne variabler som påvirker egenskaper 

dancing_in_the_rain()
været påvirker mange egenskaper.
## lag egne variabler som påvirker egenskaper 

like_A_ferrari()
max_speed vil påvirker konsum, men også sikkerhet i trafikken.
## lag egne variabler som påvirker egenskaper 


'''