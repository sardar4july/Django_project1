from rest_framework import routers
from .viewsets import userviewsets


router = routers.DefaultRouter()
router.register('host', userviewsets, base_name='user_api')