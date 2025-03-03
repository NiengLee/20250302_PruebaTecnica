from itertools import combinations
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FindBestMatchSerializer
from .utils import get_best_combinations
from .models import Element, Combination

class FindBestMatch(APIView):
    """
    ejemplo api:
    http://127.0.0.1:8000/api/app_matching/find-best-match/
    {
        "elements": [
            {"nombre": "E1", "peso": 5, "calorias": 3},
            {"nombre": "E2", "peso": 3, "calorias": 5},
            {"nombre": "E3", "peso": 5, "calorias": 2},
            {"nombre": "E4", "peso": 1, "calorias": 8},
            {"nombre": "E5", "peso": 2, "calorias": 3}
        ],
        "min_calories": 15,
        "max_weight": 10
    }
    """

    serializer_class = FindBestMatchSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elements = serializer.validated_data["elements"]
        min_calories = serializer.validated_data["min_calories"]
        max_weight = serializer.validated_data["max_weight"]

        best_combination, top_3_combinations = get_best_combinations(elements, min_calories, max_weight)

        elementos_guardados = {}
        for element in elements:
            obj, _ = Element.objects.get_or_create(
                nombre=element["nombre"],
                defaults={"peso": element["peso"], "calorias": element["calorias"]}
            )
            elementos_guardados[element["nombre"]] = obj

        combinacion = Combination.objects.create(
            total_peso=sum(e["peso"] for e in best_combination),
            total_calorias=sum(e["calorias"] for e in best_combination)
        )
        combinacion.elementos.set([elementos_guardados[e["nombre"]] for e in best_combination])

        return Response({
            "la mejor combinacion es": [e["nombre"] for e in best_combination],
            "best_combination": best_combination,
            "top_3_combinations": [
                {
                    "elements": comb[0],
                    "total_weight": comb[1],
                    "total_calories": comb[2]
                } for comb in top_3_combinations
            ]
        }, status=status.HTTP_200_OK)