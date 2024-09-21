<script>
export default {
  name: "TypesFilter",
  props: {
    analyzes: Array,
    activeAnalyze: Object,
    showAnalyzes: Boolean,
    activeFilter: Object,
  },
  methods: {
    changeActiveAnalyzes(item){
      this.$emit("changeActiveAnalyzes", item)
    },
    changeShowAnalyzes(){
      this.$emit("changeShowAnalyzes")
    }
  }
}
</script>

<template>
  <div class="relative">
    <div @click="changeShowAnalyzes"
         class="filters bg-romance cursor-pointer rounded-full py-3 px-4 max-w-[285px] min-w-[285px] w-full flex items-center justify-between max_lg:ml-auto">
      <div class="flex items-center gap-2.5">
        <p class="text-doveGrey">
          {{ activeAnalyze.name || 'Фильтры' }}
        </p>
      </div>
      <img
          class="transition-all ease-in-out duration-300"
          :class="{'rotate-180': showAnalyzes}"
          src="/img/arrow.svg" alt="arrow"
      >
    </div>
    <Transition name="left-fade">
      <ul
          v-if="showAnalyzes"
          class="filters-list absolute shadow-filter w-[285px] h-[285px] overflow-y-auto top-12 right-2 max_lg:top-12 rounded-[17px] px-5 bg-white z-[1000]"
      >
        <li
            v-for="item in analyzes"
            class="py-5 border-b last:border-none cursor-pointer hover:text-forest transition-all duration-300 ease-in-out"
            :class="{'text-forest': activeFilter.name === item.name}"
            @click="changeActiveAnalyzes(item)"
        >
          {{ item.name }}
        </li>
      </ul>
    </Transition>
  </div>
</template>

<style scoped>

</style>