from itertools import combinations

def get_best_combinations(elements, min_calories, max_weight):
    """
    Encuentra las combinaciones óptimas de elementos que cumplen los requerimientos.

    Recibe:
    - elements: Lista de objetos con nombre, peso y calorias.
    - min_calories: Calorías mínimas requeridas.
    - max_weight: Peso máximo permitido.

    Retorna:
    - best_combination: La mejor combinación de elementos.
    - top_3_combinations: Las tres mejores combinaciones ordenadas.
    """
    best_combination = []
    best_weight = float('inf')
    best_calories = 0
    viable_combinations = []

    for r in range(1, len(elements) + 1):
        for combination in combinations(elements, r):
            total_weight = sum(e["peso"] for e in combination)
            total_calories = sum(e["calorias"] for e in combination)

            if total_weight <= max_weight and total_calories >= min_calories:
                viable_combinations.append((list(combination), total_weight, total_calories))

                if total_weight < best_weight or (total_weight == best_weight and total_calories > best_calories):
                    best_weight = total_weight
                    best_calories = total_calories
                    best_combination = list(combination)

    viable_combinations.sort(key=lambda x: (x[1], -x[2]))

    return best_combination, viable_combinations[:3]
