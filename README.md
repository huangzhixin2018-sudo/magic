# Django 网站项目

这是一个 Django 网站项目，可以部署到 Vercel。

## 本地开发

```bash
# 安装依赖
pip install -r requirements.txt

# 运行迁移（如果需要）
python manage.py migrate

# 启动开发服务器
python manage.py runserver
```

## Vercel 部署

### 1. 在 Vercel 上连接 GitHub 仓库

1. 访问 [Vercel](https://vercel.com)
2. 使用 GitHub 账号登录
3. 点击 "New Project"
4. 选择你的 GitHub 仓库 `huangzhixin2018-sudo/magic`
5. 点击 "Import"

### 2. 配置环境变量（可选）

在 Vercel 项目设置中添加环境变量：
- `SECRET_KEY`: Django 密钥（生产环境建议使用随机字符串）
- `DEBUG`: 设置为 `False`（生产环境）

### 3. 部署

Vercel 会自动检测 `vercel.json` 配置文件并开始部署。

### 4. 静态文件处理

静态文件已配置为通过 Vercel 的 CDN 提供。如果需要收集静态文件，可以在部署前运行：

```bash
python manage.py collectstatic --noinput
```

## 项目结构

```
myproject/
├── api/                    # Vercel serverless 函数
│   ├── __init__.py
│   └── index.py           # WSGI 应用入口
├── myapp/                  # Django 应用
├── myproject/              # Django 项目设置
├── static/                 # 静态文件（CSS, JS）
├── templates/              # HTML 模板
├── manage.py
├── requirements.txt        # Python 依赖
└── vercel.json            # Vercel 配置
```

## 注意事项

- 数据库：当前使用 SQLite。在生产环境中，建议使用 PostgreSQL 或其他数据库服务。
- 静态文件：已配置为通过 `/static/` 路径访问。
- 环境变量：建议在生产环境中设置 `SECRET_KEY` 和 `DEBUG=False`。

## 故障排除

如果遇到 404 错误：
1. 检查 `vercel.json` 配置是否正确
2. 确保 `api/index.py` 文件存在
3. 检查 Vercel 部署日志中的错误信息

