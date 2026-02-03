#!/bin/bash

set -e

echo "🚀 Building Amber Moe Website..."

# Clean dist directory
echo "🧹 Cleaning dist directory..."
rm -rf dist
mkdir -p dist

# Copy CNAME file
echo "📋 Copying CNAME..."
cp CNAME dist/

# Build Nuxt site
echo "📦 Building Nuxt site..."
cd apps/site-nuxt
npm run generate
cd ../..

# Validate Nuxt output
if [ ! -f apps/site-nuxt/.output/public/index.html ]; then
	echo "❌ Nuxt output missing: apps/site-nuxt/.output/public/index.html"
	exit 1
fi

# Copy Nuxt output to dist
echo "📋 Copying Nuxt output..."
cp -r apps/site-nuxt/.output/public/* dist/

# Build VitePress docs
echo "📦 Building VitePress docs..."
cd apps/docs-vitepress
npm run docs:build
cd ../..

# Validate VitePress output
if [ ! -f apps/docs-vitepress/docs/.vitepress/dist/index.html ]; then
	echo "❌ VitePress output missing: apps/docs-vitepress/docs/.vitepress/dist/index.html"
	exit 1
fi

# Copy VitePress output to dist/docs
echo "📋 Copying VitePress output..."
mkdir -p dist/docs
cp -r apps/docs-vitepress/docs/.vitepress/dist/* dist/docs/

# Build Hexo blog
echo "📦 Building Hexo blog..."
cd apps/blog-hexo
npm run build
cd ../..

# Validate Hexo output
if [ ! -f apps/blog-hexo/public/index.html ]; then
	echo "❌ Hexo output missing: apps/blog-hexo/public/index.html"
	exit 1
fi

# Copy Hexo output to dist/blog
echo "📋 Copying Hexo output..."
mkdir -p dist/blog
cp -r apps/blog-hexo/public/* dist/blog/

echo "✅ Build completed successfully!"
echo "📁 Output directory: dist/"
echo ""
echo "🌐 Routes:"
echo "   - Main site: /"
echo "   - Blog: /blog/"
echo "   - Docs: /docs/"
