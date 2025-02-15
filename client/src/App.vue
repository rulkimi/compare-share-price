<script setup>
import { onMounted, ref } from 'vue';
import StockChart from './components/StockChart.vue';
import axios from 'axios';

const stockData = ref([]);
const codes = ref([]);
const tickerCode = ref('');
const startDate = ref('2024-01-01');
const endDate = ref('2024-06-02');

onMounted(() => {
  tickerCode.value = 'AAPL';
  getSharePrice();
})

const getSharePrice = async () => {
  const code = tickerCode.value.toUpperCase();
  try {
    const response = await axios.get(`http://localhost:8000/share_price/${code}`, {
      params: {
        start_date: startDate.value,
        end_date: endDate.value
      }
    });
    const { data } = response;
    stockData.value.push(data);
    codes.value.push(code);
    tickerCode.value = '';
  } catch (error) {
    console.error(`Error fetching share price for ${code}:`, error);
  }
};

const removeCode = index => {
  codes.value.splice(index, 1);
  stockData.value.splice(index, 1);
}
</script>

<template>
  <div class="grid grid-cols-4 gap-2 h-[40px] mb-4">
    <input
      v-model="tickerCode"
      placeholder="ticker symbol"
      type="text"
      class="border w-full rounded-lg p-2 outline-none col-span-1"
      @keydown.enter="getSharePrice"
    >
    <input v-model="startDate" type="date" class="border w-full rounded-lg p-2 outline-none col-span-1">
    <input v-model="endDate" type="date" class="border w-full rounded-lg p-2 outline-none col-span-1">
    <button
      class="border bg-blue-500 text-white rounded-lg px-3 py-2 col-span-1"
      @click="getSharePrice"
    >+ Add to Chart</button>
  </div>
  <transition-group name="codes" tag="div" class="flex gap-2 relative mb-4">
    <div
      v-for="(code, index) in codes"
      :key="code"
      class="bg-gray-100 px-3 py-2 rounded-lg"
    >
      <div class="flex gap-2">
        {{ code }}
        <img
          class="cursor-pointer transition-transform duration-200 hover:scale-110"
          src="./assets/times.svg"
          alt="remove code"
          width="24"
          @click="removeCode(index)"
        >
      </div>
    </div>
  </transition-group>
  <div v-if="stockData.length" class="border rounded-lg p-4">
    <StockChart :stock-data="stockData" />
  </div>
</template>

<style scoped>
.codes-enter-from, .codes-leave-to {
  opacity: 0;
}
.codes-leave-active, .codes-enter-active, .codes-move {
  transition: all 0.3s ease-in-out;
}
.codes-leave-active {
  position: absolute;
}
</style>
