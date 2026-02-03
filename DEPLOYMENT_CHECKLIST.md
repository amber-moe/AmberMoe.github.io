# 🚀 部署前检查清单

## ✅ 已完成项目

### 端口配置

- [x] Nuxt 主站端口：3000
- [x] Hexo 博客端口：3001
- [x] VitePress 文档端口：3002
- [x] HMR WebSocket 端口：24000

### 页面开发

- [x] 首页（完全重构，参考原 HTML）
- [x] 关于页面
- [x] 捐助者页面
- [x] 隐私政策页面
- [x] 服务条款页面
- [x] 社交媒体页面
- [x] 联系页面
- [x] 404 页面

### 路由配置

- [x] 主站路由：`/`
- [x] 博客路由：`/blog/`（Hexo root 配置正确）
- [x] 文档路由：`/docs/`（VitePress base 配置正确）
- [x] CNAME 文件包含域名：`amber-moe.io`

### 域名配置

- [x] Nuxt: `runtimeConfig.public.siteUrl = 'https://amber-moe.io'`
- [x] Hexo: `url: https://amber-moe.io/blog`, `root: /blog/`
- [x] VitePress: `base: '/docs/'`

### 资源文件

- [x] 所有图片复制到 `apps/site-nuxt/public/assets/`
- [x] Favicon 和 Apple Touch Icon
- [x] 视频缩略图
- [x] 头像图片

### 国际化

- [x] 6 种语言配置（英、法、西、中、日、韩）
- [x] 英文翻译完整
- [x] 中文翻译完整
- [x] 其他语言基础翻译

### 构建流程

- [x] `build.sh` 脚本正确
- [x] CNAME 文件复制
- [x] 三个项目构建顺序正确
- [x] 输出目录结构正确

### 测试

- [x] 本地构建测试通过
- [x] 输出目录结构验证
- [x] 开发服务器启动成功
- [x] 无端口冲突

## 📋 部署前最终检查

### 1. GitHub 仓库配置

- [ ] 确保所有代码已推送到 GitHub
- [ ] 检查 `.github/workflows/deploy.yml` 配置
- [ ] 确认 GitHub Pages 设置正确

### 2. Cloudflare Pages 配置

- [ ] 设置环境变量（如需要）
- [ ] 配置构建命令：`npm run build`
- [ ] 配置输出目录：`dist`
- [ ] 添加 `CLOUDFLARE_API_TOKEN` 密钥
- [ ] 添加 `CLOUDFLARE_ACCOUNT_ID` 密钥

### 3. 域名配置

- [ ] DNS 记录指向正确
- [ ] CNAME 文件存在于 `dist/` 根目录
- [ ] SSL 证书配置（Cloudflare 自动提供）

### 4. SEO 优化

- [ ] 每个页面都有正确的 title 和 description
- [ ] 添加 Google Analytics（已在原 HTML 中）
- [ ] 生成 sitemap.xml
- [ ] 添加 robots.txt（已存在）

### 5. 性能优化

- [ ] 图片压缩（如需要）
- [ ] 启用 CDN
- [ ] 配置缓存策略

## 🔍 本地测试步骤

### 1. 开发环境测试

```bash
# 安装所有依赖
npm run install:all

# 启动开发服务器
npm run dev

# 访问以下 URL 并测试所有功能：
# - http://localhost:3000 (主站)
# - http://localhost:3001/blog/ (博客)
# - http://localhost:3002/docs/ (文档)
```

**测试项目**：

- [ ] 导航栏所有链接正常
- [ ] 语言切换功能正常
- [ ] 主题切换功能正常
- [ ] 所有图片正常显示
- [ ] 响应式布局正常
- [ ] 所有页面加载正常

### 2. 生产构建测试

```bash
# 清理并构建
npm run build

# 使用 HTTP 服务器预览
cd dist
npx http-server -p 8080

# 访问以下 URL：
# - http://localhost:8080/ (主站)
# - http://localhost:8080/blog/ (博客)
# - http://localhost:8080/docs/ (文档)
```

**测试项目**：

- [ ] 所有静态资源加载正常
- [ ] 博客路由 `/blog/` 正常工作
- [ ] 文档路由 `/docs/` 正常工作
- [ ] 没有 404 错误
- [ ] 资源路径全部正确

### 3. 多浏览器测试

- [ ] Chrome
- [ ] Safari
- [ ] Firefox
- [ ] Edge
- [ ] 移动端浏览器

### 4. 多设备测试

- [ ] 桌面端（> 1280px）
- [ ] 平板端（768px - 1024px）
- [ ] 移动端（< 768px）

## 🚀 部署命令

### GitHub Pages

```bash
# 推送到 GitHub
git add .
git commit -m "Complete refactoring"
git push origin main

# GitHub Actions 会自动构建和部署
```

### Cloudflare Pages

```bash
# 连接 GitHub 仓库到 Cloudflare Pages
# 或使用 Wrangler CLI：
npx wrangler pages deploy dist
```

### 手动部署

```bash
# 构建
npm run build

# 上传 dist/ 目录到服务器
```

## 📊 监控和维护

### 部署后检查

- [ ] 访问 https://amber-moe.io/ 确认主站正常
- [ ] 访问 https://amber-moe.io/blog/ 确认博客正常
- [ ] 访问 https://amber-moe.io/docs/ 确认文档正常
- [ ] 检查所有页面的 SEO 元数据
- [ ] 测试所有外部链接
- [ ] 验证 SSL 证书

### Google Search Console

- [ ] 提交 sitemap
- [ ] 验证网站所有权
- [ ] 检查索引状态

### 性能监控

- [ ] Google PageSpeed Insights
- [ ] Lighthouse 测试
- [ ] WebPageTest

## 📝 注意事项

1. **首次部署**: 可能需要 10-15 分钟才能全球生效
2. **DNS 传播**: DNS 更改可能需要 24-48 小时
3. **缓存清理**: 部署后清除浏览器缓存进行测试
4. **SSL 证书**: Cloudflare 会自动提供，无需额外配置
5. **构建时间**: 完整构建约需 1-2 分钟

## 🆘 常见问题

### 问题：博客路径 404

**解决**：确认 Hexo `_config.yml` 中 `root: /blog/` 配置正确

### 问题：文档路径 404

**解决**：确认 VitePress `config.mts` 中 `base: '/docs/'` 配置正确

### 问题：图片不显示

**解决**：检查图片路径，确保使用 `/assets/` 而不是相对路径

### 问题：CNAME 文件丢失

**解决**：确认 `build.sh` 中包含 `cp CNAME dist/` 命令

### 问题：端口冲突

**解决**：使用 `lsof -ti:3000,3001,3002 | xargs kill -9` 释放端口

## ✅ 部署完成确认

完成部署后，填写以下信息：

- **部署日期**: ****\_\_\_\_****
- **部署平台**: GitHub Pages / Cloudflare Pages
- **域名**: https://amber-moe.io
- **构建时间**: ****\_\_\_\_****
- **测试结果**: 通过 / 需要修复

---

**祝部署顺利！🎉**
