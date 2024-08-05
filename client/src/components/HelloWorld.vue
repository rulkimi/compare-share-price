<!-- App.vue -->
<script>
  import msftData from "./assets/msft2020.json";
  export default {
    data() {
      var dps1 = [], dps2 = [];
      msftData.forEach(data => {
        dps1.push({ x: new Date(data["date"]), y: [data["open"], data["high"], data["low"], data["close"]] });
        dps2.push({ x: new Date(data["date"]), y: data["close"] });
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
            data: [{
              type: "candlestick",
              name: "Price (in USD)",
              yValueFormatString: "$#,###.##",
              dataPoints: dps1
            }]
          }],
          navigator: {
            data: [{
              dataPoints: dps2
            }],
            slider: {
              minimum: new Date(2020, 1, 1),
              maximum: new Date(2020, 11, 1)
            }
          }
        },
        styleOptions: {
          width: "100%",
          height: "460px"
        }
      }
    }
  }
</script>
<template>
  <CanvasJSStockChart :options="options" :style="styleOptions" />
</template>      