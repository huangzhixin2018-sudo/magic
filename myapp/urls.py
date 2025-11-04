from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('syntax/', views.syntax_view, name='syntax'),
    path('function-library/', views.function_library_view, name='function_library'),
    path('function-query/', views.function_query_view, name='function_query'),
    path('theme/', views.theme_view, name='theme'),
    path('ai-programming/', views.ai_programming_view, name='ai_programming'),
    path('project/', views.project_view, name='project'),
    path('login/', views.login_view, name='login'),
]

