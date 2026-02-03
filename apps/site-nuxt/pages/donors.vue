<template>
  <section class="py-12 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl mx-auto text-center">
        <h1
          class="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-6 sm:mb-8"
        >
          Support Amber Moe
        </h1>

        <p
          class="text-base sm:text-lg text-gray-600 dark:text-gray-300 mb-6 sm:mb-8"
        >
          Your support helps me create more content and continue sharing
          knowledge with the community!
        </p>

        <a
          href="https://www.buymeacoffee.com/ambermoe"
          target="_blank"
          class="inline-flex items-center justify-center gap-2 rounded-full px-6 py-3 font-bold transition-transform hover:scale-105 shadow-lg shadow-vtuber-pink/20 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800"
        >
          <Icon name="heroicons:heart" class="w-5 h-5 shrink-0" />
          <span>Buy Me a Coffee</span>
        </a>

        <div class="mt-12 sm:mt-16">
          <h2
            class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mb-6 sm:mb-8"
          >
            Thank You to Our Supporters! 💖
          </h2>

          <div
            class="bg-gray-50 dark:bg-gray-800/50 rounded-lg p-6 sm:p-8 border border-gray-200 dark:border-gray-700"
          >
            <p class="text-gray-600 dark:text-gray-400 italic">
              List of donors will appear here once the integration is set up.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
useHead({
  title: "Donors - Amber Moe",
  meta: [
    {
      name: "description",
      content: "Support Amber Moe and see our amazing supporters!",
    },
  ],
});
</script>
