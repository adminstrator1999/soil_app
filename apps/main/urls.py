from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet
from main.api.files import FileViewSet
from main.api.news import NewsViewSet
from main.api.contact import ContactApiView
from main.api.employee import EmployeeViewSet
from main.api.about import HistoryViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, 'user')
router.register('file', FileViewSet, 'file')
router.register('news', NewsViewSet, 'news')
router.register('employee', EmployeeViewSet, 'employee')
router.register('history', HistoryViewSet, 'history')

urlpatterns = [
    path('contact/', ContactApiView, name='contact'),
    path('', include(router.urls))
]
