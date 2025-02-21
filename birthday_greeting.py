import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

# 定义朋友的名字
friend_name = "唐太宗"

# 定义华丽的生日祝贺网页内容
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{friend_name}生日快乐！</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
            color: #333;
            text-align: center;
            padding: 50px;
            margin: 0;
        }}
        h1 {{
            font-size: 48px;
            color: #d32f2f;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}
        p {{
            font-size: 24px;
            line-height: 1.6;
            margin: 20px 0;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            display: inline-block;
            max-width: 800px;
        }}
        .fireworks {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }}
        .firework {{
            position: absolute;
            width: 10px;
            height: 10px;
            background: #ffeb3b;
            border-radius: 50%;
            animation: explode 1s ease-out infinite;
        }}
        @keyframes explode {{
            0% {{ transform: scale(1); opacity: 1; }}
            100% {{ transform: scale(3); opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 {friend_name}，生日快乐！ 🎂</h1>
        <p>尊敬的{friend_name}，今日是您的华诞，愿这封贺词如春风拂面，为您带来无尽的喜悦与温暖。</p>
        <p>🌺 愿您如春日之花，绚烂绽放；</p>
        <p>🌞 愿您如夏日之阳，光芒万丈；</p>
        <p>🍂 愿您如秋日之果，硕果累累；</p>
        <p>❄️ 愿您如冬日之雪，纯净无瑕。</p>
        <p>🌟 愿您的前路，星光璀璨，步步高升；</p>
        <p>💫 愿您的生活，如诗如画，幸福美满；</p>
        <p>🎁 愿您的每一天，都如今日般，充满惊喜与欢笑。</p>
        <p>🎊 生日快乐，愿您岁岁平安，年年如意！</p>
        <p>🎈 愿您在这特别的日子里，收获满满的祝福与爱！</p>
    </div>

    <!-- 烟花特效 -->
    <div class="fireworks">
        <div class="firework" style="top: 10%; left: 20%;"></div>
        <div class="firework" style="top: 30%; left: 50%;"></div>
        <div class="firework" style="top: 50%; left: 80%;"></div>
        <div class="firework" style="top: 70%; left: 10%;"></div>
        <div class="firework" style="top: 90%; left: 40%;"></div>
    </div>
</body>
</html>
"""

# 将网页内容保存为 HTML 文件
file_name = "birthday_greeting.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

# 启动一个本地 HTTP 服务器
def start_server(port=8000):
    # 切换到文件所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"服务器已启动，请访问 http://localhost:{port}/{file_name}")
    print("在微信中分享以下链接：")
    print(f"http://<你的公网IP>:{port}/{file_name}")
    httpd.serve_forever()

# 打开浏览器预览
webbrowser.open(f"http://localhost:8000/{file_name}")

# 启动服务器
start_server()