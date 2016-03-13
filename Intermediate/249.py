from random import randint
from sys import argv
from functools import reduce
import random
import time

start_time = time.time()
"""
# Non-genetic, calculates only the hamming distance
# of a random string.
step = 0
def random_str(n):
    return ''.join(
        [chr(randint(ord('A'), ord('z'))) for i in range(n)])

def hamming_distance(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        diff += int(c1 != c2)
    return diff

def generate_strings(text):
    gen = random_str(len(text))
    distance = hamming_distance(text, gen)

    while distance > 0:
        gen = random_str(len(text))


gen = random_str(len(input_text))
print(gen)
print(hamming_distance(input_text, gen))
"""
def add(x,y): return x+y

# Genetic Algorithm
def individual(length, min, max):
    'Generate random letters of the string.'
    return ''.join(
        [chr(randint(ord(min), ord(max))) for i in range(length)])

def population (count, length, min, max):
    """
    Generates random groups of strings.

    count: number of strings per population
    length: number of values per string
    min: min value in the list of values
    max: max value in the list of values

    """
    return [ individual(length, min, max) for x in range(count)]

def fitness (individual, target):
    """
    Determine the fitness of an individual. Lower is better.

    individual: individual to evaluate
    target: the string we want to evolve to
    """

    diff = 0
    for individual, target in zip(individual, target):
        diff += int(individual != target)
    return diff

def list_match(individual, target):
    i = 0
    l = []
    for individual, target in zip(individual, target):
        if (individual != target):
            l.append(i)
        i += 1
    return l
    # return abs(int(individual) - int(target))

def grade(pop, target):
    'Finds average fitness for a population.'

    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed / (len(pop) * 1.0)

def randchar(a, b):
    return chr(random.randint(ord(a), ord(b)))

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.2):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    # randomly add other individuals to promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random.random():
            parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random.random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual.replace(individual[pos_to_mutate], randchar(
             min(individual), max(individual)))

    print (individual)

    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male)//2
            child = male[:half] + female[half:]
            children.append(child)

    parents.extend(children)
    return parents


target = argv[1]
p_count = 800000
i_length = len(target)
i_min = min(target)
i_max = max(target)
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]
i = 0
while(grade(p, target) != 0):
    print ("Gen: %d\t|  Fitness: %.2f  | " %(i, grade(p, target))),
    p = evolve(p, target)
    i += 1
    fitness_history.append(grade(p, target))

elapsed_time = time.time() - start_time
print("Elapsed time is %f seconds" %(elapsed_time))
# for datum in fitness_history:
#      print (datum)
