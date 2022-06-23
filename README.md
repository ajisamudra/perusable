# Readme

## Create GIN index in postgres

[reference](https://stackoverflow.com/questions/65191492/how-to-install-django-pg-trgm-by-makemigrations)

1. add 'django.contrib.postgres' in your INSTALLED_APPS

2. add a customer migration file in the app's migration folder. (The migration files are indexed, It's better to follow that index. e.g. 0044_customer_migrations.py)

3. add TrigramExtension in your migration file

    ```python
    from django.contrib.postgres.operations import TrigramExtension

    class Migration(migrations.Migration):
        dependencies = [
            ('myapp', '0043_latest_migrations'),
        ]

        operations = [
            TrigramExtension(),
        ]
    ```

4. run migrate

    ```bash
    python manage.py migrate
    ```

## Feedback

in `part 2 - spelling mistakes`, when adding queryset class `WineSearchWordFilterSet` there's incomplete instruction on adding the class to model `WineSearchWord`

```python
class WineSearchWordQuerySet(models.query.QuerySet):
    def search(self, query):
        return (
            self.annotate(similarity=TrigramSimilarity("word", query))
            .filter(similarity__gte=0.3)
            .order_by("-similarity")
        )


class WineSearchWord(models.Model):
    word = models.CharField(max_length=255, unique=True)

    objects = WineSearchWordQuerySet.as_manager()  # not written

    def __str__(self) -> str:
        return self.word

```
