from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('notes', views.CreateListRetrieveNoteView, basename='create_list_retrieve_note')
router.register(r'notes/update', views.UpdateNoteView, basename='update-note')
router.register(r'notes/destroy', views.DestroyNoteView, basename='delete-note')
router.register('tags', views.CreateListTagView, basename='create_list_retrieve_tag')



urlpatterns = [
    path('', include(router.urls)),

    ]
