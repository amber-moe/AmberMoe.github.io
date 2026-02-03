<template>
  <div
    class="min-h-screen flex flex-col bg-white dark:bg-gray-900 text-gray-900 dark:text-white transition-colors duration-200"
  >
    <AppHeader />
    <main class="flex-1 w-full">
      <slot />
    </main>
    <AppFooter />
  </div>
</template>
