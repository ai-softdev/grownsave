<script>
export default {
  name: "Info",
  data(){
    return {
      value: 0
    }
  },
  props: {
    name: String,
    actual: Number,
    monthly: Number,
    fill: String,
    classColor: String
  },
  methods: {
    formatNumber(value) {
      if (!Number.isFinite(value)) return value;

      const fixedValue = Number.isInteger(value) ? value : value.toFixed(2);

      const [integerPart, decimalPart] = fixedValue.toLocaleString('ru-RU').split(',');

      if (!decimalPart) {
        return integerPart;
      }

      return `${integerPart}.${decimalPart}`;
    },
    getColorClass() {
      let color;
      if (this.value <= 25) color = '#FF0000';
      else if (this.value <= 60) color = '#FFDE30';
      else color = '#509948'

      return {
        'text-[#FF0000]': color === '#FF0000',
        'text-[#FFDE30]': color === '#FFDE30',
        'text-[#509948]': color === '#509948',
      };
    },
    getColor(){
      if (this.value <= 25) return '#FF0000';
      else if (this.value <= 60) return '#FFDE30';
      else return '#509948'
    }
  },
  mounted() {
    this.value = Number(this.monthly !== 0 ? this.formatNumber((this.actual * 100) / this.monthly) : 0)
  }
}
</script>

<template>
  <div>
    <div class="flex items-center gap-2 mb-6 mt-4">
      <svg class="shrink-0" width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M9.99999 13.8333V10.5M9.99999 7.16666H10.0083M18.3333 10.5C18.3333 15.1023 14.6023 18.8333 9.99999 18.8333C5.39761 18.8333 1.66666 15.1023 1.66666 10.5C1.66666 5.89761 5.39761 2.16666 9.99999 2.16666C14.6023 2.16666 18.3333 5.89761 18.3333 10.5Z" :stroke="fill || getColor()" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <p class="font-medium text-lg">
        {{ name }}
      </p>
    </div>
    <div class="flex items-center gap-2 justify-between border-b pb-5">
      <p>Амалда:</p>
      <p class="font-bold" :class="fill ? classColor : getColorClass()">{{ formatNumber(actual) }}</p>
    </div>
    <div class="flex items-center gap-2 justify-between border-b py-5">
      <p>Режада:</p>
      <p class="font-bold" :class="fill ? classColor : getColorClass()">{{ formatNumber(monthly) }}</p>
    </div>
    <div class="flex items-center gap-2 justify-between border-b py-5">
      <p>Фоиз нисбати:</p>
      <p class="font-bold" :class="fill ? classColor : getColorClass()">{{ monthly !== 0 ? formatNumber((actual * 100) / monthly) : 0 }} %</p>
    </div>
  </div>
</template>

<style scoped>

</style>