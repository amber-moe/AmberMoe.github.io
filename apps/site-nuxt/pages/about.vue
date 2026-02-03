<template>
  <section class="py-12 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl mx-auto">
        <h1
          class="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-6 sm:mb-8"
        >
          About Amber Moe
        </h1>

        <div class="prose dark:prose-invert max-w-none">
          <p
            class="text-base sm:text-lg text-gray-600 dark:text-gray-300 leading-relaxed"
          >
            Welcome! I'm Amber Moe, a Technical VTuber and Writer passionate
            about making technology accessible and exciting for everyone.
          </p>

          <h2
            class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mt-8 mb-4"
          >
            What I Do
          </h2>
          <ul
            class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-2"
          >
            <li>
              Create educational content about databases, VR, and XR
              technologies
            </li>
            <li>Stream coding sessions and tech discussions</li>
            <li>Write technical articles and tutorials</li>
            <li>Build and showcase innovative projects</li>
          </ul>

          <h2
            class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mt-8 mb-4"
          >
            My Expertise
          </h2>
          <ul
            class="list-disc list-inside text-gray-600 dark:text-gray-300 space-y-2"
          >
            <li>Database Systems and Architecture</li>
            <li>Virtual Reality (VR) Development</li>
            <li>Extended Reality (XR) Applications</li>
            <li>Software Engineering Best Practices</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
useHead({
  title: "About - Amber Moe",
  meta: [
    {
      name: "description",
      content: "Learn more about Amber Moe, Technical VTuber and Writer.",
    },
  ],
});
</script>
