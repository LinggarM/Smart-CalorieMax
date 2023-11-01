import numpy as np
import random as rd
from random import randint

def cal_fitness(weight, value, population, threshold):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        S1 = np.sum(population[i] * value)
        S2 = np.sum(population[i] * weight)
        if S2 <= threshold:
            fitness[i] = S1
        else :
            fitness[i] = 0 
    return fitness.astype(int) 
	
def weighted_random_choice(choices):
    max = sum(choices)
    pick = rd.uniform(0, max)
    current = 0
    for i,value in enumerate(choices):
        current =current+value
        if current > pick:
            return i
			
def selection(fitness, num_parents, population):
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        index=weighted_random_choice(fitness)
        parents[i,:] = population[index, :]
    return parents
	
def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2)
    crossover_rate = 0.9
    i=0
    while (parents.shape[0] < num_offsprings):
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
        offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
        i=+1
    return offsprings 
	
def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.2
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i,:] = offsprings[i,:]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0,offsprings.shape[1]-1)    
        if mutants[i,int_random_value] == 0 :
            mutants[i,int_random_value] = 1
        else :
            mutants[i,int_random_value] = 0
    return mutants   
	
def elitism(mutants, population, fitness, weight, value, threshold):
    elitis = np.empty((mutants.shape))
    elitis = mutants
    parents_max_loc = np.where(fitness == np.max(fitness))[0]
    parents_max_loc_real = parents_max_loc[0]
    fitness_mutants = cal_fitness(weight, value, mutants, threshold)
    mutants_min_loc = np.where(fitness_mutants == np.min(fitness_mutants))
    mutants_min_loc_real = mutants_min_loc[0]
    elitis[mutants_min_loc_real] = population[parents_max_loc_real]
    return elitis
	
def optimize(weight, value, population, pop_size, num_generations, threshold):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0])
    num_offsprings = pop_size[0] 
    for i in range(num_generations-1):
        fitness = cal_fitness(weight, value, population, threshold)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population = elitism(mutants, population, fitness, weight, value, threshold)
        
    fitness_last_gen = cal_fitness(weight, value, population, threshold)      
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0],:])
    return parameters, fitness_history


def kalkulasi(nama_makanan, value_makanan, harga_makanan, uang) :
	numpy_nama_makanan = np.array([i for i in nama_makanan.split(',')])
	numpy_value_makanan = np.array([int(i) for i in value_makanan.split(',')])
	numpy_harga_makanan = np.array([int(i) for i in harga_makanan.split(',')])
	
	item_number = np.arange(1,11)
	weight = numpy_harga_makanan
	value = numpy_value_makanan
	knapsack_threshold = int(uang)

	solutions_per_pop = 10
	pop_size = (solutions_per_pop, item_number.shape[0])
	initial_population = np.random.randint(2, size = pop_size)
	initial_population = initial_population.astype(int)
	num_generations = 50
	
	parameters, fitness_history = optimize(weight, value, initial_population, pop_size, num_generations, knapsack_threshold)
	selected_items = item_number * parameters
	
	hasil_nama_makanan = []
	kalori = 0
	uang_yang_dibutuhkan = 0
	for i in selected_items[0] :
		if (i!=0) :
			hasil_nama_makanan.append(numpy_nama_makanan[int(i)-1])
			kalori = kalori + numpy_value_makanan[int(i)-1]
			uang_yang_dibutuhkan = uang_yang_dibutuhkan + numpy_harga_makanan[int(i)-1]
	
	hasil_string = ""
	for i in hasil_nama_makanan :
		hasil_string = hasil_string + i + ","
	total = []
	total.append(hasil_string)
	total.append(kalori)
	total.append(uang_yang_dibutuhkan)
	
	return total