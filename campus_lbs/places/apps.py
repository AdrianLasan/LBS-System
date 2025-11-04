from django.apps import AppConfig

class PlacesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # IMPORTANT: include the parent package because places is under campus_lbs/
    name = "campus_lbs.places"
    # Keep the label as 'places' so your fixtures can still use "model": "places.category"
    label = "places"
