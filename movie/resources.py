from import_export import resources
from .models import MoviesList

class MoviesListResource(resources.ModelResource):
    class Meta:
        model = MoviesList