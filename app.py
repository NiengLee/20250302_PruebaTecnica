from itertools import combinations

def find_best_match(elements, min_calories, max_weigth, top_n=3):
    best_combination    = []
    best_weight         = float('inf')
    best_calories       = 0

    # agregado combinaciones viables
    viable_combinations = []

    for r in range(1, len(elements) + 1):
        for combination in combinations(elements, r):
            total_weigth      = sum(e["peso"] for e in combination)
            total_calories    = sum(e["calorias"] for e in combination)

            if total_weigth <= max_weigth and total_calories >= min_calories:
                viable_combinations.append((list(combination), total_weigth, total_calories))
                if total_weigth < best_weight or (total_weigth == best_weight and total_calories > best_calories):
                    best_weight = total_weigth
                    best_calories = total_calories
                    best_combination = list(combination)
    viable_combinations.sort(key=lambda x: (x[1], -x[2]))

    return best_combination, viable_combinations[:top_n]

if __name__ == "__main__":

    elements = [
        {"nombre": "E1", "peso": 5, "calorias": 3},
        {"nombre": "E2", "peso": 3, "calorias": 5},
        {"nombre": "E3", "peso": 5, "calorias": 2},
        {"nombre": "E4", "peso": 1, "calorias": 8},
        {"nombre": "E5", "peso": 2, "calorias": 3},
    ]

    min_calories    = 15
    max_weight      = 10

    result, top_results = find_best_match(elements, min_calories, max_weight)
    print("Elementos óptimos para llevar:")

    for e in result:
        print(f"{e['nombre']} - Peso: {e['peso']}, Calorías: {e['calorias']}")

    total_weigth    = sum(e["peso"] for e in result)
    total_calories  = sum(e["calorias"] for e in result)
    print(f"Total peso: {total_weigth}, Total calorías: {total_calories}")

    print("\n=======================================================================\n")

    print("Top 3 mejores combinaciones:")
    for i, (combination, total_weight, total_calories) in enumerate(top_results, start=1):
        names = [e["nombre"] for e in combination]
        print(f"\nPuesto {i}: {names}")
        print(f"Peso total: {total_weight}, Calorías totales: {total_calories}")

    print("\n=======================================================================\n")
    print("Por lo tanto, la sugerencia ofrecida en el enunciado sobre la mejor combinacino como 'E1, E2 y E4' NO ES LA MEJOR COMBINACION.\n")
    
    assert set(e['nombre'] for e in result) == {"E1", "E2", "E4"}, "La combinación óptima no es la esperada."
