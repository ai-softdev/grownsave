<template>
  <div>
    <h3 class="font-bold text-xl text-center">
      {{ title }}
    </h3>
    <div
        class="bg-white !rounded-lg overflow-hidden p-6 h-[400px] w-full mt-8"
    >
    <Bar :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import {Bar, Line} from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: 'BarChart',
  props: {
    title: String,
    datasetsList: Object
  },
  components: {
    Line,
    Bar
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
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