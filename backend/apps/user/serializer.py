from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import User,PreferOttContentGenre
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

# class PreferOttContentGenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=PreferOttContentGenre
#         fields='__all__'

#     def create(self,validated_data):
#         prefer_ott_content_genre=PreferOttContentGenre.objects.create(
#             **validated_data
#             )
#         return prefer_ott_content_genre

#회원가입
class CreateUserSerializer(serializers.ModelSerializer):

    #prefer_ott_content_genre_serializer = PreferOttContentGenreSerializer()
    class Meta:
        model= User
        # exclude=[
        #     'last_login',
        #     'is_active',
        #     'is_admin',
        #     'is_staff',
        #     ]
        fields=[
            'username',
            'password',
            'nickname',
            'birthday',
            'gender',
            'job',
            'region',
            'watch_time',
        ]
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):
        #username=validated_data['username']
        #password=validated_data['password']
        #prefer_ott_content_genre=validated_data['prefer_ott_content_genre']
        check_user=User.objects.get(validated_data['username'])
        if check_user is not None:
            raise serializers.ValidationError('해당 아이디는 중복됐습니다. 다시 작성해주세요.')
        
        user=User.objects.create_user(
            #username=username, 
            **validated_data
        )
        return user

#접속 유지 확인용
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username')


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#로그인
class LoginUserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=128,write_only=True)
    token=serializers.CharField(max_length=255,read_only=True)


    def validate(self,data):
        username=data.get('username',None)
        password=data.get('password',None)
        user=authenticate(username=username,password=password)

        if user is None:
            raise serializers.ValidationError('해당 아이디는 없는 아이디입니다.')

        try:
            payload=JWT_PAYLOAD_HANDLER(user)
            jwt_token=JWT_ENCODE_HANDLER(payload)
            update_last_login(None,user)

        except User.DoesNotExist:
            raise serializers.ValidationError("아이디나 비밀번호가 맞지 않습니다.")

        login_serialize={
            'username':user.username,
            'token':jwt_token,
        }
        return login_serialize

