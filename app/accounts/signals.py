from .models import User, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    """Créer ou mettre à jour le profil utilisateur après création/modification"""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Optionnel : mettre à jour d'autres champs du profil ici si besoin
        profil, _ = UserProfile.objects.get_or_create(user=instance)
        profil.save()
