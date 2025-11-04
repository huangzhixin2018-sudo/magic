from django.shortcuts import render

# 首页
def index_view(request):
    return render(request, 'pages/index.html')

# 语法页面
def syntax_view(request):
    return render(request, 'pages/syntax.html')

# 函数库页面
def function_library_view(request):
    return render(request, 'pages/function_library.html')

# 函数查询页面
def function_query_view(request):
    return render(request, 'pages/function_query.html')

# 主题页面
def theme_view(request):
    return render(request, 'pages/theme.html')

# AI编程页面
def ai_programming_view(request):
    return render(request, 'pages/ai_programming.html')

# 项目页面
def project_view(request):
    return render(request, 'pages/project.html')

# 登录页面
def login_view(request):
    return render(request, 'pages/login.html')
