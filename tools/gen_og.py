"""生成站点分享卡片 og.png（1200x630）。

内容与站点首页一致：标题 + 一行说明 + 域名。
字体用 Windows 自带的微软雅黑，避免中文豆腐块。
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (15, 17, 21)
INK = (232, 234, 238)
MUTED = (154, 162, 175)
ACCENT = (116, 162, 255)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 左侧竖条
d.rectangle([0, 0, 10, H], fill=ACCENT)

title_font = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 62)
sub_font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 34)
small_font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 26)

x = 96
d.text((x, 132), "把大模型接进 Java 服务，", font=title_font, fill=INK)
d.text((x, 214), "中间那一段", font=title_font, fill=INK)

d.text((x, 330), "接入手册 · 踩坑手册 · 完整项目", font=sub_font, fill=ACCENT)

d.text((x, 410), "每个结论都能跑、能复现、能对上代码；", font=small_font, fill=MUTED)
d.text((x, 452), "每个项目都写清它没验证到什么程度。", font=small_font, fill=MUTED)

d.text((x, 540), "pgy763.github.io", font=sub_font, fill=MUTED)

img.save(r"D:\Github-code\.github.io\og.png", "PNG", optimize=True)
print("saved", img.size)