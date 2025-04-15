from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import User, UserProfile

# === Serializer du modèle utilisateur principal ===
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a new user with encrypted password"""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)

        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    def validate_email(self, value):
        """Check if the email is already in use during registration"""
        # Cette validation ne s'applique qu'à la création (pas à la mise à jour)
        if self.instance is None and get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value

    def validate_password(self, value):
        """Check if the password is strong enough"""
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value


# === Serializer du modèle UserProfile ===
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the user profile"""

    class Meta:
        model = UserProfile
        fields = '__all__'  # ou ['user', 'avatar', 'bio', etc.] selon ton modèle


# === Serializer pour l'authentification (login) ===
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not email or not password:
            msg = _('Email and password are required.')
            raise serializers.ValidationError(msg, code='authorization')
            
        user = authenticate(
            request=self.context.get('request'),
            username=email,  # Django utilise username par défaut mais on passe l'email
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


# === Serializer pour login (alternative) ===
class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    
    def validate(self, attrs):
        """Validate credentials and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError("Email and password are required")
            
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            raise serializers.ValidationError("Invalid credentials")
            
        attrs['user'] = user
        return attrs