<script>
export default {
  name: "Tooltip"
}
</script>

<template>
  <div id="tooltip" class="tooltip">
    <p id="district-name" class="font-bold">
      <slot/>
    </p>
  </div>
</template>

<style scoped>

</style>