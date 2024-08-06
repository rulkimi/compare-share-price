<script setup>
import { ref, onMounted } from 'vue';
import StockChart from './components/StockChart.vue';
import axios from 'axios';

const msftData = ref([]);
const appleData = ref([]);

onMounted(() => {
  getSharePrice('AAPL');
  getSharePrice('MSFT');
});

const getSharePrice = async (tickerCode) => {
  try {
    const response = await axios.get(`http://localhost:8000/share_price/${tickerCode}`, {
      params: {
        start_date: '2020-01-01',
        end_date: '2020-09-02'
      }
    });
    const { data } = response;
    
    if (tickerCode === 'AAPL') {
      appleData.value = data;
    } else if (tickerCode === 'MSFT') {
      msftData.value = data;
    }
  } catch (error) {
    console.error(`Error fetching share price for ${tickerCode}:`, error);
  }
};
</script>

<template>
  <div class="border rounded-lg p-4">
    <StockChart :stock-data="[msftData, appleData]" />
  </div>
</template>
