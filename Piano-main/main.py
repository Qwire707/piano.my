import play
import pygame
pygame.init()
pygame.mixer.init()
#створення текстових спрайтів
play.set_backdrop((100, 0, 50))

text1 = play.new_text(words = "Це - піаніно", x = 0, y = 230)
text2 = play.new_text(words = "Твори музику натискаючи на клафіша", x = 0, y = 180)

piano_on = play.new_circle(color =(150, 16, 20), x = -180, y = -100, radius= 10, border_color= "black", border_width=3)
piano_txt = play.new_text(words="piano" , x = -142, y = -100, font_size=25)

flute_on = play.new_circle(color = (150, 16, 20), x = -100, y = -100, radius= 10, border_color= "black", border_width=3)
flute_txt = play.new_text(words= "flute", x = -65, y = -100, font_size=25)

gitar_on = play.new_circle(color = (150, 16, 20), x = -20, y = -100, radius= 10, border_color= "black", border_width=3)
gitar_txt = play.new_text(words= "gitar", x = 17, y = -100, font_size=25)

violin_on = play.new_circle(color = (150, 16, 20), x = 60, y = -100, radius= 10, border_color= "black", border_width=3)
violin_txt = play.new_text(words= "violin", x = 100, y = -100, font_size=25)


#списки для клавіш та звуків
keys = []
sounds = []
for s in range(4):
    sounds.append([])
#формуємо списки з клавішами та звуками
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color="white", width = 40, height = 120, x = key_x, y = 0, border_width = 5, border_color = "black")
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + ".ogg")
    sounds[0].append(sound)
    sound = pygame.mixer.Sound("f" + str(i + 1) + ".ogg")
    sounds[1].append(sound)
    sound = pygame.mixer.Sound("g" + str(i + 1) + ".ogg")
    sounds[2].append(sound)
    sound = pygame.mixer.Sound("v" + str(i + 1) + ".ogg")
    sounds[3].append(sound)


get_instrument = 0


@play.when_program_starts#функція для початку програми
def start():
    pass
@piano_on.when_clicked
def get_piano_on():
    global get_instrument
    get_instrument = 0
    piano_on.color = (150, 16, 20)
    flute_on.color = "white"
    gitar_on.color = "white"
    violin_on.color = "white"
@flute_on.when_clicked
def get_flute_on():
    global get_instrument 
    get_instrument = 1
    piano_on.color = "white"
    flute_on.color = (150, 16, 20)
    gitar_on.color = "white"
    violin_on.color = "white"
@gitar_on.when_clicked
def get_gitar_on():
    global get_instrument 
    get_instrument = 2
    piano_on.color = "white"
    flute_on.color = "white"
    gitar_on.color = (150, 16, 20)
    violin_on.color = "white"
@violin_on.when_clicked
def get_violin_on():
    global get_instrument 
    get_instrument = 3
    piano_on.color = "white"
    flute_on.color = "white"
    gitar_on.color = "white"
    violin_on.color = (150, 16, 20)


@play.repeat_forever#ігровий цикл
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = (55, 144, 29)
            await play.timer(0.3)
            keys[j].color = ("white")
play.start_program()