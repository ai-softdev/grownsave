<script>
export default {
  name: "Loading"
}
</script>

<template>
  <div class="loading"><slot/>...</div>
</template>

<style scoped>
.loading {
  font-weight: bold;
  display:inline-block;
  font-family: monospace;
  font-size: 20px;
  clip-path: inset(0 3ch 0 0);
  animation: l 1s steps(4) infinite;
}

@keyframes l {
  to {
    clip-path: inset(0 -1ch 0 0)
  }
}
</style>