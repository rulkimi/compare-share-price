<template>
  <CanvasJSStockChart :options="options" :style="styleOptions" />
</template>

<script setup>
import { computed } from 'vue';
import { toRefs } from 'vue';

const props = defineProps({
  stockData: {
    type: Array,
    required: true
  }
});

const { stockData } = toRefs(props);

const getDataPoints = (data, type) => 
  data.map(item => ({
    x: new Date(item["Date"]),
    y: type === "candlestick" ? [item["Open"], item["High"], item["Low"], item["Close"]] : item["Close"]
  }));

const options = computed(() => {
  const chartData = [];
  const navigatorData = [];

  stockData.value.forEach((data, index) => {
    const datasetName = `Dataset ${index + 1}`;
    chartData.push({
      type: "candlestick",
      name: `${datasetName} Price (in USD)`,
      yValueFormatString: "$#,###.##",
      dataPoints: getDataPoints(data, "candlestick")
    });

    navigatorData.push({
      type: "line",
      name: datasetName,
      color: index % 2 === 0 ? "blue" : "red", // Alternate colors
      dataPoints: getDataPoints(data, "line")
    });
  });

  return {
    exportEnabled: true,
    theme: "light1",
    subtitles: [{
      text: "Stock Price"
    }],
    charts: [{
      axisY: {
        title: "Price",
        prefix: "$",
        tickLength: 0
      },
      data: chartData
    }],
    navigator: {
      data: navigatorData,
      slider: {
        minimum: new Date(2020, 0, 1),
        maximum: new Date(2020, 11, 1)
      }
    }
  };
});

const styleOptions = {
  width: "100%",
  height: "700px"
};
</script>
