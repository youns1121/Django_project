from django.contrib import admin
from django.urls import path, include

urlpatterns = [# blog app 서비스로 요청을 넘겨주는 기능
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('blog.urls')),
    path('cbv_post/', include('blog.urls'))
]
