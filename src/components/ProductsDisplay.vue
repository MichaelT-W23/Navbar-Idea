<template>
  <div 
    class="products-display" 
    @mouseenter="handleMouseEnter" 
    @mouseleave="handleMouseLeave"
  >
    <!-- Content of the rectangle -->
    <div class="products-container">
      <p>Product Category 1</p>
      <p>Product Category 2</p>
      <p>Product Category 3</p>
    </div>
  </div>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['mouseenter', 'mouseleave']);

const handleMouseEnter = () => {
  emit('mouseenter');
};

const handleMouseLeave = () => {
  emit('mouseleave');
};
</script>

<style scoped>
.products-display {
  position: absolute;
  top: 110px; /* Adjust based on your navbar height */
  left: 0;
  width: 100%;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 15;
  padding: 20px;
}

.products-container {
  display: flex;
  justify-content: space-around;
  color: #333;
  font-family: Arial, sans-serif;
  font-size: 16px;
}
</style>
