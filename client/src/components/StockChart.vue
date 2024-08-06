<template>
  <CanvasJSStockChart :options="options" :style="styleOptions" />
</template>

<script setup>
import { computed } from 'vue';
import { toRefs } from 'vue';
import { defineProps } from 'vue';

const props = defineProps({
  msftData: {
    type: Array,
    required: true
  },
  appleData: {
    type: Array,
    required: true
  }
});

const { msftData, appleData } = toRefs(props);

const msftDps = computed(() => 
  msftData.value.map(data => ({
    x: new Date(data["Date"]),
    y: [data["Open"], data["High"], data["Low"], data["Close"]]
  }))
);

const msftDps2 = computed(() => 
  msftData.value.map(data => ({
    x: new Date(data["Date"]),
    y: data["Close"]
  }))
);

const dummyDps = computed(() => 
  appleData.value.map(data => ({
    x: new Date(data["Date"]),
    y: [data["Open"], data["High"], data["Low"], data["Close"]]
  }))
);

const dummyDps2 = computed(() => 
  appleData.value.map(data => ({
    x: new Date(data["Date"]),
    y: data["Close"]
  }))
);

const options = computed(() => ({
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
        dataPoints: msftDps.value
      },
      {
        type: "candlestick",
        name: "Dummy Data Price (in USD)",
        yValueFormatString: "$#,###.##",
        dataPoints: dummyDps.value
      }
    ]
  }],
  navigator: {
    data: [
      {
        type: "line",
        name: "MSFT",
        color: "blue",
        dataPoints: msftDps2.value
      },
      {
        type: "line",
        name: "Dummy Data",
        color: "red",
        dataPoints: dummyDps2.value
      }
    ],
    slider: {
      minimum: new Date(2020, 0, 1),
      maximum: new Date(2020, 11, 1)
    }
  }
}));

const styleOptions = {
  width: "100%",
  height: "460px"
};
</script>
