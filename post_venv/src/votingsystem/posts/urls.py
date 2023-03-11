from django.urls import path
from .views import *

urlpatterns = [
    path('post',PostList.as_view()),
    path('post/<int:pk>/vote/', VoteCreate.as_view()),
    path('post/<int:pk>/', PostRetrieveDestroy.as_view()),
    path('signup/',signup),
    path('login/',login),
]