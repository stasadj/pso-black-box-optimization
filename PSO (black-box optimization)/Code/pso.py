import numpy as np
from operator import attrgetter
from particle import Particle

'''
******************* Projektni zadatak 12 *******************
Autori: Anastasija Đurić SW48-2018, Nenad Petković SW37-2018 
'''


def pso(options):
    iteration = 0
    result = {
        'global_best': np.zeros(60),
        'global_best_fitness': 100
    }

    swarm = create_swarm(options['num_of_particles'])
    update_global_best(swarm, result)
    print_initial_info(result)

    for i in range(options.get('num_of_iters')):
        for particle in swarm:
            particle.update_position(options, result['global_best'])

        iteration += 1
        update_parameters(options)
        update_global_best(swarm, result)
        print_iteration_info(iteration, result)

    return result['global_best'], result['global_best_fitness']


def update_parameters(options):
    num_of_iters = options['num_of_iters']
    options['w'] = options['w'] - 0.5 / (num_of_iters + 1)
    options['cp'] = options['cp'] - 2 / (num_of_iters + 1)
    options['cg'] = options['cg'] + 2 / (num_of_iters + 1)


def create_swarm(size):
    swarm = []

    for i in range(size):
        swarm.append(Particle())

    return swarm


def update_global_best(swarm, result):

    best_particle = min(swarm, key=attrgetter('fitness'))

    if best_particle.fitness < result.get('global_best_fitness'):
        result['global_best'] = best_particle.current_position.copy()
        result['global_best_fitness'] = best_particle.fitness


def print_initial_info(result):

    print('INITIAL SWARM')
    print('MEAN ABSOLUTE ERROR: ', result.get('global_best_fitness'))
    print('--------------------------------------------------------')


def print_iteration_info(iteration, result):

    print('ITERATION: ', iteration)
    print('MEAN ABSOLUTE ERROR: ', result.get('global_best_fitness'))
    print('--------------------------------------------------------')


def get_options():
    opts = {
        'num_of_particles': 30,
        'num_of_iters': 30,
        'w': 0.9,
        'cp': 2.5,
        'cg': 0.5
    }

    return opts

