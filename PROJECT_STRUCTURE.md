# 📁 项目结构说明

## 项目根目录

```
AmberMoe.github.io/
├── 📁 .github/              # GitHub 配置
│   └── workflows/          # CI/CD 工作流
│       ├── deploy.yml      # GitHub Pages 部署
│       └── cloudflare.yml  # Cloudflare Pages 部署
│
├── 📁 .vscode/             # VSCode 配置
│   ├── extensions.json    # 推荐扩展
│   └── settings.json      # 编辑器设置
│
├── 📁 apps/                # 子项目
│   ├── site-nuxt/         # Nuxt 主站
│   ├── docs-vitepress/    # VitePress 文档
│   └── blog-hexo/         # Hexo 博客
│
├── 📁 assets/              # 资源备份
│   ├── images/            # 图片资源
│   └── index.html         # 原始HTML备份
│
├── 📁 dist/                # 构建输出（.gitignore）
│   ├── index.html         # Nuxt 主站
│   ├── _nuxt/             # Nuxt 资源
│   ├── blog/              # Hexo 博客
│   └── docs/              # VitePress 文档
│
├── 📄 .gitignore           # Git 忽略文件
├── 📄 build.sh             # 统一构建脚本
├── 📄 CNAME                # 域名配置
├── 📄 package.json         # 根配置
├── 📄 README.md            # 项目说明
├── 📄 PLAN.md              # 原始需求
├── 📄 QUICKSTART.md        # 快速开始
├── 📄 REFACTOR_SUMMARY.md  # 重构总结
├── 📄 TROUBLESHOOTING.md   # 故障排查
├── 📄 CHECKLIST.md         # 验收清单
└── 📄 amber-moe.code-workspace  # VSCode 工作区
```

---

## Nuxt 主站结构 (apps/site-nuxt/)

```
site-nuxt/
├── 📁 .git/                # Git 子仓库（Nuxt 初始化创建）
├── 📁 .nuxt/               # Nuxt 构建缓存（.gitignore）
├── 📁 app/                 # 应用配置（Nuxt 自动创建）
│
├── 📁 components/          # Vue 组件
│   ├── AboutSection.vue   # 关于区块
│   ├── AppFooter.vue      # 页脚
│   ├── AppHeader.vue      # 导航栏
│   ├── SocialLink.vue     # 社交媒体链接
│   ├── SocialSection.vue  # 社交媒体区块
│   └── VideoPlayer.vue    # 视频播放器
│
├── 📁 locales/             # 多语言文件
│   ├── en.json            # 英语
│   ├── fr.json            # 法语
│   ├── es.json            # 西班牙语
│   ├── zh.json            # 中文
│   ├── ja.json            # 日语
│   └── ko.json            # 韩语
│
├── 📁 pages/               # 页面路由
│   ├── about.vue          # 关于页面
│   ├── blog.vue           # 博客重定向
│   ├── docs.vue           # 文档重定向
│   ├── donors.vue         # 捐赠者页面
│   ├── privacy.vue        # 隐私政策
│   └── terms.vue          # 服务条款
│
├── 📁 public/              # 静态资源
│   ├── favicon.ico        # 网站图标
│   ├── apple-touch-icon.png  # iOS 图标
│   └── *.png              # 其他图片
│
├── 📁 node_modules/        # 依赖（.gitignore）
│
├── 📄 .gitignore           # Git 忽略
├── 📄 app.vue              # 应用入口/首页
├── 📄 nuxt.config.ts       # Nuxt 配置
├── 📄 package.json         # 项目配置
├── 📄 tsconfig.json        # TypeScript 配置
└── 📄 README.md            # 项目说明
```

### 关键文件说明

#### `app.vue` - 应用入口

首页布局，包含：

- Hero 区块（标题、描述、YouTube 视频）
- About 区块
- Social Media 区块
- Header 和 Footer

#### `nuxt.config.ts` - Nuxt 配置

配置内容：

- 模块：@nuxt/ui, @nuxtjs/i18n, @nuxtjs/color-mode
- i18n：6种语言配置
- 主题模式：浅色/深色
- SEO meta 标签

#### Components（组件）

- **AppHeader**: 响应式导航栏，包含语言选择器和主题切换
- **AppFooter**: 页脚，包含快速链接和版权信息
- **VideoPlayer**: YouTube 视频嵌入组件
- **AboutSection**: 关于区块
- **SocialSection**: 社交媒体展示区块
- **SocialLink**: 单个社交媒体链接组件

---

## Hexo 博客结构 (apps/blog-hexo/)

