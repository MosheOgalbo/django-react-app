"""
URL configuration for OrderManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from OrderManagement_app import views
from OrderManagement_app.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'orders', views.OrderView, 'order')
router.register(r'customer', views.CustomerViewSet, 'customer')
router.register(r'ProductViewSet', views.ProductViewSet, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),

    path("api/notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("api/notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("api/order/create/<int:pk>/", views.OrderViewSet.as_view(), name="create-order"),
    path("api/product/create/<int:pk>/", views.ProductViewSet.as_view({'post': 'create'}), name="create-product"),

    ##*Not supported in this version to bring url from the application
    # path('api/', include("OrderManagement_app.views()"))
]
