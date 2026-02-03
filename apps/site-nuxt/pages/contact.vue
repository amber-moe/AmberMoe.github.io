<template>
  <section class="py-12 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl mx-auto">
        <h1
          class="text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6 sm:mb-8"
        >
          Contact Me 📧
        </h1>
        <p
          class="text-base sm:text-lg md:text-xl text-gray-600 dark:text-gray-400 mb-8 sm:mb-12"
        >
          Have a question, collaboration idea, or just want to say hi? I'd love
          to hear from you! Here are the best ways to reach me:
        </p>

        <div class="space-y-4 sm:space-y-6">
          <!-- Email -->
          <UCard>
            <div class="flex items-start gap-3 sm:gap-4">
              <div class="text-2xl sm:text-4xl">📧</div>
              <div class="flex-1">
                <h3
                  class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
                >
                  Email
                </h3>
                <p
                  class="text-sm sm:text-base text-gray-600 dark:text-gray-400 mb-3 sm:mb-4"
                >
                  For business inquiries, collaborations, or general questions
                </p>
                <a
                  href="mailto:amber.zhangying@foxmail.com"
                  class="text-vtuber-pink-dark hover:text-vtuber-pink-darker font-medium"
                >
                  amber.zhangying@foxmail.com
                </a>
              </div>
            </div>
          </UCard>

          <!-- Twitter DM -->
          <UCard>
            <div class="flex items-start gap-3 sm:gap-4">
              <div class="text-2xl sm:text-4xl">💬</div>
              <div class="flex-1">
                <h3
                  class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
                >
                  Twitter DM
                </h3>
                <p
                  class="text-sm sm:text-base text-gray-600 dark:text-gray-400 mb-3 sm:mb-4"
                >
                  Quick messages and community interaction
                </p>
                <UButton
                  to="https://twitter.com/amber_moe66"
                  target="_blank"
                  color="primary"
                >
                  Message on Twitter
                </UButton>
              </div>
            </div>
          </UCard>

          <!-- Discord -->
          <UCard>
            <div class="flex items-start gap-3 sm:gap-4">
              <div class="text-2xl sm:text-4xl">🎮</div>
              <div class="flex-1">
                <h3
                  class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
                >
                  Discord Community
                </h3>
                <p
                  class="text-sm sm:text-base text-gray-600 dark:text-gray-400 mb-3 sm:mb-4"
                >
                  Join our community server for real-time discussions
                </p>
                <UButton
                  to="https://discord.gg/ambermoevt/"
                  target="_blank"
                  color="primary"
                >
                  Join Discord
                </UButton>
              </div>
            </div>
          </UCard>

          <!-- GitHub -->
          <UCard>
            <div class="flex items-start gap-3 sm:gap-4">
              <div class="text-2xl sm:text-4xl">🐙</div>
              <div class="flex-1">
                <h3
                  class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
                >
                  GitHub Issues
                </h3>
                <p
                  class="text-sm sm:text-base text-gray-600 dark:text-gray-400 mb-3 sm:mb-4"
                >
                  For technical questions or project-related discussions
                </p>
                <UButton
                  to="https://github.com/Amber1990Zhang"
                  target="_blank"
                  color="neutral"
                >
                  Visit GitHub
                </UButton>
              </div>
            </div>
          </UCard>
        </div>

        <!-- Response Time Notice -->
        <UAlert
          icon="i-heroicons-information-circle"
          color="info"
          variant="subtle"
          title="Response Time"
          description="I typically respond within 24-48 hours. For urgent matters, please reach out via Twitter DM."
          class="mt-8 sm:mt-12"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
useHead({
  title: "Contact",
  meta: [
    {
      name: "description",
      content:
        "Get in touch with Amber Moe for collaborations, questions, or just to say hi",
    },
  ],
});
</script>
