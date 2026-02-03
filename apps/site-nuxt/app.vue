<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
useHead({
  titleTemplate: "%s - Amber Moe",
  meta: [
    {
      name: "description",
      content:
        "Amber Moe - Technical VTuber/Writer. Database/VR/XR enthusiast.",
    },
  ],
});
</script>
