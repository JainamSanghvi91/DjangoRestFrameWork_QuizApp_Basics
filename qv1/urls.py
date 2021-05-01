from django.urls import path
from qv1.views import quiz_view, quiz_put_view, quiz_delete_view
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('<slug>/', quiz_view, name='quizes'),
    path('<slug>/put/', quiz_put_view, name='quizes'),
    path('<slug>/delete/', quiz_delete_view, name='quizes'),
]


# router = DefaultRouter()
# router.register(r'quizes', QuizView, basename='quiz')
# urlpatterns = []
# urlpatterns += router.urls

