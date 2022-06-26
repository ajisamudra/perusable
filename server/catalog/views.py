from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Match, Term
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView

from . import constants
from .models import Wine, WineSearchWord
from .serializers import WineSerializer, WineSearchWordSerializer
from .filters import WineFilterSet, WineSearchWordFilterSet


class WinesView(ListAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    filterset_class = WineFilterSet


class WineSearchWordsView(ListAPIView):
    queryset = WineSearchWord.objects.all()
    serializer_class = WineSearchWordSerializer
    filterset_class = WineSearchWordFilterSet

    def filter_queryset(self, request):
        return super().filter_queryset(request)[:100]


class ESWinesView(APIView):
    def get(self, request, *args, **kwargs):
        query = self.request.query_params.get("query")
        country = self.request.query_params.get("country")
        points = self.request.query_params.get("points")

        # build elasticsearch query
        search = Search(index=constants.ES_INDEX)
        q = {"should": [], "filter": []}

        # build should clause
        if query:
            q["should"] = [
                Match(variety=query),
                Match(winery=query),
                Match(description=query),
            ]
            q["minimum_should_match"] = 1

        # build filter clause
        if country:
            q["filter"].append(Term(country=country))
        if points:
            q["filter"].append(Term(points=points))

        response = (
            search.query(
                "bool",
                **q,
            )
            .params(size=100)
            .execute()
        )

        if response.hits.total.value > 0:
            return Response(
                data=[
                    {
                        "id": hit.meta.id,
                        "country": hit.country,
                        "description": hit.description,
                        "points": hit.points,
                        "price": hit.price,
                        "variety": hit.variety,
                        "winery": hit.winery,
                    }
                    for hit in response
                ]
            )
        else:
            return Response(data=[])
