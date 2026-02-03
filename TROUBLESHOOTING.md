# 🔧 故障排查指南

## 常见问题和解决方案

### 1. 依赖安装失败

#### 问题：npm install 失败

```bash
Error: EACCES: permission denied
```

**解决方案：**

```bash
# 清理 npm 缓存
npm cache clean --force

# 删除所有 node_modules
rm -rf node_modules apps/*/node_modules

# 重新安装
npm run install:all
```

#### 问题：版本冲突

```bash
ERESOLVE unable to resolve dependency tree
```

**解决方案：**

```bash
# 使用 --legacy-peer-deps
npm install --legacy-peer-deps

# 或者使用 --force
npm install --force
```

### 2. 开发服务器问题

#### 问题：端口已被占用

```bash
Error: listen EADDRINUSE: address already in use
```

**解决方案：**

```bash
# 查找占用端口的进程
lsof -i :3456  # Nuxt
lsof -i :5678  # VitePress
lsof -i :4567  # Hexo

# 终止进程
kill -9 <PID>

# 或者使用不同的端口
PORT=3457 npm run dev:site
```

#### 问题：Nuxt 热重载不工作

**解决方案：**

```bash
# 删除 .nuxt 缓存
rm -rf apps/site-nuxt/.nuxt

# 重启开发服务器
cd apps/site-nuxt && npm run dev
```

### 3. 构建问题

#### 问题：Nuxt 构建失败

```bash
Error: Cannot find module...
```

**解决方案：**

```bash
# 清理并重新安装依赖
cd apps/site-nuxt
rm -rf node_modules .nuxt .output
npm install
npm run generate
```

#### 问题：VitePress 构建失败

**解决方案：**

```bash
# 清理缓存
cd apps/docs-vitepress
rm -rf node_modules docs/.vitepress/cache docs/.vitepress/dist
npm install
npm run docs:build
```

#### 问题：Hexo 构建失败

**解决方案：**

```bash
# 清理 Hexo 数据库
cd apps/blog-hexo
npx hexo clean
rm -rf db.json public
npm run build
```

### 4. TypeScript 错误

#### 问题：找不到类型定义

**解决方案：**

```bash
# 重新生成 Nuxt 类型
cd apps/site-nuxt
npx nuxi prepare

# 或者删除并重新生成
rm -rf .nuxt
npm run dev  # 会自动生成类型
```

#### 问题：模块解析错误

**解决方案：**
检查 `tsconfig.json` 中的 paths 配置，确保路径正确。

### 5. i18n 问题

#### 问题：翻译不显示

**解决方案：**

1. 检查 `locales/` 目录下的 JSON 文件格式
2. 确认 `nuxt.config.ts` 中的 i18n 配置
3. 重启开发服务器

#### 问题：语言切换不工作

**解决方案：**

```bash
# 清理浏览器 cookies
# 或者在浏览器控制台执行：
document.cookie = 'i18n_redirected=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
```

### 6. NuxtUI 组件问题

#### 问题：组件不显示或样式错误

**解决方案：**

```bash
# 确保 @nuxt/ui 正确安装
cd apps/site-nuxt
npm install @nuxt/ui@latest

# 检查 nuxt.config.ts 中是否包含：
# modules: ['@nuxt/ui']
```

### 7. 路由问题

#### 问题：页面 404

**解决方案：**

1. 检查文件名是否正确（小写，使用短横线）
2. 确保文件在 `pages/` 目录下
3. 重启开发服务器

#### 问题：重定向不工作

**解决方案：**
检查构建输出，确保 `/blog/` 和 `/docs/` 目录存在。

### 8. Git 和部署问题

#### 问题：GitHub Actions 构建失败

**解决方案：**

1. 检查 `.github/workflows/` 文件语法
2. 确保所有依赖都在 `package.json` 中
3. 查看 Actions 日志获取详细错误信息

#### 问题：Cloudflare Pages 部署失败

**解决方案：**

1. 确认已设置正确的 secrets：
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`
2. 检查 Cloudflare Pages 项目名称是否匹配
3. 确认 API Token 有正确的权限

### 9. 性能问题

#### 问题：构建太慢

**解决方案：**

```bash
# 使用 pnpm（更快的包管理器）
npm install -g pnpm
pnpm install

# 或者并行构建
npm run build:site & npm run build:docs & npm run build:blog
wait
```

#### 问题：开发服务器响应慢

**解决方案：**

1. 检查是否有大量的 node_modules
2. 关闭不必要的浏览器扩展
3. 增加 Node.js 内存限制：

```bash
export NODE_OPTIONS="--max-old-space-size=4096"
```

### 10. 清理和重置

#### 完全重置项目

**如果一切都不工作，尝试完全重置：**

```bash
# 回到项目根目录
cd /Volumes/13EjectionPlug/code/AmberMoe.github.io

# 清理所有构建产物和依赖
npm run clean

# 重新安装所有依赖
npm run install:all

# 测试构建
npm run build
```

## 获取帮助

如果以上方法都不能解决问题：

1. 查看错误日志的完整信息
2. 在对应工具的 GitHub Issues 中搜索
3. 查阅官方文档：
   - Nuxt: https://nuxt.com/docs
   - VitePress: https://vitepress.dev
   - Hexo: https://hexo.io/docs

## 日志收集

收集完整的错误日志：

```bash
# Nuxt
cd apps/site-nuxt
npm run dev > nuxt.log 2>&1

# VitePress
cd apps/docs-vitepress
npm run docs:dev > vitepress.log 2>&1

# Hexo
cd apps/blog-hexo
npm run server > hexo.log 2>&1
```

## 诊断检查清单

- [ ] Node.js 版本 >= 20
- [ ] npm 版本最新
- [ ] 所有依赖都已安装
- [ ] 没有端口冲突
- [ ] TypeScript 配置正确
- [ ] Git 状态干净
- [ ] 网络连接正常
- [ ] 磁盘空间充足

祝你好运！🍀
