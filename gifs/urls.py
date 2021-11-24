from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', homepage, name = 'homepage'),
    path('category/<int:category_id>', category, name = 'category'),
    path('categories/', categories, name = 'categories'),
    path('gif/<int:gif_id>', gif, name = 'gif'),
    path ('gif/<int:gif_id>/<int:liked>', gif_like_action, name = 'like_link')
]