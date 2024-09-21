<template>
  <div>
    <h3 class="font-bold text-xl text-center">
      {{ title }}
    </h3>
    <div
        class="bg-white !rounded-lg overflow-hidden p-6 h-[400px] w-full mt-8"
    >
      <PolarArea
          ref="chart"
          :data="chartData"
          :options="options"
      />
    </div>
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  RadialLinearScale,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js'
import {Line, PolarArea} from "vue-chartjs";

ChartJS.register(RadialLinearScale, ArcElement, Tooltip, Legend)

export default {
  name: 'PolarChart',
  props: {
    title: String,
    datasetsList: Object
  },
  components: {
    Line,
    PolarArea
  },
  data() {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  computed: {
    chartData() {
      return {
        labels: this.datasetsList.labels,
        datasets: this.datasetsList.datasets
      }
    }
  }
}
</script>