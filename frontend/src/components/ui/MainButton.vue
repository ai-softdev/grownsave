<script>
export default {
  name: "MainButton",
  props: {
    disabled: Boolean
  }
}
</script>

<template>
  <button
      class="font-bold bg-forest text-white w-full py-3 rounded-lg mt-[16px] hover:bg-opacity-90 transition-all ease-in-out duration-300"
      :disabled="disabled"
  >
    <slot></slot>
  </button>
</template>

<style scoped>

</style>