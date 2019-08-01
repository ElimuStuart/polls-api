from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from .views import polls_list, polls_detail
from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView

schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("swagger-docs/", schema_view),
]

urlpatterns += router.urls
