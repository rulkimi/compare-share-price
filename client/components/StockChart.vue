<template>
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

export default {
  name: 'StockChart',
  components: { Line },
  data() {
    return {
      chartData: {
        labels: Array.from({ length: 1000 }, (_, i) => i + 1),
        datasets: [
          {
            label: 'Series 1',
            data: this.generateRandomData(),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1, // Thinner line
            pointRadius: 0,
            fill: false,
          },
          {
            label: 'Series 2',
            data: this.generateRandomData(),
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1, // Thinner line
            pointRadius: 0,

            fill: false,
          },
          {
            label: 'Series 3',
            data: this.generateRandomData(),
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1, // Thinner line
            pointRadius: 0,

            fill: false,
          },
          {
            label: 'Series 4',
            data: this.generateRandomData(),
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1, // Thinner line
            pointRadius: 0,

            fill: false,
          }
        ]
      },
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            display: true
          },
          title: {
            display: true,
            text: 'Vue.js StockChart with Multiple Series'
          },
          tooltip: {
            mode: 'index',
            intersect: false
          },
        },
        scales: {
          x: {
            type: 'linear',
            position: 'bottom',
            beginAtZero: true,
            title: {
              display: true,
              text: 'Index'
            }
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Value'
            }
          }
        }
      }
    }
  },
  methods: {
    generateRandomData() {
      let y = 1000;
      const dps = [];
      for (let i = 0; i < 1000; i++) {
        y += Math.round(Math.random() * 10 - 5);
        dps.push({ x: i + 1, y: y });
      }
      return dps;
    }
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 450px;
}
</style>
