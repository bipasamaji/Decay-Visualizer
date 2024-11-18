<<<<<<< HEAD
#

import math
import pygame
import random
pygame.init()
atom_size = (50, 50)
beta_size = (10, 10)
c14 = pygame.image.load(&#39;assets\c14.png&#39;)
carbon14 = pygame.transform.scale(c14, atom_size)
n14 = pygame.image.load(r&#39;assets\n14.png&#39;)
nitrogen14 = pygame.transform.scale(n14, atom_size)
e0 = pygame.image.load(r&#39;assets\e0.png&#39;)
beta_particle = pygame.transform.scale(e0, beta_size)
class Carbon:
    def __init__(self, pos) -&gt; None:
        self.img = carbon14
        self.x_pos , self.y_pos = pos
        self.vel_mag = 0.3
        self.status = &quot;undecayed&quot;
        self.half_life = 1000
        self.decay_constant = math.log(2)/self.half_life
    def draw(self, surface):
        self.surface = surface
        self.possible_vel = [1, -1]
        self.x_vel = random.choice(self.possible_vel)  
        self.y_vel = random.choice(self.possible_vel)
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.status == &quot;undecayed&quot;:
            self.decay_lottery()
        if self.status == &quot;decayed&quot;:
            self.decay()
            self.status = &quot;decayed_and_stable&quot;
        self.check_bounds()
        self.surface.blit(self.img, (self.x_pos, self.y_pos))
        if self.status == &quot;decayed_and_stable&quot;:
            self.beta.draw(self.surface)

    def check_bounds(self):

        if self.x_pos &gt; self.surface.get_size()[0] - 25:
            self.x_pos = self.surface.get_size()[0] - 25
   
        if self.y_pos &gt; self.surface.get_size()[1] - 25:
            self.y_pos = self.surface.get_size()[1]- 25
        if self.x_pos &lt; 0:
            self.x_pos = 0
        if self.y_pos &lt; 0:
            self.y_pos = 0
    def decay(self):
        self.img = nitrogen14
        self.beta = betaParticle((self.x_pos, self.y_pos))
    def decay_lottery(self):
        chance = random.random()
        if chance &lt; self.decay_constant:
            self.status = &quot;decayed&quot;
   
class betaParticle:
    def __init__(self, pos) -&gt; None:
        self.img = beta_particle
        self.x_pos, self.y_pos = pos
        self.vel_mag = 3
        self.x_vel = self.vel_mag*random.choice((-1, 1))
        self.y_vel = self.vel_mag*random.choice((-1, 1))
    def draw(self, surface):
        self.surface = surface
        if self.on_screen():
            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
            self.surface.blit(self.img, (self.x_pos, self.y_pos))
    def on_screen(self):
        if self.x_pos &gt; 0 and self.x_pos &lt; self.surface.get_size()[0]:
            if self.y_pos &gt; 0 and self.y_pos &lt; self.surface.get_size()[1]:
=======
#

import math
import pygame
import random
pygame.init()
atom_size = (50, 50)
beta_size = (10, 10)
c14 = pygame.image.load(&#39;assets\c14.png&#39;)
carbon14 = pygame.transform.scale(c14, atom_size)
n14 = pygame.image.load(r&#39;assets\n14.png&#39;)
nitrogen14 = pygame.transform.scale(n14, atom_size)
e0 = pygame.image.load(r&#39;assets\e0.png&#39;)
beta_particle = pygame.transform.scale(e0, beta_size)
class Carbon:
    def __init__(self, pos) -&gt; None:
        self.img = carbon14
        self.x_pos , self.y_pos = pos
        self.vel_mag = 0.3
        self.status = &quot;undecayed&quot;
        self.half_life = 1000
        self.decay_constant = math.log(2)/self.half_life
    def draw(self, surface):
        self.surface = surface
        self.possible_vel = [1, -1]
        self.x_vel = random.choice(self.possible_vel)  
        self.y_vel = random.choice(self.possible_vel)
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.status == &quot;undecayed&quot;:
            self.decay_lottery()
        if self.status == &quot;decayed&quot;:
            self.decay()
            self.status = &quot;decayed_and_stable&quot;
        self.check_bounds()
        self.surface.blit(self.img, (self.x_pos, self.y_pos))
        if self.status == &quot;decayed_and_stable&quot;:
            self.beta.draw(self.surface)

    def check_bounds(self):

        if self.x_pos &gt; self.surface.get_size()[0] - 25:
            self.x_pos = self.surface.get_size()[0] - 25
   
        if self.y_pos &gt; self.surface.get_size()[1] - 25:
            self.y_pos = self.surface.get_size()[1]- 25
        if self.x_pos &lt; 0:
            self.x_pos = 0
        if self.y_pos &lt; 0:
            self.y_pos = 0
    def decay(self):
        self.img = nitrogen14
        self.beta = betaParticle((self.x_pos, self.y_pos))
    def decay_lottery(self):
        chance = random.random()
        if chance &lt; self.decay_constant:
            self.status = &quot;decayed&quot;
   
class betaParticle:
    def __init__(self, pos) -&gt; None:
        self.img = beta_particle
        self.x_pos, self.y_pos = pos
        self.vel_mag = 3
        self.x_vel = self.vel_mag*random.choice((-1, 1))
        self.y_vel = self.vel_mag*random.choice((-1, 1))
    def draw(self, surface):
        self.surface = surface
        if self.on_screen():
            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
            self.surface.blit(self.img, (self.x_pos, self.y_pos))
    def on_screen(self):
        if self.x_pos &gt; 0 and self.x_pos &lt; self.surface.get_size()[0]:
            if self.y_pos &gt; 0 and self.y_pos &lt; self.surface.get_size()[1]:
>>>>>>> 52cefcea66ee8dc18dc418f029917ea80aa9b813
                return True