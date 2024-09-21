<script>
export default {
  name: "ChangeLang",
  props: {
    showLang: Boolean,
    languages: Array,
    activeLanguage: Object
  },
  methods: {
    changeShowLang() {
      this.$emit("changeShowLang")
    },
    changeLanguage(language) {
      this.$emit("changeLanguage", language)
    }
  }
}
</script>

<template>
  <div class="relative">
    <button @click="changeShowLang" class="flex items-center text-white gap-2">
      <p>{{ $t(activeLanguage.short) }}</p>
      <img
          :class="{'rotate-180': showLang, 'rotate-0': !showLang}"
          class="transition-all ease-in-out duration-300"
          src="/img/light-bottom.svg" alt="bottom"
      >
    </button>
    <transition name="fade">
      <div v-if="showLang" ref="langRef"
           class="absolute top-10 rounded-lg bg-white shadow w-[200px] max_sm:w-[250px] flex flex-col items-start overflow-hidden">
        <button v-for="language in languages" :key="language.short"
                :class="{'bg-forest text-white hover:!bg-forest': language.short === activeLanguage.short,
                         'hover:bg-romance transition-all ease-in-out duration-300': language.short !== activeLanguage.short}"
                class="w-full text-start py-1 px-3"
                @click="changeLanguage(language)">
          {{ $t(language.name) }}
        </button>
      </div>
    </transition>
  </div>
</template>

<style scoped>

</style>