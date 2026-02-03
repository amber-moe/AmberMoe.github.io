import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Amber Moe Docs",
  description:
    "Technical documentation by Amber Moe - Database, VR, XR, and more",
  base: "/docs/",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/assets/apple-touch-icon.png",

    nav: [
      { text: "官网", link: "https://amber-moe.io/" },
      { text: "Home", link: "/" },
      { text: "Database", link: "/database/" },
      { text: "VR/XR", link: "/vrxr/" },
      { text: "Tutorials", link: "/tutorials/" },
    ],

    sidebar: {
      "/": [
        {
          text: "Getting Started",
          items: [
            { text: "Introduction", link: "/" },
            { text: "Markdown Examples", link: "/markdown-examples" },
            { text: "API Examples", link: "/api-examples" },
          ],
        },
        {
          text: "Database",
          collapsed: false,
          items: [
            { text: "Introduction", link: "/database/" },
            { text: "Getting Started", link: "/database/getting-started" },
          ],
        },
        {
          text: "VR/XR",
          collapsed: false,
          items: [
            { text: "Introduction", link: "/vrxr/" },
            { text: "Getting Started", link: "/vrxr/getting-started" },
          ],
        },
        {
          text: "Tutorials",
          collapsed: false,
          items: [{ text: "Index", link: "/tutorials/" }],
        },
      ],
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/AmberMoeVT" },
      { icon: "twitter", link: "https://twitter.com/AmberMoeVT" },
      { icon: "youtube", link: "https://www.youtube.com/@AmberMoeVT" },
    ],

    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2026 Amber Moe",
    },

    // Enable search
    search: {
      provider: "local",
    },

    // Outline settings
    outline: {
      level: [2, 3],
      label: "On this page",
    },

    // Edit link
    editLink: {
      pattern:
        "https://github.com/Amber1990Zhang/amber-moe-docs/edit/main/docs/:path",
      text: "Edit this page on GitHub",
    },
  },
});
