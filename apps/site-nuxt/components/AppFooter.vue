<template>
  <footer
    class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-lg border-t border-gray-200/50 dark:border-gray-800/50"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="py-12 sm:py-16">
        <div
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 sm:gap-12 mb-8 sm:mb-12"
        >
          <!-- Brand -->
          <div class="space-y-4 sm:space-y-6">
            <div class="flex items-center gap-3">
              <div
                class="w-12 h-12 sm:w-14 sm:h-14 bg-vtuber-pink-dark rounded-xl flex items-center justify-center shadow-lg shadow-vtuber-pink/20 overflow-hidden"
              >
                <img
                  src="/assets/apple-touch-icon.png"
                  alt="Logo"
                  class="w-full h-full object-cover"
                />
              </div>
              <div>
                <h3 class="text-lg sm:text-xl font-black text-vtuber-pink-dark">
                  Amber Moe
                </h3>
                <p class="text-xs text-gray-500 dark:text-gray-400">
                  Technical VTuber
                </p>
              </div>
            </div>
            <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
              Exploring the intersection of technology, databases, and virtual
              reality through engaging content.
            </p>
          </div>

          <!-- Social Media -->
          <div>
            <h3
              class="text-sm font-black uppercase tracking-wider text-gray-900 dark:text-white mb-4 sm:mb-6"
            >
              {{ $t("footer.aboutMe") }}
            </h3>
            <ul class="space-y-3 sm:space-y-4">
              <li>
                <a
                  href="https://www.youtube.com/@ambermoe"
                  target="_blank"
                  class="group flex items-center gap-3 text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  <Icon
                    name="heroicons:play-circle"
                    class="w-5 h-5 group-hover:scale-110 transition-transform duration-200"
                  />
                  YouTube
                </a>
              </li>
              <li>
                <a
                  href="https://space.bilibili.com/557737255"
                  target="_blank"
                  class="group flex items-center gap-3 text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  <Icon
                    name="heroicons:play-circle"
                    class="w-5 h-5 group-hover:scale-110 transition-transform duration-200"
                  />
                  Bilibili
                </a>
              </li>
              <li>
                <a
                  href="https://twitter.com/amber_moe66"
                  target="_blank"
                  class="group flex items-center gap-3 text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  <svg
                    viewBox="0 0 24 24"
                    class="w-5 h-5 group-hover:scale-110 transition-transform duration-200"
                    fill="currentColor"
                  >
                    <path
                      d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"
                    />
                  </svg>
                  X (Twitter)
                </a>
              </li>
            </ul>
          </div>

          <!-- Quick Links -->
          <div>
            <h3
              class="text-sm font-black uppercase tracking-wider text-gray-900 dark:text-white mb-4 sm:mb-6"
            >
              Quick Links
            </h3>
            <ul class="space-y-3 sm:space-y-4">
              <li>
                <NuxtLink
                  to="/about"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.about") }}
                </NuxtLink>
              </li>
              <li>
                <a
                  href="/blog/"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.blog") }}
                </a>
              </li>
              <li>
                <a
                  href="/docs/"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.docs") }}
                </a>
              </li>
              <li>
                <NuxtLink
                  to="/donors"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.donors") }}
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/download"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.download") }}
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/contact"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("nav.contact") }}
                </NuxtLink>
              </li>
            </ul>
          </div>

          <!-- Contact & Legal -->
          <div>
            <h3
              class="text-sm font-black uppercase tracking-wider text-gray-900 dark:text-white mb-4 sm:mb-6"
            >
              {{ $t("footer.contactMe") }}
            </h3>
            <ul class="space-y-3 sm:space-y-4 mb-6 sm:mb-8">
              <li>
                <a
                  href="mailto:amber.zhangying@foxmail.com"
                  class="group flex items-start gap-2 text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  <Icon
                    name="heroicons:envelope"
                    class="w-5 h-5 mt-0.5 flex-shrink-0"
                  />
                  <span class="break-all">amber.zhangying@foxmail.com</span>
                </a>
              </li>
            </ul>
            <h3
              class="text-sm font-black uppercase tracking-wider text-gray-900 dark:text-white mb-4 sm:mb-6"
            >
              Legal
            </h3>
            <ul class="space-y-3 sm:space-y-4">
              <li>
                <NuxtLink
                  to="/privacy"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("footer.privacy") }}
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/terms"
                  class="text-sm text-gray-600 dark:text-gray-400 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink transition-colors duration-200"
                >
                  {{ $t("footer.terms") }}
                </NuxtLink>
              </li>
            </ul>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div
          class="pt-6 sm:pt-8 border-t border-gray-200 dark:border-gray-700/50"
        >
          <div
            class="flex flex-col sm:flex-row justify-between items-center gap-4"
          >
            <p
              class="text-sm text-gray-500 dark:text-gray-400 text-center sm:text-left"
            >
              {{ $t("footer.copyright") }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts"></script>
