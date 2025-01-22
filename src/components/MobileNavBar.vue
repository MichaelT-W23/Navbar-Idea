<template>
  <div>
    <nav class="navbar" ref="navbarRef">
      <div class="nav-links nav-left">
        <span
          class="material-symbols-outlined hamburger-icon"
          @click="openSideView('menu')"
        >
          menu
        </span>
      </div>
      <img :src="BlueLogo" alt="Blue Logo" class="logo" />
      <div class="nav-links nav-right">
        <div
          class="material-symbols-outlined profile-icon"
          @click="goToProfileView"
        >
          account_circle
        </div>
        <div
          class="material-symbols-outlined cart-icon"
          @click="goToCartView"
        >
          shopping_cart
        </div>
      </div>
    </nav>
    <div class="content">
      <transition name="slide">
        <MobileSideBar
          v-if="activeSideView === 'menu'"
          @close="closeSideView"
        />
      </transition>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import BlueLogo from '../../images/logos/blue-logo.png';
import MobileSideBar from './MobileSideBar.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const activeSideView = ref(null);

const openSideView = (view) => {
  activeSideView.value = view;
};

const closeSideView = () => {
  activeSideView.value = null;
};

const keysPressed = new Set();

const handleKeydown = (event) => {
  keysPressed.add(event.code);

  if (
    (keysPressed.has('AltLeft') || keysPressed.has('AltRight') ||
      keysPressed.has('MetaLeft') || keysPressed.has('MetaRight')) &&
    keysPressed.has('KeyS')
  ) {
    event.preventDefault();
    openSideView('search');
  }
};

const handleKeyup = (event) => {
  if (keysPressed.has(event.code)) {
    keysPressed.delete(event.code);
    keysPressed.clear();
  }
};

const goToProfileView = () => {
  router.push("/second-page");
}

const goToCartView = () => {
  router.push("/second-page");
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
  window.addEventListener('keyup', handleKeyup);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown);
  window.removeEventListener('keyup', handleKeyup);
});

</script>


<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: center; /* Center the logo */
  padding: 18px;
  height: 110px;
  background-color: #00a6ce;
  transition: transform 0.2s ease;
  transform: translateY(0);
}

.nav-links.nav-left,
.nav-links.nav-right {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.nav-links.nav-left {
  left: 18px;
}

.nav-links.nav-right {
  right: 18px;
  display: flex;
  gap: 15px;
}

.logo {
  height: 80px;
  object-fit: contain;
}

.material-symbols-outlined {
  font-size: 24px;
  cursor: pointer;
}

.hamburger-icon,
.profile-icon,
.cart-icon {
  color: white;
  font-size: 29px;
}

.hamburger-icon:hover,
.profile-icon:hover,
.cart-icon:hover {
  color: #d2d2d2;
}

.content {
  display: flex;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  z-index: 10;
  transition: opacity 0.3s ease;
}
</style>
