from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'tasks/statuses', views.TaskStatusView, basename='status')
router.register(r'tasks', views.TaskView, basename='task')
router.register(r'fin_operations', views.FinOperationView, basename='fin_operation')
router.register(r'fin_operations/types', views.FinOperationTypeView, basename='type')
router.register(r'fin_operations/tags', views.FinOperationTagView, basename='tag')
router.register(r'notes', views.NoteView, basename='note')
router.register(r'notes/tags', views.NoteTagView, basename='tag')
router.register(r'notes', views.NoteTypeView, basename='type')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
