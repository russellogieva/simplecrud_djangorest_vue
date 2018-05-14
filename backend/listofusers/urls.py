from rest_framework import routers

from .views import UsersViewSet, RolesViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, base_name="Users")
router.register(r'roles', RolesViewSet)


# URLs настраиваются автоматически роутером
urlpatterns = router.urls