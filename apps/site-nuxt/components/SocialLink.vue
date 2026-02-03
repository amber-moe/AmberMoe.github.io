<template>
  <a
    :href="url"
    target="_blank"
    rel="noopener noreferrer"
    class="flex flex-col items-center justify-center p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 hover:scale-105 transform"
  >
    <UIcon :name="icon" class="w-8 h-8 text-primary mb-2" />
    <span class="text-sm font-medium text-gray-900 dark:text-white">{{
      name
    }}</span>
  </a>
</template>

<script setup lang="ts">
defineProps<{
  name: string;
  url: string;
  icon: string;
}>();
</script>
