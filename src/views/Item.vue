<template>
  <div>
    <p>ITEM: {{ itemName }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  itemName: String
});

console.log('itemName:', props.itemName);
</script>

<style scoped>
</style>
