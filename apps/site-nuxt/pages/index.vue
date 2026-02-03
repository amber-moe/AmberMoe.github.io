<template>
  <div class="overflow-x-hidden">
    <!-- Hero Section -->
    <section
      class="relative min-h-[90vh] flex items-center justify-center overflow-hidden pt-20 bg-gray-50 dark:bg-gray-800"
    >
      <!-- Background Elements -->
      <div class="absolute inset-0 z-0">
        <div
          class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] bg-vtuber-pink/20 rounded-full blur-[100px] animate-pulse-slow"
        ></div>
        <div
          class="absolute bottom-[-10%] left-[-10%] w-[600px] h-[600px] bg-vtuber-blue/20 rounded-full blur-[120px] animate-pulse-slow animation-delay-2000"
        ></div>
        <!-- Grid Pattern -->
        <div
          class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20"
        ></div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div class="grid lg:grid-cols-2 gap-8 lg:gap-12 items-center">
          <!-- Text Content -->
          <div class="space-y-6 sm:space-y-8 text-center lg:text-left">
            <div
              class="inline-block px-4 py-2 bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm rounded-full border border-vtuber-pink/30 shadow-sm animate-bounce-slow"
            >
              <span
                class="text-vtuber-pink-dark font-bold tracking-wide text-sm"
                >✨ TECHNICAL VTUBER & WRITER</span
              >
            </div>

            <h1
              class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-black leading-tight tracking-tight text-gray-900 dark:text-white"
            >
              Hello, I'm <br />
              <span class="text-vtuber-pink-dark">
                {{ $t("hero.name") }}
              </span>
            </h1>

            <p
              class="text-base sm:text-lg md:text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto lg:mx-0 leading-relaxed font-medium"
            >
              {{ $t("hero.description") }} <br />
              Exploring
              <span class="text-vtuber-pink-dark font-bold">Database</span>,
              <span class="text-vtuber-pink-dark font-bold">VR</span>, and
              <span class="text-vtuber-pink-dark font-bold">Tech</span>.
            </p>

            <div
              class="flex flex-wrap gap-3 sm:gap-4 justify-center lg:justify-start pt-4"
            >
              <a
                href="https://www.youtube.com/@ambermoe"
                target="_blank"
                class="inline-flex items-center justify-center gap-2 rounded-full px-6 sm:px-8 py-3 font-bold transition-transform hover:scale-105 shadow-lg shadow-vtuber-pink/20 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800"
              >
                <Icon name="heroicons:play-circle" class="w-5 h-5 shrink-0" />
                <span>YouTube</span>
              </a>
              <a
                href="https://space.bilibili.com/557737255"
                target="_blank"
                class="inline-flex items-center justify-center gap-2 rounded-full px-6 sm:px-8 py-3 font-bold transition-transform hover:scale-105 shadow-lg shadow-vtuber-pink/20 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800"
              >
                <Icon name="heroicons:tv" class="w-5 h-5 shrink-0" />
                <span>Bilibili</span>
              </a>
            </div>

            <!-- Stats -->
            <div
              class="grid grid-cols-3 gap-4 sm:gap-6 pt-6 sm:pt-8 pb-5 border-t border-gray-200/50 dark:border-gray-700/50 mt-6 sm:mt-8"
            >
              <div>
                <div
                  class="text-lg sm:text-2xl md:text-3xl font-black text-gray-900 dark:text-white"
                >
                  10K+
                </div>
                <div
                  class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider"
                >
                  Followers
                </div>
              </div>
              <div>
                <div
                  class="text-lg sm:text-2xl md:text-3xl font-black text-gray-900 dark:text-white"
                >
                  500+
                </div>
                <div
                  class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider"
                >
                  Videos
                </div>
              </div>
              <div>
                <div
                  class="text-lg sm:text-2xl md:text-3xl font-black text-gray-900 dark:text-white"
                >
                  1M+
                </div>
                <div
                  class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider"
                >
                  Views
                </div>
              </div>
            </div>
          </div>

          <!-- Hero Image area -->
          <div class="relative hidden lg:block h-[600px] xl:h-[800px]">
            <!-- Abstract background shapes for image -->
            <div
              class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] border-[3px] border-vtuber-pink/20 rounded-full animate-spin-slow"
            ></div>
            <div
              class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] border-[3px] border-vtuber-blue/20 rounded-full animate-reverse-spin-slow"
            ></div>

            <!-- Main Character Image Container -->
            <div class="absolute inset-0 flex items-center justify-center">
              <!-- Main Image - single card with image scaled 120% to fill -->
              <div
                class="relative transition-transform duration-500 hover:-translate-y-4 filter drop-shadow-2xl rounded-3xl overflow-hidden border-4 border-white shadow-2xl"
              >
                <img
                  src="/assets/006-1-2.png"
                  alt="Amber Moe"
                  class="w-auto h-[480px] object-cover scale-120 z-20 relative"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div
        class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce flex flex-col items-center gap-2 opacity-60"
      >
        <span class="text-xs font-bold tracking-widest uppercase text-gray-400"
          >Scroll Down</span
        >
        <Icon name="heroicons:arrow-down" class="w-6 h-6 text-gray-400" />
      </div>
    </section>

    <!-- Hightlight Section -->
    <section class="py-12 sm:py-16 md:py-24 bg-white dark:bg-gray-900 relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center gap-4 mb-8 sm:mb-12 md:mb-16">
          <div class="h-px bg-gray-200 dark:bg-gray-700 flex-1"></div>
          <h2
            class="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-black text-gray-900 dark:text-white uppercase tracking-tight text-center"
          >
            Latest <span class="text-vtuber-pink-dark">Highlights</span>
          </h2>
          <div class="h-px bg-gray-200 dark:bg-gray-700 flex-1"></div>
        </div>

        <div
          class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8 max-w-6xl mx-auto"
        >
          <!-- Card 1 -->
          <div
            class="group relative bg-white dark:bg-gray-800 rounded-2xl sm:rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 hover:shadow-2xl hover:shadow-vtuber-pink/20 transition-all duration-300 flex flex-col h-full transform hover:-translate-y-2"
          >
            <a
              href="https://www.youtube.com/watch?v=XEKJ45QjWME"
              target="_blank"
              class="block aspect-video overflow-hidden relative"
            >
              <div
                class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
              >
                <Icon
                  name="heroicons:play-circle"
                  class="w-16 h-16 text-white"
                />
              </div>
              <img
                src="/assets/image.png"
                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                alt="Thumbnail"
              />
            </a>
            <div class="p-4 sm:p-6 flex flex-col flex-1">
              <div class="flex gap-2 mb-3">
                <span
                  class="px-2 py-1 bg-vtuber-pink-light dark:bg-vtuber-pink-dark/30 text-vtuber-pink-darker dark:text-vtuber-pink-light text-xs font-bold rounded-md"
                  >Music</span
                >
                <span
                  class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 text-xs font-bold rounded-md"
                  >Cover</span
                >
              </div>
              <h3
                class="text-base sm:text-lg md:text-xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-vtuber-pink-dark transition-colors"
              >
                王心凌《爱你》宇宙无敌Amber宝宝版
              </h3>
              <p class="text-gray-500 dark:text-gray-400 text-sm mt-auto">
                Re-imagining a classic with a virtual twist.
              </p>
            </div>
          </div>

          <!-- Card 2 -->
          <div
            class="group relative bg-white dark:bg-gray-800 rounded-2xl sm:rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 hover:shadow-2xl hover:shadow-vtuber-pink/20 transition-all duration-300 flex flex-col h-full transform hover:-translate-y-2"
          >
            <a
              href="https://www.youtube.com/watch?v=-vDpvfqFNLk&t=803s"
              target="_blank"
              class="block aspect-video overflow-hidden relative"
            >
              <div
                class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
              >
                <Icon
                  name="heroicons:play-circle"
                  class="w-16 h-16 text-white"
                />
              </div>
              <img
                src="/assets/image-2.png"
                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                alt="Thumbnail"
              />
            </a>
            <div class="p-4 sm:p-6 flex flex-col flex-1">
              <div class="flex gap-2 mb-3">
                <span
                  class="px-2 py-1 bg-vtuber-pink-light dark:bg-vtuber-pink-dark/30 text-vtuber-pink-darker dark:text-vtuber-pink-light text-xs font-bold rounded-md"
                  >Tech</span
                >
                <span
                  class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 text-xs font-bold rounded-md"
                  >Tutorial</span
                >
              </div>
              <h3
                class="text-base sm:text-lg md:text-xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-vtuber-pink-dark transition-colors"
              >
                Vtuber streaming solutions on Mac M1
              </h3>
              <p class="text-gray-500 dark:text-gray-400 text-sm mt-auto">
                A comprehensive guide for Mac users in the VTuber space.
              </p>
            </div>
          </div>

          <!-- Card 3 -->
          <div
            class="group relative bg-white dark:bg-gray-800 rounded-2xl sm:rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 hover:shadow-2xl hover:shadow-vtuber-pink/20 transition-all duration-300 flex flex-col h-full transform hover:-translate-y-2"
          >
            <a
              href="https://www.youtube.com/watch?v=FyTcSxuQ_2k&t=117s"
              target="_blank"
              class="block aspect-video overflow-hidden relative"
            >
              <div
                class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent z-10 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center"
              >
                <Icon
                  name="heroicons:play-circle"
                  class="w-16 h-16 text-white"
                />
              </div>
              <img
                src="/assets/image-3.png"
                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                alt="Thumbnail"
              />
            </a>
            <div class="p-4 sm:p-6 flex flex-col flex-1">
              <div class="flex gap-2 mb-3">
                <span
                  class="px-2 py-1 bg-vtuber-pink-light dark:bg-vtuber-pink-dark/30 text-vtuber-pink-darker dark:text-vtuber-pink-light text-xs font-bold rounded-md"
                  >Code</span
                >
                <span
                  class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 text-xs font-bold rounded-md"
                  >Docker</span
                >
              </div>
              <h3
                class="text-base sm:text-lg md:text-xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-vtuber-pink-dark transition-colors"
              >
                Apache Flink SQL client on Docker
              </h3>
              <p class="text-gray-500 dark:text-gray-400 text-sm mt-auto">
                Setting up big data tools locally has never been easier.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Social Banner -->
    <section
      class="py-12 sm:py-16 md:py-24 relative overflow-hidden bg-gray-900"
    >
      <div
        class="absolute inset-0 opacity-20 bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"
      ></div>
      <!-- Colored blobs -->
      <div
        class="absolute top-0 right-0 w-[300px] sm:w-[400px] md:w-[500px] h-[300px] sm:h-[400px] md:h-[500px] bg-vtuber-pink rounded-full blur-[120px] opacity-20"
      ></div>
      <div
        class="absolute bottom-0 left-0 w-[300px] sm:w-[400px] md:w-[500px] h-[300px] sm:h-[400px] md:h-[500px] bg-vtuber-pink-dark rounded-full blur-[120px] opacity-20"
      ></div>

      <div
        class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center"
      >
        <div class="max-w-3xl mx-auto space-y-6 sm:space-y-8">
          <div
            class="w-12 h-12 sm:w-16 sm:h-16 mx-auto bg-white dark:bg-gray-800 rounded-xl flex items-center justify-center animate-bounce"
          >
            <svg
              viewBox="0 0 24 24"
              class="w-8 h-8 sm:w-10 sm:h-10 text-gray-900 dark:text-white"
              fill="currentColor"
            >
              <path
                d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"
              />
            </svg>
          </div>
          <h2
            class="text-2xl sm:text-4xl md:text-6xl font-black text-white leading-tight"
          >
            Join the
            <span class="text-vtuber-pink">Conversation</span>
          </h2>
          <p class="text-lg sm:text-xl text-gray-400">
            {{ $t("social.twitterDescription") }}
          </p>
          <a
            href="https://twitter.com/amber_moe66"
            target="_blank"
            class="inline-flex items-center justify-center gap-2 rounded-full px-8 py-4 text-lg font-bold bg-vtuber-pink text-gray-800 hover:bg-vtuber-pink-light transition-all hover:scale-105 shadow-lg shadow-vtuber-pink/30"
          >
            Follow on X
            <Icon name="heroicons:arrow-right" class="w-5 h-5" />
          </a>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section
      class="py-12 sm:py-16 md:py-24 bg-gray-50 dark:bg-gray-800 relative"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-8 sm:gap-12 md:gap-16 items-center">
          <div class="relative group order-2 lg:order-1">
            <div
              class="absolute -inset-2 bg-vtuber-pink-dark rounded-2xl opacity-75 blur-lg group-hover:opacity-100 transition duration-1000 group-hover:duration-200"
            ></div>
            <div
              class="relative bg-white dark:bg-gray-900 rounded-2xl p-4 sm:p-6 md:p-8 border border-gray-100 dark:border-gray-700"
            >
              <div
                class="w-12 h-12 sm:w-16 sm:h-16 bg-vtuber-pink-light dark:bg-vtuber-pink-dark/30 rounded-2xl flex items-center justify-center mb-4 sm:mb-6"
              >
                <Icon
                  name="heroicons:code-bracket-square"
                  class="w-6 h-6 sm:w-8 sm:h-8 text-vtuber-pink-dark"
                />
              </div>
              <h3
                class="text-xl sm:text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-3 sm:mb-4"
              >
                Oceanbase-sql-gpt
              </h3>
              <p
                class="text-sm sm:text-base text-gray-600 dark:text-gray-300 mb-4 sm:mb-6 leading-relaxed"
              >
                An innovative open-source project integrating AI capabilities
                with database management. Helping developers write better SQL
                queries faster.
              </p>
              <div class="flex flex-wrap gap-2 sm:gap-3 mb-6 sm:mb-8">
                <UBadge color="gray" variant="soft">TypeScript</UBadge>
                <UBadge color="gray" variant="soft">AI</UBadge>
                <UBadge color="gray" variant="soft">SQL</UBadge>
              </div>
              <a
                href="https://github.com/Amber1990Zhang/oceanbase-sql-gpt"
                target="_blank"
                class="w-full inline-flex items-center justify-center gap-2 rounded-full px-6 py-3 font-bold transition-transform hover:scale-105 shadow-lg shadow-vtuber-pink/20 bg-vtuber-pink hover:bg-vtuber-pink-light text-gray-800"
              >
                <svg
                  viewBox="0 0 24 24"
                  class="w-5 h-5 shrink-0"
                  fill="currentColor"
                >
                  <path
                    d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                  />
                </svg>
                <span>View Source Code</span>
              </a>
            </div>
          </div>

          <div class="space-y-6 sm:space-y-8 order-1 lg:order-2">
            <h2
              class="text-2xl sm:text-3xl md:text-4xl font-black text-gray-900 dark:text-white"
            >
              Building
              <span class="text-vtuber-pink-dark">Open Source</span> Solutions
            </h2>
            <p
              class="text-base sm:text-lg md:text-xl text-gray-600 dark:text-gray-300 leading-relaxed"
            >
              {{ $t("tools.description") }}
            </p>
            <ul class="space-y-3 sm:space-y-4">
              <li class="flex items-center gap-3">
                <Icon
                  name="heroicons:check-circle"
                  class="w-5 h-5 sm:w-6 sm:h-6 text-vtuber-pink-dark"
                />
                <span
                  class="text-sm sm:text-base md:text-lg font-medium text-gray-700 dark:text-gray-300"
                  >Community Driven Development</span
                >
              </li>
              <li class="flex items-center gap-3">
                <Icon
                  name="heroicons:check-circle"
                  class="w-5 h-5 sm:w-6 sm:h-6 text-vtuber-pink-dark"
                />
                <span
                  class="text-sm sm:text-base md:text-lg font-medium text-gray-700 dark:text-gray-300"
                  >Modern Tech Stack</span
                >
              </li>
              <li class="flex items-center gap-3">
                <Icon
                  name="heroicons:check-circle"
                  class="w-5 h-5 sm:w-6 sm:h-6 text-vtuber-pink-dark"
                />
                <span
                  class="text-sm sm:text-base md:text-lg font-medium text-gray-700 dark:text-gray-300"
                  >Continuous Innovation</span
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonial -->
    <section
      class="py-12 sm:py-16 md:py-24 bg-white dark:bg-gray-900 relative overflow-hidden"
    >
      <div
        class="absolute right-0 top-0 w-1/3 h-full bg-vtuber-pink/5 dark:bg-vtuber-pink/10 skew-x-[-12deg] transform translate-x-32"
      ></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <div
            class="w-20 h-20 sm:w-24 sm:h-24 md:w-28 md:h-28 mx-auto mb-6 sm:mb-8 rounded-full overflow-hidden border-4 border-white dark:border-gray-800 shadow-xl"
          >
            <img
              src="/assets/apple-touch-icon.png"
              alt="Avatar"
              class="w-full h-full object-cover"
            />
          </div>
          <Icon
            name="heroicons:chat-bubble-bottom-center-text"
            class="w-8 h-8 sm:w-10 sm:h-10 md:w-12 md:h-12 text-vtuber-pink/30 mx-auto mb-4 sm:mb-6"
          />
          <blockquote
            class="text-lg sm:text-xl md:text-2xl lg:text-3xl font-bold text-gray-900 dark:text-white italic leading-snug mb-6 sm:mb-8"
          >
            "{{ $t("testimonial.description") }}"
          </blockquote>
          <div
            class="font-black text-vtuber-pink-dark tracking-widest uppercase"
          >
            Amber Moe
          </div>
          <div class="text-sm text-gray-500 dark:text-gray-400 font-bold mt-2">
            Content Creator
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
// No extra js needed for static content
</script>

<style scoped>
/* Custom animations that are specific to this page */
@keyframes float {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(1deg);
  }
  100% {
    transform: translateY(0px) rotate(0deg);
  }
}

.animate-pulse-slow {
  animation: pulse 8s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.animate-spin-slow {
  animation: spin 20s linear infinite;
}

.animate-reverse-spin-slow {
  animation: spin 25s linear infinite reverse;
}

@keyframes spin {
  from {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  to {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
