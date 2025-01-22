<template>
  <transition name="slide">
    <div class="side-view-container">
      <button class="close-btn" @click="emitClose">Close</button>
      <p>Profile Side View</p>
    </div>
  </transition>
</template>


<script setup>
const emit = defineEmits(['close']);

const emitClose = () => {
  emit('close');
};

</script>


<style scoped>
.side-view-container {
  position: fixed;
  top: 110px;
  right: 0;
  width: 400px;
  height: calc(100% - 110px);
  background-color: #fff;
  box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  overflow-y: auto;
  z-index: 999;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: purple;
  color: #fff;
  border: none;
  border-radius: 3px;
  padding: 0.5rem;
  cursor: pointer;
  font-size: 14px;
}

.close-btn:hover {
  background-color: #a005a0;
}

.slide-enter-active {
  transition: all 0.175s ease-out;
}

.slide-leave-active {
  transition: all 0.4s;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}

</style>
