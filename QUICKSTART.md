# 🚀 快速开始指南

## 第一次使用

### 1. 安装所有依赖

```bash
cd /Volumes/13EjectionPlug/code/AmberMoe.github.io

# 安装根目录依赖
npm install

# 安装 Nuxt 项目依赖
cd apps/site-nuxt && npm install && cd ../..

# 安装 VitePress 依赖
cd apps/docs-vitepress && npm install && cd ../..

# 安装 Hexo 依赖
cd apps/blog-hexo && npm install && cd ../..
```

或者使用一键安装命令：

```bash
npm run install:all
```

### 2. 启动开发服务器

**同时启动所有服务（推荐）:**

```bash
npm run dev
```

访问:

- 主站: http://localhost:3456
- 博客: http://localhost:4567
- 文档: http://localhost:5678

**或者单独启动:**

**Nuxt 主站:**

```bash
cd apps/site-nuxt
npm run dev
```

访问: http://localhost:3456

**VitePress 文档:**

```bash
cd apps/docs-vitepress
npm run docs:dev
```

访问: http://localhost:5678

**Hexo 博客:**

```bash
cd apps/blog-hexo
npm run server
```

访问: http://localhost:4567

### 3. 构建所有项目

```bash
# 从根目录执行
bash build.sh
```

构建完成后，所有静态文件将在 `dist/` 目录中。

## 项目结构说明

```
AmberMoe.github.io/
├─ apps/
│  ├─ site-nuxt/        # 🏠 主站 (Nuxt 4 + NuxtUI)
│  │  ├─ components/    # Vue 组件
│  │  ├─ pages/         # 页面
│  │  ├─ locales/       # 多语言文件
│  │  ├─ public/        # 静态资源
│  │  └─ nuxt.config.ts # Nuxt 配置
│  │
│  ├─ docs-vitepress/   # 📚 文档 (VitePress)
│  │  └─ docs/          # 文档内容
│  │
│  └─ blog-hexo/        # ✍️ 博客 (Hexo)
│     ├─ source/        # 博客文章
│     └─ _config.yml    # Hexo 配置
```

## 常用命令

### 开发

```bash
npm run dev:site    # 启动 Nuxt 开发服务器
npm run dev:docs    # 启动 VitePress 开发服务器
npm run dev:blog    # 启动 Hexo 开发服务器
```

### 构建

```bash
npm run build       # 构建所有项目
npm run build:site  # 只构建 Nuxt
npm run build:docs  # 只构建 VitePress
npm run build:blog  # 只构建 Hexo
```

### 清理

```bash
npm run clean      # 清理所有构建文件和依赖
```

## 开发提示

### 修改主站内容

1. 页面文件在 `apps/site-nuxt/pages/`
2. 组件文件在 `apps/site-nuxt/components/`
3. 多语言翻译在 `apps/site-nuxt/locales/`
4. 静态资源放在 `apps/site-nuxt/public/`

### 添加博客文章

```bash
cd apps/blog-hexo
npx hexo new post "文章标题"
```

然后编辑 `source/_posts/文章标题.md`

### 添加文档

在 `apps/docs-vitepress/docs/` 目录下创建或编辑 Markdown 文件

## 部署

### 自动部署（推荐）

推送到 `main` 分支会自动触发 GitHub Actions 部署

### 手动部署

```bash
# 构建
npm run build

# 然后将 dist/ 目录上传到服务器
```

## 需要帮助？

- 查看 [REFACTOR_SUMMARY.md](REFACTOR_SUMMARY.md) 了解完整的项目说明
- 查看 [PLAN.md](PLAN.md) 了解原始需求
- Nuxt 文档: https://nuxt.com
- VitePress 文档: https://vitepress.dev
- Hexo 文档: https://hexo.io

## 下一步做什么？

1. ✅ 测试开发服务器是否正常运行
2. ✅ 查看各个页面的显示效果
3. ⏭️ 开始添加你的内容
4. ⏭️ 自定义样式和布局
5. ⏭️ 配置 Cloudflare Pages 部署

祝你开发愉快！🎉
