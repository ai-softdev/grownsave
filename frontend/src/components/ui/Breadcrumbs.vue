<script>
export default {
  name: "Breadcrumbs",
  props: {
    content: String,
    breadcrumbItems: {
      type: Array,
      required: true,
      default: () => []
    }
  }
}
</script>

<template>
  <ul class="flex items-center gap-[3px] font-medium">
    <li
        v-for="(item, index) in breadcrumbItems"
        :key="index"
        class="relative flex"
        :class="{
          'pr-2': index !== breadcrumbItems.length - 1,
          'link': item.path
        }"
    >
      <router-link v-if="item.path" :to="item.path" class="pr-2 text-smokey">
        {{ $t(item.label) }}
      </router-link>
      <span v-else class="text-forest cursor-default">
        {{ $t(item.label) }}
      </span>
    </li>
  </ul>
</template>

<style scoped>
.link::after {
 content: "/";
  color: #737373;
}
</style>