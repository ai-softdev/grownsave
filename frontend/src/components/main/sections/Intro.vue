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
        <h1 class="font-bold text-white leading-[130%] text-[48px] max_sm:text-[38px]" v-html="$t('Grow\'n Save — is your digital assistant in agronomy.')">
        </h1>
        <MainSubtitle
            class="w-[490px] max_md:mx-auto"
        >
          {{
          $t('Optimize your farm with more accurate data and recommendations. Increase yields and reduce costs with the help of agricultural technologies.')
          }}
        </MainSubtitle>
        <a href="#map">
          <MainButton
              class="mt-[32px] !rounded-[100px] !w-fit !px-4"
          >
            {{ $t('To the interactive map') }}
          </MainButton>
        </a>
      </div>
    </div>
    <img class="absolute object-cover top-0 right-0 left-0 bottom-0 w-full h-full" src="/img/intro-bg.webp" alt="intro-bg"/>
  </section>
</template>

<style scoped>

</style>