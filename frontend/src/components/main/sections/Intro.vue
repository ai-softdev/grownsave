<script>
import MainButton from "../../ui/MainButton.vue";
import MainSubtitle from "../../ui/MainSubtitle.vue";

export default {
  name: "Intro",
  components: {MainSubtitle, MainButton}
}
</script>

<template>
  <section id="intro" class="relative pt-[235px] pb-20">
    <div class="container relative z-10 flex items-center justify-between max_md:flex-col">
      <div class="w-7/12 max_md:order-2 max_md:w-full max_md:text-center">
        <h1 class="font-bold text-white leading-[130%] text-[48px] max_sm:text-[38px]" v-html="$t('Grow\'n Save — ваш цифровой помощник в агрономии.')">
        </h1>
        <MainSubtitle
            class="w-[490px] max_md:mx-auto"
        >
          Оптимизируйте хозяйство с более точными данными и рекомендациями. Повышайте урожайность и снижайте затраты с помощью агротехнологий
        </MainSubtitle>
        <a href="#map">
          <MainButton
              class="mt-[32px] !rounded-[100px] !w-fit !px-4"
          >
            К интерактивной карте
          </MainButton>
        </a>
      </div>
    </div>
    <img class="absolute object-cover top-0 right-0 left-0 bottom-0 w-full h-full" src="/img/intro-bg.webp" alt="intro-bg"/>
  </section>
</template>

<style scoped>

</style>