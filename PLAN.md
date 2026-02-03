# 这是一个Vtuber 个人博客+官网项目

项目由nuxt 官网+hexo 博客+vitepress 文档三部分组成,全部为静态文件加载.当前项目已有资源可以利用,为一些素材图片,但是整个架构需要重构,而不使用当前 html 代码.

# 开发需求
1. 开发语言:typescript
2. 前端框架:Nuxt
3. UI 框架:NuxtUI
4. 博客系统:hexo
5. 文档系统:vitepress
6. CI/CD:GitHub action/Cloudflare page
7. i18n 多语言翻译:英语(默认),法语,西班牙语,中文,日语,韩语
8. 支持主题模式:浅色模式和深色模式,默认浅色主题模式.

# 核心功能
1. 首页是一个介绍宣传页面,展示所有 Vtuber 相关内容,Hexobanner 内嵌展示视频播放器.视频地址:https://www.youtube.com/watch?v=XEKJ45QjWME
2. 首页其他部分模块,展示一些介绍内容,参考原来的 html 文件.
3. 推荐目录结构
repo/
├─ apps/
│  ├─ site-nuxt/
│  ├─ docs-vitepress/
│  └─ blog-hexo/
│
├─ dist/              # CF Pages 的 output directory
│  ├─ index.html      # Nuxt
│  ├─ _nuxt/
│  ├─ docs/
│  │   ├─ index.html
│  │   └─ assets/
│  └─ blog/
│      ├─ index.html
│      └─ assets/
│
├─ package.json
└─ build.sh
4. 各自 build → 拷贝到统一 dist
Nuxt（SSG 模式）
cd apps/site-nuxt
npx nuxi generate
# 输出到 .output/public
VitePress
cd apps/docs-vitepress
npx vitepress build
# 输出到 .vitepress/dist
Hexo
cd apps/blog-hexo
npx hexo generate
# 输出到 public

# UI页面
1. 首页
2. 博客页面
3. 文档页面
4. 404页面
5. 社交媒体页面
6. 联系页面
7. 隐私政策页面
8. 服务条款页面
9. 关于页面
10. 捐助者页面 (名字列表,展示所有捐助的人,顶部放一个 buymeacoffee 的链接)
11. 

# 社交媒体
1. Twitter: https://twitter.com/AmberMoeVT
2. YouTube: https://www.youtube.com/@AmberMoeVT
3. TikTok: https://www.tiktok.com/@ambermoevt
4. Instagram: https://www.instagram.com/ambermoevt/
5. Facebook: https://www.facebook.com/AmberMoeVT/
6. Reddit: https://www.reddit.com/user/AmberMoeVT/
7. Discord: https://discord.gg/ambermoevt/
8. Twitch: https://www.twitch.tv/ambermoevt/
9. GitHub: https://github.com/AmberMoeVT/
10. LinkedIn: https://www.linkedin.com/in/ambermoevt/
11. Telegram: https://t.me/ambermoevt/
12. WhatsApp: https://wa.me/1234567890
13. WeChat: https://www.wechat.com/en/
14. QQ: https://www.qq.com/
15. Weibo: https://www.weibo.com/
16. Douyin: https://www.douyin.com/
17. Kuaishou: https://www.kuaishou.com/
18. Bilibili: https://www.bilibili.com/
19. AcFun: https://www.acfun.cn/
20. Niconico: https://www.nicovideo.jp/
21. YouTube Shorts: https://www.youtube.com/shorts/
22. YouTube Music: https://music.youtube.com/
23. YouTube Kids: https://www.youtube.com/kids/
24. YouTube TV: https://tv.youtube.com/
25. YouTube Premium: https://www.youtube.com/premium/
26. YouTube Music Premium: https://music.youtube.com/premium/
27. YouTube Kids Premium: https://www.youtube.com/kids/premium/
28. YouTube TV Premium: https://tv.youtube.com/premium/
29. YouTube Premium Music: https://www.youtube.com/premium/music/
30. YouTube Premium Kids: https://www.youtube.com/kids/premium/
31. YouTube Premium TV: https://tv.youtube.com/premium/
32. YouTube Premium Music Kids: https://www.youtube.com/kids/premium/music/
33. YouTube Premium Music TV: https://tv.youtube.com/premium/music/
34. YouTube Premium Kids TV: https://tv.youtube.com/kids/premium/
35. YouTube Premium Kids Music TV: https://tv.youtube.com/kids/premium/music/
36. YouTube Premium Kids Music TV Premium: https://tv.youtube.com/kids/premium/music/premium/
37. YouTube Premium Kids Music TV Premium Music: https://tv.youtube.com/kids/premium/music/premium/
38. YouTube Premium Kids Music TV Premium Music Kids: https://tv.youtube.com/kids/premium/music/premium/
39. YouTube Premium Kids Music TV Premium Music Kids TV: https://tv.youtube.com/kids/premium/music/premium/
40. YouTube Premium Kids Music TV Premium Music Kids TV Premium: https://tv.youtube.com/kids/premium/music/premium/
41. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music: https://tv.youtube.com/kids/premium/music/premium/
42. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids: https://tv.youtube.com/kids/premium/music/premium/
43. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV: https://tv.youtube.com/kids/premium/music/premium/
44. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium: https://tv.youtube.com/kids/premium/music/premium/
45. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music: https://tv.youtube.com/kids/premium/music/premium/
46. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids: https://tv.youtube.com/kids/premium/music/premium/
47. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids TV: https://tv.youtube.com/kids/premium/music/premium/
48. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids TV Premium: https://tv.youtube.com/kids/premium/music/premium/
49. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids TV Premium Music: https://tv.youtube.com/kids/premium/music/premium/
50. YouTube Premium Kids Music TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids TV Premium Music Kids: https://tv.youtube.com/kids/premium/music/premium/