```
blog-hexo/
├── 📁 node_modules/        # 依赖（.gitignore）
├── 📁 public/              # 构建输出（.gitignore）
├── 📁 scaffolds/           # 文章模板
│   ├── draft.md
│   ├── page.md
│   └── post.md
├── 📁 source/              # 源文件
│   └── _posts/            # 博客文章
│       └── hello-world.md
├── 📁 themes/              # 主题
│   └── landscape/         # 默认主题
│
├── 📄 .gitignore           # Git 忽略
├── 📄 _config.yml          # Hexo 配置
├── 📄 db.json              # 数据库（.gitignore）
├── 📄 package.json         # 项目配置
└── 📄 tsconfig.json        # TypeScript 配置
```

### 关键文件说明

#### `_config.yml` - Hexo 配置

配置内容：

- 站点信息（标题、描述、作者）
- URL 配置
- 目录结构
- 文章设置
- 部署设置

#### `source/_posts/` - 博客文章

存放所有博客文章的 Markdown 文件

---

## VitePress 文档结构 (apps/docs-vitepress/)

```
docs-vitepress/
├── 📁 docs/                # 文档内容
│   ├── 📁 .vitepress/     # VitePress 配置
│   │   ├── cache/         # 缓存（.gitignore）
│   │   ├── dist/          # 构建输出（.gitignore）
│   │   └── config.mts     # VitePress 配置
│   │
│   ├── api-examples.md    # API 示例
│   ├── index.md           # 首页
│   └── markdown-examples.md  # Markdown 示例
│
├── 📁 node_modules/        # 依赖（.gitignore）
│
├── 📄 .gitignore           # Git 忽略
├── 📄 package.json         # 项目配置
└── 📄 tsconfig.json        # TypeScript 配置
```

### 关键文件说明

#### `.vitepress/config.mts` - VitePress 配置

配置内容：

- 站点标题和描述
- base path: `/docs/`
- 导航栏配置
- 侧边栏配置
- 社交媒体链接
- 页脚信息

#### `docs/*.md` - 文档页面

Markdown 格式的文档内容

---

## 构建输出结构 (dist/)

构建完成后的 `dist/` 目录结构：

```
dist/
├── index.html              # Nuxt 主站首页
├── about/                  # 关于页面
├── donors/                 # 捐赠者页面
├── privacy/                # 隐私政策
├── terms/                  # 服务条款
│
├── _nuxt/                  # Nuxt 静态资源
│   ├── *.js               # JavaScript 文件
│   ├── *.css              # CSS 文件
│   └── assets/            # 图片等资源
│
├── blog/                   # Hexo 博客
│   ├── index.html         # 博客首页
│   ├── archives/          # 归档页面
│   └── *.html             # 文章页面
│
└── docs/                   # VitePress 文档
    ├── index.html         # 文档首页
    ├── assets/            # 文档资源
    └── *.html             # 文档页面
```

---

## 开发工作流

### 1. 开发阶段

```bash
# 启动 Nuxt 主站
cd apps/site-nuxt
npm run dev         # http://localhost:3000

# 启动 VitePress 文档
cd apps/docs-vitepress
npm run docs:dev    # http://localhost:5173

# 启动 Hexo 博客
cd apps/blog-hexo
npm run server      # http://localhost:4000
```

### 2. 构建阶段

```bash
# 从根目录执行
bash build.sh

# 或单独构建
npm run build:site
npm run build:docs
npm run build:blog
```

### 3. 部署阶段

```
git push origin main
↓
GitHub Actions 触发
↓
并行构建三个项目
↓
合并到 dist/ 目录
↓
部署到 GitHub Pages / Cloudflare Pages
```

---

## 文件命名规范

### Vue 组件

- PascalCase: `AppHeader.vue`, `VideoPlayer.vue`
- 以 App 开头的为全局组件

### 页面文件

- kebab-case: `about.vue`, `privacy.vue`
- 会自动生成对应路由

### 配置文件

- kebab-case: `nuxt.config.ts`, `_config.yml`
- TypeScript 配置: `.ts` / `.mts`

### 文档文件

- kebab-case: `quick-start.md`, `api-reference.md`
- Markdown 格式: `.md`

---

## 端口分配

| 服务      | 端口 | 用途           |
| --------- | ---- | -------------- |
| Nuxt      | 3456 | 主站开发服务器 |
| VitePress | 5678 | 文档开发服务器 |
| Hexo      | 4567 | 博客开发服务器 |

---

## 环境变量

目前项目不需要环境变量，所有配置都在配置文件中。

如需添加环境变量：

1. 创建 `.env` 文件
2. 在 `.gitignore` 中添加
3. 在配置文件中使用 `process.env.VAR_NAME`

---

## 依赖管理

- **根目录**: 只有 package.json，无实际依赖
- **site-nuxt**: 完整的 Nuxt 生态系统依赖
- **docs-vitepress**: VitePress 及其依赖
- **blog-hexo**: Hexo 及其依赖

每个子项目独立管理依赖，互不影响。
