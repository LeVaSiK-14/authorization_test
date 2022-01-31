from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts.models import User
from accounts.serializers import UserSerializer, UserRegistrationSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwagrs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = User.objects.create_user(
            username=data['username'],
            avatar=data['avatar'],
            number=data['number'],
        )
        user.set_password(data['password'])
        user.save()


        token = Token.objects.create(user=user)

        return Response({'token': token.key})


