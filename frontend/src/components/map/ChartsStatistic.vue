<script>
import LinedChart from "./ui/charts/LinedChart.vue";
import PolarChart from "./ui/charts/PolarChart.vue";
import RadarChart from "./ui/charts/RadarChart.vue";
import BarChart from "./ui/charts/BarChart.vue";
import AIButton from "../ui/AIButton.vue";

export default {
  name: "ChartsStatistic",
  components: {AIButton, BarChart, RadarChart, PolarChart, LinedChart},
  props: {
    activeAnalyze: Object
  }
}
</script>

<template>
  <div class="mt-[100px]">
    <div class="flex items-center justify-between">
      <h2 class="text-3xl font-bold">
        Дополнительные данные
      </h2>
      <AIButton class="flex items-center justify-center gap-2 w-3/12">
        <img src="/img/ai.svg" alt="ai-icon">
        Рекомендации от ИИ
      </AIButton>
    </div>
    <div class="mt-[44px] flex flex-col gap-8">
      <div class="rounded-lg p-8 bg-romance">
        <LinedChart
            v-if="activeAnalyze.name"
            :datasets-list="activeAnalyze.datasets"
            :title="activeAnalyze.name"
        />
      </div>
      <div class="rounded-lg p-8 bg-romance">
        <PolarChart
            v-if="activeAnalyze.name"
            :datasets-list="activeAnalyze.polarAnalyzes"
            :title="activeAnalyze.polarAnalyzes.title"
        />
      </div>
      <div class="rounded-lg p-8 bg-romance">
        <BarChart
            v-if="activeAnalyze.name"
            :datasets-list="activeAnalyze.barAnalyzes"
            :title="activeAnalyze.barAnalyzes.title"
        />
      </div>
      <div class="rounded-lg p-8 bg-romance">
        <RadarChart
            v-if="activeAnalyze.name"
            :datasets-list="activeAnalyze.radarAnalyzes"
            :title="activeAnalyze.radarAnalyzes.title"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>