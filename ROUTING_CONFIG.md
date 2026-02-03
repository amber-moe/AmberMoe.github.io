# 路由配置说明

## 域名和路由结构

### 生产环境

- **主域名**: `https://amber-moe.io`
- **主站**: `https://amber-moe.io/` (Nuxt SSG)
- **博客**: `https://amber-moe.io/blog/` (Hexo)
- **文档**: `https://amber-moe.io/docs/` (VitePress)

### 开发环境端口

- **Nuxt 主站**: `http://localhost:3000`
- **Hexo 博客**: `http://localhost:3001`
- **VitePress 文档**: `http://localhost:3002/docs/`

## 构建输出结构

```
dist/
├── index.html                  # Nuxt 主站首页
├── _nuxt/                      # Nuxt 资源
├── about/                      # 关于页面
├── contact/                    # 联系页面
├── social/                     # 社交媒体页面
├── donors/                     # 捐助者页面
├── privacy/                    # 隐私政策
├── terms/                      # 服务条款
├── 404/                        # 404 页面
├── blog/                       # Hexo 博客
│   ├── index.html
│   ├── archives/
│   ├── tags/
│   └── ...
└── docs/                       # VitePress 文档
    ├── index.html
    ├── assets/
    └── ...
```

## 路由配置详情

### 1. Nuxt 主站配置

- **配置文件**: `apps/site-nuxt/nuxt.config.ts`
- **输出目录**: `apps/site-nuxt/.output/public/`
- **部署路径**: `/` (根路径)
- **域名配置**: `runtimeConfig.public.siteUrl = 'https://amber-moe.io'`

### 2. Hexo 博客配置

- **配置文件**: `apps/blog-hexo/_config.yml`
- **输出目录**: `apps/blog-hexo/public/`
- **部署路径**: `/blog/`
- **关键配置**:
  ```yaml
  url: https://amber-moe.io/blog
  root: /blog/
  ```

### 3. VitePress 文档配置

- **配置文件**: `apps/docs-vitepress/docs/.vitepress/config.mts`
- **输出目录**: `apps/docs-vitepress/docs/.vitepress/dist/`
- **部署路径**: `/docs/`
- **关键配置**:
  ```typescript
  export default defineConfig({
    base: "/docs/",
    // ...
  });
  ```

## 构建流程

1. **清理输出目录**

   ```bash
   rm -rf dist && mkdir -p dist
   ```

2. **构建 Nuxt 主站**

   ```bash
   cd apps/site-nuxt
   npm run generate
   cp -r .output/public/* ../../dist/
   ```

3. **构建 VitePress 文档**

   ```bash
   cd apps/docs-vitepress
   npm run docs:build
   mkdir -p ../../dist/docs
   cp -r docs/.vitepress/dist/* ../../dist/docs/
   ```

4. **构建 Hexo 博客**
   ```bash
   cd apps/blog-hexo
   npm run build
   mkdir -p ../../dist/blog
   cp -r public/* ../../dist/blog/
   ```

## 验证清单

- [x] Nuxt 主站输出到 `dist/` 根目录
- [x] Hexo 博客输出到 `dist/blog/`
- [x] VitePress 文档输出到 `dist/docs/`
- [x] Hexo 配置了 `root: /blog/`
- [x] VitePress 配置了 `base: '/docs/'`
- [x] 所有静态资源路径正确
- [x] 域名配置为 `amber-moe.io`

## 测试方法

### 本地构建测试

```bash
# 1. 构建所有项目
npm run build

# 2. 使用 HTTP 服务器预览
cd dist
npx http-server -p 8080

# 3. 访问以下 URL 验证
# - http://localhost:8080/ (主站)
# - http://localhost:8080/blog/ (博客)
# - http://localhost:8080/docs/ (文档)
```

### 生产部署验证

```bash
# 访问以下 URL
# - https://amber-moe.io/
# - https://amber-moe.io/blog/
# - https://amber-moe.io/docs/
```

## 注意事项

1. **博客链接**: 从主站链接到博客时，使用 `/blog/` 而不是外部链接
2. **文档链接**: 从主站链接到文档时，使用 `/docs/` 而不是外部链接
3. **资源路径**: 确保所有资源使用相对路径或正确的绝对路径
4. **404 处理**: 每个子系统都应该有自己的 404 页面处理
5. **CNAME 文件**: 确保 `CNAME` 文件存在于 `dist/` 根目录

## CI/CD 配置

GitHub Actions 和 Cloudflare Pages 都应该：

1. 使用 `dist/` 作为输出目录
2. 确保 `CNAME` 文件包含 `amber-moe.io`
3. 运行完整的 `npm run build` 命令
