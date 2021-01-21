import numpy as np
import random as rand
from ann_criterion import optimality_criterion

'''
******************* Projektni zadatak 12 *******************
Autori: Anastasija Đurić SW48-2018, Nenad Petković SW37-2018 
'''


class Particle(object):

    def __init__(self):
        self.current_position = np.random.uniform(-5, 5, 60)
        self.velocity = np.random.uniform(-1, 1, 60)
        self.personal_best = self.current_position.copy()
        self.fitness = optimality_criterion(self.current_position)
        self.fitness_best = self.fitness

    def update_position(self, options, global_best):
        self.velocity = options['w'] * self.velocity + \
                        options['cp'] * rand.random() * (self.personal_best - self.current_position) + \
                        options['cg'] * rand.random() * (global_best - self.current_position)

        self.current_position = self.current_position + self.velocity
        self.current_position[self.current_position < -5] = -5
        self.current_position[self.current_position > 5] = 5

        self.fitness = optimality_criterion(self.current_position)

        if self.fitness < self.fitness_best:
            self.personal_best = self.current_position.copy()
            self.fitness_best = self.fitness

