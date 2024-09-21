<script>
import i18n from "../../../../locales/index.js";

export default {
  name: "DistricsFilter",
  computed: {
    i18n() {
      return i18n
    }
  },
  props: {
    activeDistrictFilter: Object,
    showDistrictFilter: Boolean,
    districsArray: Array
  },
  methods: {
    changeShowDistrictFilter(){
      this.$emit("changeShowDistrictFilter")
    },
    changeActiveDistrictFilter(item){
      this.$emit("changeActiveDistrictFilter", item)
    },
    setActiveDistrict(id){
      this.$emit("setActiveDistrict", id)
    }
  }
}
</script>

<template>
  <div class="relative">
    <div @click="changeShowDistrictFilter"
         class="districs-filters bg-romance cursor-pointer rounded-full py-3 px-4 max-w-[285px] min-w-[285px] w-full flex items-center justify-between max_lg:ml-auto">
      <div class="flex items-center gap-2.5">
        <img src="/img/districs.svg" alt="disctics">
        <p class="text-doveGrey">
          {{ activeDistrictFilter && activeDistrictFilter.id && activeDistrictFilter.names[$i18n.locale] || 'Все' }}
        </p>
      </div>
      <img
          class="transition-all ease-in-out duration-300"
          :class="{'rotate-180': showDistrictFilter}"
          src="/img/arrow.svg" alt="arrow"
      >
    </div>
    <Transition name="left-fade">
      <ul
          v-if="showDistrictFilter"
          class="districs-filters-list absolute shadow-filter w-[285px] h-[285px] overflow-y-auto top-12 right-2 max_lg:top-12 rounded-[17px] px-5 bg-white z-[1000]"
      >
        <li
            v-for="item in districsArray"
            :key="item.id"
            class="py-5 border-b last:border-none cursor-pointer hover:text-forest transition-all duration-300 ease-in-out"
            :class="{'text-forest': activeDistrictFilter && activeDistrictFilter.id && activeDistrictFilter.names[$i18n.locale] === item.name}"
            @click="changeActiveDistrictFilter(item); setActiveDistrict(item.id)"
        >
          {{ item.names[$i18n.locale] }}
        </li>
      </ul>
    </Transition>
  </div>
</template>

<style scoped>

</style>