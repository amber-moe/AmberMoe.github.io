// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },

  modules: ["@nuxt/ui", "@nuxtjs/i18n", "@nuxtjs/color-mode"],

  // SSG mode for static hosting
  ssr: true,

  // Production URL
  runtimeConfig: {
    public: {
      siteUrl: "https://amber-moe.io",
    },
  },

  // Development server configuration
  devServer: {
    port: 5173,
  },

  // DevTools configuration
  devtools: {
    enabled: true,
    vscode: {},
    // Change WebSocket port to avoid conflicts
    timeline: {
      enabled: true,
    },
  },

  // Vite configuration
  vite: {
    server: {
      hmr: {
        port: 24173, // Use a different WebSocket port
      },
    },
  },

  // i18n configuration
  i18n: {
    locales: [
      { code: "en", language: "en-US", name: "English", files: ["en.json"] },
      { code: "fr", language: "fr-FR", name: "Français", files: ["fr.json"] },
      { code: "es", language: "es-ES", name: "Español", files: ["es.json"] },
      { code: "zh", language: "zh-CN", name: "中文", files: ["zh.json"] },
      { code: "ja", language: "ja-JP", name: "日本語", files: ["ja.json"] },
      { code: "ko", language: "ko-KR", name: "한국어", files: ["ko.json"] },
    ],
    defaultLocale: "en",
    langDir: "locales",
    strategy: "prefix_except_default",
    bundle: {
      fullInstall: true,
    },
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: "i18n_redirected",
      redirectOn: "root",
    },
  },

  // Color mode configuration
  colorMode: {
    preference: "system",
    fallback: "light",
    classSuffix: "",
    storageKey: "nuxt-color-mode",
  },

  // CSS configuration
  css: ["~/assets/css/main.css"],

  // App configuration
  app: {
    pageTransition: { name: "page", mode: "out-in" },
    head: {
      title: "Amber Moe - Technical VTuber",
      htmlAttrs: {
        lang: "en",
      },
      link: [
        { rel: "preconnect", href: "https://fonts.googleapis.com" },
        {
          rel: "preconnect",
          href: "https://fonts.gstatic.com",
          crossorigin: "",
        },
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap",
        },
      ],
    },
  },

  // TypeScript configuration
  typescript: {
    strict: true,
    shim: false,
  },

  // Nitro configuration
  nitro: {
    prerender: {
      failOnError: false, // Don't fail on 404 for external routes
      ignore: ["/blog", "/docs"], // Ignore blog/docs routes (handled by Hexo/VitePress)
    },
  },
});
