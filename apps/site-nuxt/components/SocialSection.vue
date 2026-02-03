<template>
  <section class="py-16 px-6">
    <UContainer>
      <div class="max-w-4xl mx-auto">
        <h2
          class="text-4xl font-bold text-center text-gray-900 dark:text-white mb-12"
        >
          {{ $t("social.title") }}
        </h2>
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6">
          <SocialLink
            v-for="social in socialLinks"
            :key="social.name"
            :name="social.name"
            :url="social.url"
            :icon="social.icon"
          />
        </div>
      </div>
    </UContainer>
  </section>
</template>

<script setup lang="ts">
const socialLinks = [
  {
    name: "Twitter",
    url: "https://twitter.com/AmberMoeVT",
    icon: "i-simple-icons-twitter",
  },
  {
    name: "YouTube",
    url: "https://www.youtube.com/@AmberMoeVT",
    icon: "i-simple-icons-youtube",
  },
  {
    name: "TikTok",
    url: "https://www.tiktok.com/@ambermoevt",
    icon: "i-simple-icons-tiktok",
  },
  {
    name: "Instagram",
    url: "https://www.instagram.com/ambermoevt/",
    icon: "i-simple-icons-instagram",
  },
  {
    name: "Facebook",
    url: "https://www.facebook.com/AmberMoeVT/",
    icon: "i-simple-icons-facebook",
  },
  {
    name: "Reddit",
    url: "https://www.reddit.com/user/AmberMoeVT/",
    icon: "i-simple-icons-reddit",
  },
  {
    name: "Discord",
    url: "https://discord.gg/ambermoevt/",
    icon: "i-simple-icons-discord",
  },
  {
    name: "Twitch",
    url: "https://www.twitch.tv/ambermoevt/",
    icon: "i-simple-icons-twitch",
  },
  {
    name: "GitHub",
    url: "https://github.com/AmberMoeVT/",
    icon: "i-simple-icons-github",
  },
  {
    name: "LinkedIn",
    url: "https://www.linkedin.com/in/ambermoevt/",
    icon: "i-simple-icons-linkedin",
  },
];
</script>
