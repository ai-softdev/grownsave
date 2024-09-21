<script>
export default {
  name: "Title",
  props: {
    title: String
  }
}
</script>

<template>
  <h5
      v-html="$t(title)"
      class="text-[36px] max_sm:text-[26px] font-bold"
  >
  </h5>
</template>

<style scoped>

</style>