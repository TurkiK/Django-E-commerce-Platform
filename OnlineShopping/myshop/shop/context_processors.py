from .models import UserProfile

def add_balance_to_context(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        return {'user_balance': user_profile.balance}
    return {}
