# 🚀 开发服务器端口更新说明

## 修改的端口

项目使用连续端口，便于记忆和管理：

| 服务           | 原端口 | 新端口    | 访问地址              |
| -------------- | ------ | --------- | --------------------- |
| Nuxt 主站      | 3456   | **3000**  | http://localhost:3000 |
| Hexo 博客      | 4567   | **3001**  | http://localhost:3001 |
| VitePress 文档 | 5678   | **3002**  | http://localhost:3002 |
| HMR WebSocket  | 24690  | **24000** | -                     |

## 快速启动

### 同时启动所有服务（推荐）

```bash
npm run dev
```

这个命令会并行启动三个开发服务器，你可以同时访问：

- 主站: http://localhost:3000
- 博客: http://localhost:3001
- 文档: http://localhost:3002/docs/

### 单独启动服务

```bash
# 启动 Nuxt 主站
npm run dev:site

# 启动 Hexo 博客
npm run dev:blog

# 启动 VitePress 文档
npm run dev:docs
```

## 配置文件说明

### Nuxt 主站端口配置

文件: `apps/site-nuxt/nuxt.config.ts`

```typescript
devServer: {
  port: 3456
},
```

### Hexo 博客端口配置

文件: `apps/blog-hexo/_config.yml`

```yaml
server:
  port: 4567
  log: false
```

### VitePress 文档端口配置

文件: `apps/docs-vitepress/package.json`

```json
"docs:dev": "vitepress dev docs --port 5678"
```

## i18n 配置修复

多语言文件需要放在 `apps/site-nuxt/i18n/locales/` 目录下，而不是 `apps/site-nuxt/locales/`。

目录结构：

```
apps/site-nuxt/
├── i18n/
│   └── locales/
│       ├── en.json
│       ├── fr.json
│       ├── es.json
│       ├── zh.json
│       ├── ja.json
│       └── ko.json
└── locales/     # 保留作为备份
```

nuxt.config.ts 中的配置：

```typescript
i18n: {
  langDir: 'locales',  // 会自动查找 i18n/locales/
  // ...
}
```

## 路由配置

所有路由已正确配置：

### Nuxt 主站路由

- `/` - 首页
- `/about` - 关于页面
- `/donors` - 捐赠者页面
- `/privacy` - 隐私政策
- `/terms` - 服务条款
- `/blog` - 重定向到 `/blog/`
- `/docs` - 重定向到 `/docs/`

### 多语言路由

使用 `prefix_except_default` 策略：

- 英语（默认）：`/about`
- 其他语言：`/fr/about`, `/es/about`, `/zh/about`, `/ja/about`, `/ko/about`

### 博客路由

访问 `http://localhost:4567` 后：

- `/` - 博客首页
- `/archives/` - 归档页面
- `/2026/01/22/hello-world/` - 文章页面

### 文档路由

访问 `http://localhost:5678` 后：

- `/` - 文档首页
- `/markdown-examples.html` - Markdown 示例
- `/api-examples.html` - API 示例

## 构建说明

构建命令保持不变：

```bash
npm run build
```

构建会生成：

```
dist/
├── index.html           # Nuxt 主站
├── _nuxt/              # Nuxt 资源
├── blog/               # Hexo 博客
│   └── index.html
└── docs/               # VitePress 文档
    └── index.html
```

## 调试技巧

### 1. 清理缓存

如果遇到问题，清理所有缓存：

```bash
# 清理 Nuxt 缓存
cd apps/site-nuxt && rm -rf .nuxt node_modules/.cache

# 清理 VitePress 缓存
cd apps/docs-vitepress && rm -rf docs/.vitepress/cache

# 清理 Hexo 数据库
cd apps/blog-hexo && rm -rf db.json public
```

### 2. 重新安装依赖

```bash
npm run clean
npm run install:all
```

### 3. 查看日志

```bash
# 查看所有服务日志
npm run dev

# 单独查看某个服务的详细日志
cd apps/site-nuxt && npm run dev
```

### 4. 端口被占用

如果端口被占用，可以找到并终止进程：

```bash
# macOS/Linux
lsof -ti:3456 | xargs kill -9
lsof -ti:4567 | xargs kill -9
lsof -ti:5678 | xargs kill -9
```

## 常见问题

### Q: npm run dev 启动失败？

A: 确保已安装 npm-run-all：

```bash
npm install --save-dev npm-run-all
```

### Q: i18n 文件找不到？

A: 确保文件在 `apps/site-nuxt/i18n/locales/` 目录下。

### Q: 构建失败？

A: 先清理缓存，然后重新构建：

```bash
cd apps/site-nuxt && rm -rf .nuxt
cd ../.. && npm run build
```

### Q: 热重载不工作？

A: 重启开发服务器，确保端口没有被占用。

## 生产环境

生产环境的URL配置（GitHub Pages/Cloudflare Pages）：

- 主站: https://amber-moe.io
- 博客: https://amber-moe.io/blog
- 文档: https://amber-moe.io/docs

端口配置仅影响本地开发环境，不影响生产环境部署。
