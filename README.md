# 猫国网站

这是一个基于 Flask 的猫国主题站点，包含：
- 登录页
- 主页展示
- 画图工具
- 猫咪证件生成
- 头像下载
- 文章发布区

## 运行方式

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python flask_app.py
```

访问：
- 登录页： http://localhost:5000/login
- 默认账号： cat
- 默认密码： 123456

## 部署建议

GitHub 仅用于托管代码；如果需要真正在线访问，建议部署到 Render、Railway、PythonAnywhere 或 Heroku 等平台。
