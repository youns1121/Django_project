from django.urls import path
from blog import views

urlpatterns = [# blog app 서비스로 요청을 넘겨주는 기능

    path('', views.index), # 메인 페이지
    path('<int:pk>', views.single_post_page), # 디테일

    path('cbv', views.PostList.as_view()),
    path('cbv/<int:pk>', views.PostDetail.as_view()),
    path('cbv_post', views.NewPostList.as_view()),


]
