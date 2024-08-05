<!-- App.vue -->
<template>
  <CanvasJSStockChart :options="options" :style="styleOptions" />
</template>

<script>
import msftData from "../assets/msft2020.json";
import dummyData from '../assets/randomised.json';

export default {
  data() {
    const msftDps = [];
    const dummyDps = [];

    msftData.forEach(data => {
      msftDps.push({ x: new Date(data["date"]), y: [data["open"], data["high"], data["low"], data["close"]] });
    });

    dummyData.forEach(data => {
      dummyDps.push({ x: new Date(data["date"]), y: [data["open"], data["high"], data["low"], data["close"]] });
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
          text: "MSFT Stock Price"
        }],
        charts: [{
          axisY: {
            title: "Price",
            prefix: "$",
            tickLength: 0
          },
          data: [
            {
              type: "candlestick",
              name: "MSFT Price (in USD)",
              yValueFormatString: "$#,###.##",
              dataPoints: msftDps
            },
            {
              type: "candlestick",
              name: "Dummy Data Price (in USD)",
              yValueFormatString: "$#,###.##",
              dataPoints: dummyDps
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
