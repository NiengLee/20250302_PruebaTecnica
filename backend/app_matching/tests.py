from django.test import TestCase
from app_matching.utils import get_best_combinations

class MatchingTests(TestCase):
    def test_get_best_combinations(self):
        elements = [
            {"nombre": "E1", "peso": 5, "calorias": 3},
            {"nombre": "E2", "peso": 3, "calorias": 5},
            {"nombre": "E3", "peso": 5, "calorias": 2},
            {"nombre": "E4", "peso": 1, "calorias": 8},
            {"nombre": "E5", "peso": 2, "calorias": 3}
        ]
        min_calories = 15
        max_weight = 10

        best_combination, top_3_combinations = get_best_combinations(elements, min_calories, max_weight)

        # Bajo este testing, nunca sera la combinacion obtima y por lo tanto siempre saldra error
        self.assertEqual([e["nombre"] for e in best_combination], ["E1", "E2", "E4"])