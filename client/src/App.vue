<script setup>
import { onMounted } from 'vue';
import StockChart from './components/StockChart.vue';
import axios from 'axios';

onMounted(() => {
  getSharePrice();
});

const getSharePrice = async () => {
  try {
    const response = await axios.get(`http://localhost:8000/share_price/AAPL`, {
      params: {
        start_date: '2020-05-02',
        end_date: '2020-05-10'
      }
    });
    const { data } = response;
    console.log(data)
  } catch (error) {

  }
}
</script>

<template>
  <StockChart />
</template>
