from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views.user_views import (
    MyTokenObtainPairView, RegisterViewSet,
)
from myapp.views.article_views import ArticleListView
router = DefaultRouter()
router.register('accounts/register', RegisterViewSet,
                basename='register')
router.register('article/list', ArticleListView,
                basename='article_list')
urlpatterns = [
    path('', include(router.urls)),
    path('accounts/login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]