<template>
  <div>
    <h3 class="font-bold text-xl text-center">
      {{ title }}
    </h3>
   <div
       class="bg-white !rounded-lg overflow-hidden p-6 h-[400px] w-full mt-8"
   >
     <Line
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
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import {Line} from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
  name: 'BarChart',
  props: {
    title: String,
    datasetsList: Array
  },
  components: {
    Line
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
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: this.datasetsList
      }
    }
  }
}
</script>