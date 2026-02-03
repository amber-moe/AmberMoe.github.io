<template>
  <header
    class="sticky top-0 z-50 backdrop-blur-lg bg-white/80 dark:bg-gray-900/80 border-b border-gray-200/50 dark:border-gray-800/50 shadow-sm"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="group flex items-center gap-2 shrink-0">
          <div
            class="w-10 h-10 bg-vtuber-pink-dark rounded-xl flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300 shadow-lg shadow-vtuber-pink/30 overflow-hidden"
          >
            <img
              src="/assets/apple-touch-icon.png"
              alt="Logo"
              class="w-full h-full object-cover"
            />
          </div>
          <span
            class="text-xl font-black text-vtuber-pink-dark hidden sm:inline"
          >
            amber-moe.io
          </span>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center gap-1">
          <NuxtLink
            to="/"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.home") }}
          </NuxtLink>
          <NuxtLink
            to="/about"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.about") }}
          </NuxtLink>
          <a
            :href="blogUrl"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.blog") }}
          </a>
          <a
            :href="docsUrl"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.docs") }}
          </a>
          <NuxtLink
            to="/social"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.social") }}
          </NuxtLink>
          <NuxtLink
            to="/donors"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.donors") }}
          </NuxtLink>
          <NuxtLink
            to="/download"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.download") }}
          </NuxtLink>
          <NuxtLink
            to="/contact"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.contact") }}
          </NuxtLink>
          <a
            href="https://github.com/Amber1990Zhang"
            target="_blank"
            class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300 hover:text-vtuber-pink-dark dark:hover:text-vtuber-pink hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
          >
            {{ $t("nav.github") }}
          </a>
        </nav>

        <!-- Right Side Controls -->
        <div class="flex items-center gap-2">
          <!-- Language Selector Dropdown -->
          <div class="relative" ref="langDropdownRef">
            <button
              @click="isLangOpen = !isLangOpen"
              class="flex items-center gap-1.5 px-3 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-all duration-200"
            >
              <Icon name="heroicons:language" class="w-5 h-5" />
              <span class="hidden sm:inline">{{ currentLocaleName }}</span>
              <Icon
                name="heroicons:chevron-down"
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': isLangOpen }"
              />
            </button>
            <Transition
              enter-active-class="transition duration-100 ease-out"
              enter-from-class="transform scale-95 opacity-0"
              enter-to-class="transform scale-100 opacity-100"
              leave-active-class="transition duration-75 ease-in"
              leave-from-class="transform scale-100 opacity-100"
              leave-to-class="transform scale-95 opacity-0"
            >
              <div
                v-if="isLangOpen"
                class="absolute right-0 mt-2 w-40 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50"
              >
                <button
                  v-for="loc in availableLocales"
                  :key="loc.code"
                  @click="switchLocale(loc.code)"
                  class="w-full px-4 py-2 text-left text-sm font-medium transition-colors duration-150"
                  :class="
                    locale === loc.code
                      ? 'bg-vtuber-pink-light dark:bg-vtuber-pink-dark/30 text-vtuber-pink-dark dark:text-vtuber-pink-light'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                  "
                >
                  {{ loc.name }}
                </button>
              </div>
            </Transition>
          </div>

          <!-- Theme Toggle -->
          <button
            @click="toggleTheme"
            class="p-2 rounded-lg text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all duration-200"
            :aria-label="
              colorMode.preference === 'dark'
                ? 'Switch to light mode'
                : 'Switch to dark mode'
            "
          >
            <Icon
              v-if="colorMode.preference === 'dark'"
              name="heroicons:moon-solid"
              class="w-5 h-5"
            />
            <Icon v-else name="heroicons:sun-solid" class="w-5 h-5" />
          </button>

          <!-- Mobile Menu Button -->
          <button
            class="lg:hidden p-2 rounded-lg text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all duration-200"
            @click="isMenuOpen = !isMenuOpen"
            aria-label="Toggle menu"
          >
            <Icon
              :name="isMenuOpen ? 'heroicons:x-mark' : 'heroicons:bars-3'"
              class="w-6 h-6"
            />
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <Transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="opacity-0 -translate-y-2"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition duration-150 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-2"
      >
        <div
          v-if="isMenuOpen"
          class="lg:hidden py-4 border-t border-gray-200 dark:border-gray-800"
        >
          <nav class="flex flex-col gap-1">
            <NuxtLink
              to="/"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.home") }}
            </NuxtLink>
            <NuxtLink
              to="/about"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.about") }}
            </NuxtLink>
            <a
              :href="blogUrl"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.blog") }}
            </a>
            <a
              :href="docsUrl"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.docs") }}
            </a>
            <NuxtLink
              to="/social"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.social") }}
            </NuxtLink>
            <NuxtLink
              to="/donors"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.donors") }}
            </NuxtLink>
            <NuxtLink
              to="/download"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.download") }}
            </NuxtLink>
            <NuxtLink
              to="/contact"
              @click="isMenuOpen = false"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.contact") }}
            </NuxtLink>
            <a
              href="https://github.com/Amber1990Zhang"
              target="_blank"
              class="px-4 py-3 text-base font-medium text-gray-900 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg"
            >
              {{ $t("nav.github") }}
            </a>
          </nav>
        </div>
      </Transition>
    </div>
  </header>
</template>

<script setup lang="ts">
const colorMode = useColorMode();
const { locale, locales, setLocale } = useI18n();
const runtimeConfig = useRuntimeConfig();

const isMenuOpen = ref(false);
const isLangOpen = ref(false);
const langDropdownRef = ref<HTMLElement | null>(null);

// Dev mode detection and URLs
const isDev = import.meta.dev;
const blogUrl = computed(() =>
  isDev ? "http://localhost:5175/blog/" : "/blog/",
);
const docsUrl = computed(() =>
  isDev ? "http://localhost:5174/docs/" : "/docs/",
);

const availableLocales = computed(() =>
  locales.value.map((loc) => ({
    code: typeof loc === "string" ? loc : loc.code,
    name: typeof loc === "string" ? loc : loc.name || loc.code,
  })),
);

const currentLocaleName = computed(() => {
  const current = availableLocales.value.find(
    (loc) => loc.code === locale.value,
  );
  return current?.name || locale.value;
});

const switchLocale = async (code: string) => {
  await setLocale(code);
  isLangOpen.value = false;
};

const toggleTheme = () => {
  const newMode = colorMode.preference === "dark" ? "light" : "dark";
  colorMode.preference = newMode;
};

// Close dropdown when clicking outside
const onClickOutside = (event: MouseEvent) => {
  if (
    langDropdownRef.value &&
    !langDropdownRef.value.contains(event.target as Node)
  ) {
    isLangOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", onClickOutside);
});

onUnmounted(() => {
  document.removeEventListener("click", onClickOutside);
});
</script>
