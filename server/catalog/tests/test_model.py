from catalog.models import Wine, WineSearchWord


def test_wine_search_words_populated_on_save(self):
    WineSearchWord.objects.all().delete()
    Wine.objects.create(
        country="US",
        description="A cheap, but inoffensive wine.",
        points=80,
        price=1.99,
        variety="Pinot Grigio",
        winery="Charles Shaw",
    )
    wine_search_words = (
        WineSearchWord.objects.all().order_by("word").values_list("word", flat=True)
    )
    self.assertListEqual(
        ["a", "but", "charles", "cheap", "inoffensive", "shaw", "wine"],
        list(wine_search_words),
    )
