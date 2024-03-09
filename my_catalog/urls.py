from django.urls import path

from . import views

urlpatterns = [
    path('',views.catalog_home, name='catalog_home' ),
    path('create', views.create, name='create'),
    path('<int:pk>', views.StoryDetailView.as_view(), name='story-detail'),
    path('<int:pk>/update', views.StoryUpdateView.as_view(), name='story-update'),
    path('<int:pk>/delete', views.StoryDeleteView.as_view(), name='story-delete')

]