from matplotlib import pyplot # Install matplotlib før du begynner med oppgavene 

'''
oppgave 1

    Anne har laget et program som skal regne ut hvor mye mel ho trenger til å lage a antall liter vaffelrøre.


'''
a = 2
b = a * 4.5
print("Du trenger", b, " dl mel. ")

'''
Anne prøver å taste inn 4.5 liter vaffelrøre, men programmet skriver ut en feilmelding til skjermen.
Hjelp Anne med koden slik at den vil fungere også med desimaltall.
'''
#####################################################################################################################
'''
Oppgave 2

Kari har gjort en undersøkelse i klassen sin og spurt klassekameratene hvilke type kjæledyr de har hjemme.
Svarene ble:
Katt: 7
Hund: 5
Fugl: 3
Andre dyr: 4
Ingen:6

Kari ønsker å lage et Python- program der ho kan taste inn frekvensene til de ulike observasjonene og
hun vil at programmet skal skrive ut et stolpediagram til skjermen.
'''
'''
x = ["katt", "hund","fugl","andre_dyr","ingen_dyr"] #lager en liste x med 5 elementer 


y = [0, 1,2,3,4]
y[0]= input("hvor mange katter?")
y[1]= input("hvor mange hunder")
y[2]= input("hvor mange fugler")
y[3]= input("hvor mange med andre dyr")
y[4]= input("hvor mange uten dyr")
pyplot.bar(x,y) # lager stolpediagram  med elementene fra x og y
pyplot.show() # skriver diagrammet til skjermen
'''

#############################################################################################################################
'''
oppgave 3

Kjør programmet og forklar hva det gjør.  #programmet printer ut alle de hele tallene mellom 4 og 19
Prøv å skriv ut heltall fra og med 7 til og med 32
Prøv å skriv ut heltall fra og med -10 til og med 10

'''
for tall in range (-10,10):
    print(tall)

###############################################################################################################################

'''
oppgave 4

Kjør programmet og forklar hva det gjør.   # programmet tall fra 0 til m og ganger alle tallene med 3
Endre 3 tallet til andre tall og se hva som skjer.
'''
for m in range (10):
    print(m, 1*m)

################################################################################################################################

'''
Oppgave 5

Kari har laget et program der bruker kan taste inn alder å få skrevet ut pris på kinobillett til skjermen.

Kjør programmet og forklar hvordan det fungerer. # du skriver inn en alder, også gir den deg forskjellige svar etter pris. hvis alderen er under 6 er prisen 0. hvis den er 6-12 er prisen 80. hvis alderen er 13 - 17 er prisen 100, og hvis alderen er 18+ så er prisen 120.

Kinoen kommer med en tilbud til de mellom 18 og 25 år på 110 kroner per billett.
Gjør endringer på koden slik at det blir tilpasset tilbudet.
'''
b = 80  # pris for en billett barn(6-12 år)
u = 100 # pris for en billett ungdom(13-17)
v = 120 # pris for en billett voksen
g = 0   # under 6 år er gratis
uv = 110
alder = int(input("Tast inn alder: "))
if alder <= 5:
  pris = g
elif alder > 5 and alder < 13: 
  pris = b
elif alder > 12 and alder < 18:
  pris = u
elif alder > 17 and alder < 26:
    pris = uv
else:
  pris = v
print("Prisen blir", pris, "kroner. ")

########################################################################################################################################

'''
Oppgave 6
En dag i Moss var det følgende temperaturer:
Klokkeslett - grader
kl 06.00 - 12
kl 12.00 - 14
kl 18.00 - 20
kl 22.00 - 21
Lag et linjediagram over temperaturutviklingen.
Tips: Bruk det du har lært i koden over i tillegg til det under.
'''
x = ["kl 06:00", "kl 12:00", "kl 18:00", "kl 22:00"]  # lag en liste for klokkeslett
y = [12, 14, 20, 21]  # lag en liste for temperaturen
pyplot.plot(x,y) # lager linjediagram med elementene fra x og y 
#pyplot.show()


#################################################################################################################################################
'''easy-medium'''

'''

Pygame må installeres før å begynne oppgavene!!!!!!!!!!!

Last ned Praktisk_arv_subklasse og kjør koden. Du skal se et sett objekter laget av subklasser definerte 
i fila subclass_practical_exercise.py. 

'''

import pygame
import random

################################# settings################################################
'''
her finner du vindustørrelse og elementer(figurer) som brukes i programmet
'''

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "img/sushiplate.jpg" ### figurer for å lage fylle objekter
MOUSE_FNAME = "img/fugu.png"     
BALL_FNAME = "img/ball.png"


################################## start #######################################
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img  = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()

### superklasse #### en superklasse er en form som brukes for å implementere subklasser
class MovingObject:
    def __init__(self):###### variabler som definerer egenskapene ####
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
        self.size = 30

    def move(self, time_passed):    ######## funksjon move skal bruke variablene ovenfor for å 
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

        if self.x > SCREEN_X - self.size:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y - self.size:
            self.speed[1] = -abs(self.speed[1])

    def draw(self): #### not in use####
        pass

################################################ SUBKLASSER #############################

### subklasse Ball ###################
class Ball(MovingObject):
    def __init__(self):
        MovingObject.__init__(self) #### en subklasse må deklarere superklasse
        self.img = ball_img
        self.size = self.img.get_height()

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


## subklasse Circle ########################

class Circle(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)
        self.col = (255, 255, 0)

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)),
                           round(self.size / 2))

############################ instance ########### 
'''
***
'''

ball1 = Ball()
objs = [
    Ball(),
    Ball(),
    Circle(),
    Circle(),
    Ball(),
]

######################### main loop ####################################
clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    time_passed = clock.tick(30) / 1000.0

    # t = pygame.mouse.get_pos()
    # x = t[0]
    # y = t[1]
    x, y = pygame.mouse.get_pos()

    mx = x - mouse_size_x / 2
    my = y - mouse_size_y / 2

    screen.blit(background, (0, 0))
    screen.blit(mouse_img, (mx, my))

    ball1.move(time_passed)
    ball1.draw()

    for obj in objs:
        obj.move(time_passed)

    for obj in objs:
        obj.draw()

    pygame.display.update()
'''
Oppgave 1 
script du ser i fila subclass_practical_exercise.py viser blant annet to subklasser som brukes for å lage objekter.

Du skal implementere 2 andre subklasser med MOvingObjekt class som superklasse. opprett en lista med 2 objekter for hver subklasse
Du MÅ kommentere koden din. forklar implementasjon av klassene. 
 
'''

###################################################################################################################################

'''
Oppgave 2 

forklar med egne ord hva betyr arv i objektorientert programmering i Python.


'''




#################################################################################################################################################
'''medium'''

'''
Pygame må installeres før å begynne oppgavene!!!!!!!!!!!

Last ned Praktisk_arv_subklasse og kjør koden. Du skal se et sett objekter laget av subklasser definerte 
i fila subclass_practical_exercise.py. 

'''
'''
Oppgave 1

Forklar med egne ord hva betyr begrepet "objekt" i objektorientert programmering.

'''
# ett objekt 
'''
Oppgave 2
implementer EGET program med 2 superklasser og 1 subklasse for hver superklasse.
opprett 2 objekter for hver subklasse. disse objektene skal bytte farge hvis de kolliderer med andre objekter 
'''
