# Amber Moe - Official Website

Your go-to destination for all things tech, creativity, and innovation!

## 🎯 Project Overview

This is a monorepo project consisting of three parts:

- **Nuxt Site** - Main website and landing page
- **Hexo Blog** - Technical blog
- **VitePress Docs** - Technical documentation

## 🚀 Tech Stack

- **Frontend Framework**: Nuxt 4 (TypeScript)
- **UI Framework**: NuxtUI
- **Blog System**: Hexo
- **Documentation**: VitePress
- **CI/CD**: GitHub Actions / Cloudflare Pages
- **i18n**: English (default), French, Spanish, Chinese, Japanese, Korean
- **Theme**: Light/Dark mode support (default: light)

## 📁 Project Structure

```
repo/
├─ apps/
│  ├─ site-nuxt/         # Main website (Nuxt)
│  ├─ docs-vitepress/    # Documentation (VitePress)
│  └─ blog-hexo/         # Blog (Hexo)
├─ dist/                 # Build output directory
├─ assets/               # Shared assets and backup files
├─ .github/workflows/    # CI/CD configurations
├─ build.sh             # Build script
└─ package.json         # Root package.json
```

## 🛠️ Development

### Prerequisites

- Node.js 20+
- npm

### Installation

```bash
# Install all dependencies
npm run install:all
```

### Development Servers

```bash
# Run all services simultaneously
npm run dev

# Or run individually:

# Run Nuxt site (port 3456)
npm run dev:site

# Run VitePress docs (port 5678)
npm run dev:docs

# Run Hexo blog (port 4567)
npm run dev:blog
```

### Build

```bash
# Build all projects
npm run build

# Build individual projects
npm run build:site
npm run build:docs
npm run build:blog
```

## 📦 Deployment

The project is configured for automatic deployment via:

- **GitHub Pages** - Deployed from `main` branch
- **Cloudflare Pages** - Deployed from `main` branch

### Cloudflare Pages Setup

1. Set up the following secrets in your GitHub repository:
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`

2. Configure Cloudflare Pages project:
   - Project name: `amber-moe-io-website`
   - Build command: (handled by GitHub Actions)
   - Build output directory: `dist`

## 🌐 URLs

- Main Site: https://amber-moe.io
- Blog: https://amber-moe.io/blog
- Docs: https://amber-moe.io/docs

## 🔗 Social Media

- Twitter: [@AmberMoeVT](https://twitter.com/AmberMoeVT)
- YouTube: [@AmberMoeVT](https://www.youtube.com/@AmberMoeVT)
- GitHub: [@AmberMoeVT](https://github.com/AmberMoeVT)
- Discord: [Join Server](https://discord.gg/ambermoevt/)

## 📝 License

MIT License - Copyright © 2026 Amber Moe

## 🙏 Support

If you enjoy my content, consider [buying me a coffee](https://www.buymeacoffee.com/ambermoe)!
