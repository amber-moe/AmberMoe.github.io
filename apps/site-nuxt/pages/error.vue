<template>
  <section class="py-16 sm:py-24 md:py-32">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center space-y-6 sm:space-y-8">
        <h1
          class="text-6xl sm:text-7xl md:text-9xl font-bold text-vtuber-pink dark:text-vtuber-pink-light"
        >
          404
        </h1>
        <h2
          class="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-900 dark:text-white"
        >
          Oops! Page Not Found
        </h2>
        <p
          class="text-base sm:text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto px-4"
        >
          The page you're looking for seems to have wandered off into the
          digital void. Don't worry though, I'll help you find your way back!
        </p>
        <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center">
          <a
            href="/"
            class="inline-flex items-center justify-center gap-2 rounded-full px-8 py-3.5 text-lg font-bold transition-transform hover:scale-105 shadow-lg shadow-vtuber-pink/20 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800"
          >
            <Icon name="heroicons:home" class="w-5 h-5 shrink-0" />
            <span>Go Home</span>
          </a>
          <a
            href="/blog/"
            class="inline-flex items-center justify-center gap-2 rounded-full px-8 py-3.5 text-lg font-bold transition-transform hover:scale-105 border-2 border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:border-vtuber-pink hover:text-vtuber-pink-dark"
          >
            <Icon name="heroicons:document-text" class="w-5 h-5 shrink-0" />
            <span>Check Blog</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
useHead({
  title: "404 - Page Not Found",
});
</script>
