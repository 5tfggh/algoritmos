import random

def fitness_function(solution):
    x, y, z = solution
    target_value = 8
    equation_result = x + 2*y - z
    return 1 / (1 + abs(target_value - equation_result))

def generate_individual():
    return [random.randint(0, 12) for _ in range(3)]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += random.randint(-1, 1)
    return individual

def genetic_algorithm(population_size, generations):
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness_function(x), reverse=True)

        new_population = []
        for _ in range(population_size // 2):
            parent1 = population[random.randint(0, population_size // 2 - 1)]
            parent2 = population[random.randint(0, population_size // 2 - 1)]
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = population[:population_size // 2] + new_population

        best_solution = population[0]
        best_fitness = fitness_function(best_solution)

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Solution = {best_solution}")

    return population[0]

if __name__ == "__main__":
    population_size = 12
    generations = 10

    best_solution = genetic_algorithm(population_size, generations)

    print("\nFinal Result:")
    print("Best Solution:", best_solution)
    print("Equation Result:", best_solution[0] + 2 * best_solution[1] - best_solution[2])

