from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("order/create/<int:pk>/", views.OrderViewSet.as_view(), name="create-order"),

]
##*Not supported in this version to bring url from the application
