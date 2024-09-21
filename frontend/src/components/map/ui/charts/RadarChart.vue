<script>
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js'
import {Bar, Radar} from 'vue-chartjs'

ChartJS.register(
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip,
    Legend
)

export default {
  name: "RadarChart",
  components: {
    Bar,
    Radar
  },
  props: {
    title: String,
    datasetsList: Object
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  computed: {
    chartData(){
      return {
        labels: this.datasetsList.labels,
        datasets: this.datasetsList.datasets
      }
    }
  }
}
</script>

<template>
  <div>
    <h3 class="font-bold text-xl text-center">
      {{ title }}
    </h3>
    <div
        class="bg-white !rounded-lg overflow-hidden p-6 h-[800px] w-full mt-8"
    >
    <Radar :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<style scoped>

</style>