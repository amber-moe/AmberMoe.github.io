<template>
  <section class="py-12 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1
          class="text-3xl sm:text-4xl md:text-5xl font-black text-gray-900 dark:text-white mb-4"
        >
          {{ $t("download.title") }}
        </h1>
        <p class="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
          {{ $t("download.description") }}
        </p>
      </div>

      <!-- Download Cards Grid -->
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8"
      >
        <!-- Card 1: Wallpapers -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-vtuber-pink to-vtuber-blue flex items-center justify-center"
          >
            <Icon name="heroicons:photo" class="w-16 h-16 text-white/80" />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.wallpapers.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.wallpapers.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.wallpapers.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>

        <!-- Card 2: Fan Kit -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-vtuber-blue to-vtuber-purple flex items-center justify-center"
          >
            <Icon
              name="heroicons:paint-brush"
              class="w-16 h-16 text-white/80"
            />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.fankit.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.fankit.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.fankit.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>

        <!-- Card 3: BGM / Music -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-vtuber-purple to-vtuber-pink flex items-center justify-center"
          >
            <Icon
              name="heroicons:musical-note"
              class="w-16 h-16 text-white/80"
            />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.music.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.music.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.music.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>

        <!-- Card 4: Stickers / Emotes -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-yellow-400 to-vtuber-pink flex items-center justify-center"
          >
            <Icon name="heroicons:face-smile" class="w-16 h-16 text-white/80" />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.stickers.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.stickers.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.stickers.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>

        <!-- Card 5: Stream Assets -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-green-400 to-vtuber-blue flex items-center justify-center"
          >
            <Icon
              name="heroicons:video-camera"
              class="w-16 h-16 text-white/80"
            />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.streamAssets.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.streamAssets.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.streamAssets.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>

        <!-- Card 6: Brand Guidelines -->
        <div
          class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div
            class="aspect-video bg-gradient-to-br from-gray-600 to-gray-900 flex items-center justify-center"
          >
            <Icon
              name="heroicons:document-text"
              class="w-16 h-16 text-white/80"
            />
          </div>
          <div class="p-6">
            <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">
              {{ $t("download.brandGuide.title") }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
              {{ $t("download.brandGuide.description") }}
            </p>
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-500">
                {{ $t("download.brandGuide.size") }}
              </span>
              <a
                href="#"
                class="inline-flex items-center gap-2 px-4 py-2 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 font-bold text-sm rounded-lg transition-colors duration-200"
              >
                <Icon name="heroicons:arrow-down-tray" class="w-4 h-4" />
                {{ $t("download.button") }}
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Terms Notice -->
      <div class="mt-12 text-center">
        <p class="text-sm text-gray-500 dark:text-gray-400">
          {{ $t("download.terms") }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
useHead({
  title: "Download - Amber Moe",
  meta: [
    {
      name: "description",
      content:
        "Download wallpapers, fan kits, music, and other resources from Amber Moe.",
    },
  ],
});
</script>
