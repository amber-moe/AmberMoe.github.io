<template>
  <UButton
    :to="to"
    :href="href"
    :target="target"
    :size="size"
    :block="block"
    :disabled="disabled"
    :loading="loading"
    class="inline-flex items-center justify-center gap-2 rounded-full font-bold transition-all duration-200 hover:scale-105 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800 shadow-lg shadow-vtuber-pink/20 px-5 py-2.5"
    :class="[
      size === 'xl' && 'px-8 py-3.5 text-lg',
      size === 'lg' && 'px-6 py-3 text-base',
      size === 'md' && 'px-5 py-2.5 text-sm',
      size === 'sm' && 'px-4 py-2 text-xs',
      block && 'w-full',
    ]"
  >
    <Icon v-if="icon && !trailing" :name="icon" class="w-5 h-5 shrink-0" />
    <span class="whitespace-nowrap"><slot /></span>
    <Icon v-if="icon && trailing" :name="icon" class="w-5 h-5 shrink-0" />
  </UButton>
</template>

<script setup lang="ts">
defineProps<{
  to?: string;
  href?: string;
  target?: string;
  size?: "sm" | "md" | "lg" | "xl";
  icon?: string;
  trailing?: boolean;
  block?: boolean;
  disabled?: boolean;
  loading?: boolean;
}>();
</script>
