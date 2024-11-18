<<<<<<< HEAD
import pygame
from atoms import Carbon
import random
from matplotlib import pyplot as plt
initial_conc = int(input(&quot;Enter initial number of atoms: &quot;))
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(&quot;Radioactivity&quot;)
clock = pygame.time.Clock()
carbons = []
nitros = []
concentration = []
TIME = []
for i in range(initial_conc):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    carbons.append(Carbon((x, y)))
def plot(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel(&#39;Time&#39;)
    plt.ylabel(&#39;Concentration&#39;)
    plt.title(&#39;Concentration Vs Time&#39;)
    plt.show()

time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for carbon in carbons:
        if carbon.status == &quot;decayed_and_stable&quot;:
            nitros.append(carbon)
            carbons.remove(carbon)
   
    screen.fill([0, 0, 0])
    for carbon in carbons:
        carbon.draw(screen)
    for nitro in nitros:
        nitro.draw(screen)
   
    pygame.display.flip()
    num_c = len(carbons)
    concentration.append(num_c)
    TIME.append(time)
    time += 1
    clock.tick(60)
=======
import pygame
from atoms import Carbon
import random
from matplotlib import pyplot as plt
initial_conc = int(input(&quot;Enter initial number of atoms: &quot;))
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(&quot;Radioactivity&quot;)
clock = pygame.time.Clock()
carbons = []
nitros = []
concentration = []
TIME = []
for i in range(initial_conc):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    carbons.append(Carbon((x, y)))
def plot(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel(&#39;Time&#39;)
    plt.ylabel(&#39;Concentration&#39;)
    plt.title(&#39;Concentration Vs Time&#39;)
    plt.show()

time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for carbon in carbons:
        if carbon.status == &quot;decayed_and_stable&quot;:
            nitros.append(carbon)
            carbons.remove(carbon)
   
    screen.fill([0, 0, 0])
    for carbon in carbons:
        carbon.draw(screen)
    for nitro in nitros:
        nitro.draw(screen)
   
    pygame.display.flip()
    num_c = len(carbons)
    concentration.append(num_c)
    TIME.append(time)
    time += 1
    clock.tick(60)
>>>>>>> 52cefcea66ee8dc18dc418f029917ea80aa9b813
plot(TIME, concentration)