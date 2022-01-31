from rest_framework.routers import SimpleRouter
from django.urls import path
from accounts.views import UserModelViewSet, UserRegistrationView

router = SimpleRouter()

router.register('users', UserModelViewSet)

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]

urlpatterns += router.urls