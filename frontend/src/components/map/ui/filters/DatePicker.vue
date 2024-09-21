<script>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: "DatePicker",
  components: {VueDatePicker},
  props: {
    placeholder: String
  },
  data(){
    return {
      date: ''
    }
  }
}
</script>

<template>
  <vue-date-picker
      class="indicators"
      :v-model="date"
      :value="date"
      :placeholder="placeholder"
  />
</template>

<style>
.dp__input {
  background-color: #F2F2F2 !important;
  border: none !important;
  height: 48px !important;
  border-radius: 1000px;
  padding-left: 45px !important;
}

.dp__input::placeholder {
  color: #161616;
}

.dp__input_wrap svg {
  width: 24px !important;
  height: 24px !important;
  fill: #6B6B6B;
}
</style>