<script>
import Title from "../../ui/Title.vue";
import MainSubtitle from "../../ui/MainSubtitle.vue";
import CountryMap from "../../ui/CountryMap.vue";

export default {
  name: "InteractiveMap",
  components: {CountryMap, MainSubtitle, Title}
}
</script>

<template>
  <section id="map" class="py-[90px] bg-forest bg-opacity-10 !mx-4 my-[90px] rounded-[40px]">
    <div class="container rounded-[40px] !py-[80px] flex items-center justify-between gap-[80px]">
      <div class="w-5/12">
        <Title
            title="Узнайте информацию о вашей области"
        />
        <MainSubtitle class="!text-dune">
          Проверьте состояние земли в вашей области: получите данные о природных ресурсах и экологии, чтобы лучше понять её устойчивость и перспективы.
        </MainSubtitle>
      </div>
      <div class="relative z-10 w-full h-[500px] bg-white rounded-[40px] shadow-filter py-10">
        <CountryMap/>
        <div class="bg-[#EBF1E7] absolute bottom-4 right-4 rounded-full px-4 py-2 flex items-center gap-3 font-medium">
          <img src="/img/click.svg" alt="click">
          Кликните на область
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>