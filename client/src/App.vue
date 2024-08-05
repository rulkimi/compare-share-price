<!-- App.vue -->
<template>
  <CanvasJSStockChart :options="options" :style="styleOptions" />
</template>

<script>
import msftData from "./assets/msft2020.json";
import dummyData from './assets/randomised.json';

export default {
  data() {
    const msftDps = [];
    const dummyDps = [];

    msftData.forEach(data => {
      msftDps.push({ x: new Date(data["date"]), y: data["close"] });
    });

    dummyData.forEach(data => {
      dummyDps.push({ x: new Date(data["date"]), y: data["close"] });
    });

    return {
      chart: null,
      options: {
        exportEnabled: true,
        theme: "light2",
        title: {
          text: "Vue.js StockChart with Date-Time Axis"
        },
        subtitles: [{
          text: "MSFT and Dummy Data Stock Prices"
        }],
        charts: [{
          axisY: {
            title: "Price",
            prefix: "$",
            tickLength: 0
          },
          data: [
            {
              type: "line",
              name: "MSFT Close Price",
              yValueFormatString: "$#,###.##",
              dataPoints: msftDps,
              lineColor: "#4F81BC" // Set color for MSFT line
            },
            {
              type: "line",
              name: "Dummy Data Close Price",
              yValueFormatString: "$#,###.##",
              dataPoints: dummyDps,
              lineColor: "#C0504E" // Set color for Dummy Data line
            }
          ]
        }],
        navigator: {
          data: [{
            dataPoints: [...msftDps, ...dummyDps]
          }],
          slider: {
            minimum: new Date(2020, 0, 1),
            maximum: new Date(2020, 11, 1)
          }
        }
      },
      styleOptions: {
        width: "100%",
        height: "460px"
      }
    };
  }
}
</script>
