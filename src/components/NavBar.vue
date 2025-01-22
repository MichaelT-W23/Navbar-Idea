<template>
  <div>
    <nav class="navbar" ref="navbarRef">
      <img :src="YellowLogo" alt="Yellow Logo" class="logo" />

      <div class="nav-center">
        <div class="nav-tabs">
          <span class="tab" 
                @mouseenter="showProductsDisplay"
                @mouseleave="hideProductsDisplay">
            Products
            <i class="material-icons expand-icon">expand_more</i>
          </span>
          <span class="tab" @click="navigateTo('/best-sellers')">Best Sellers</span>
          <span class="tab" @click="navigateTo('/our-story')">Our Story</span>
        </div>
      </div>

      <div class="nav-actions">
        <div class="shop-all-btn-section">
          <span class="shop-all-btn" @click="navigateTo('/shop-all')">Shop All</span>
        </div>
        <div class="nav-links">
          <span
            class="material-symbols-outlined search-icon"
            :class="{ active: activeSideView === 'search' }"
            @click="openSideView('search')"
            ref="searchIcon"
          >
            search
          </span>
          <div class="divider"></div>
          <span
            class="material-symbols-outlined profile-icon"
            :class="{ active: activeSideView === 'profile' }"
            @click="openSideView('profile')"
            ref="profileIcon"
          >
            account_circle
          </span>
          <div class="divider"></div>
          <span
            class="material-symbols-outlined cart-icon"
            :class="{ active: activeSideView === 'cart' }"
            @click="openSideView('cart')"
            ref="cartIcon"
          >
            shopping_cart
          </span>
        </div>
      </div>
    </nav>

    <div class="content">
      <div
        class="overlay"
        v-if="activeSideView"
        @click="closeSideView"
      ></div>
      <transition name="slide">
        <SearchSideView
          v-if="activeSideView === 'search'"
          @close="closeSideView"
        />
      </transition>
      <transition name="slide">
        <ProfileSideView
          v-if="activeSideView === 'profile'"
          @close="closeSideView"
        />
      </transition>
      <transition name="slide">
        <CartSideView
          v-if="activeSideView === 'cart'"
          @close="closeSideView"
        />
      </transition>
    </div>
  </div>
  <ProductsDisplay
    v-if="isProductsVisible"
    @mouseenter="showProductsDisplay"
    @mouseleave="hideProductsDisplay"
  />
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import YellowLogo from '../../images/logos/blue-logo.png';
import SearchSideView from './SearchSideView.vue';
import ProfileSideView from './ProfileSideView.vue';
import CartSideView from './CartSideView.vue';
import { useRouter } from 'vue-router';
import ProductsDisplay from './ProductsDisplay.vue';

const activeSideView = ref(null);
const activeIconPosition = ref(0);

const router = useRouter();

const searchIcon = ref(null);
const profileIcon = ref(null);
const cartIcon = ref(null);

const isProductsVisible = ref(false);
let hoverTimeout = null;

const showProductsDisplay = () => {
  clearTimeout(hoverTimeout);
  isProductsVisible.value = true;
};

const hideProductsDisplay = () => {
  hoverTimeout = setTimeout(() => {
    isProductsVisible.value = false;
  }, 100);
};

const openSideView = (view) => {
  activeSideView.value = view;
  updateTrianglePosition();
};

const closeSideView = () => {
  activeSideView.value = null;
};

const updateTrianglePosition = () => {
  const iconRefs = {
    search: searchIcon,
    profile: profileIcon,
    cart: cartIcon,
  };

  const activeRef = iconRefs[activeSideView.value];

  if (activeRef && activeRef.value) {
    const rect = activeRef.value.getBoundingClientRect();
    activeIconPosition.value = rect.left + rect.width / 2;
  }
};

const navigateTo = (tab) => {
  console.log(`Navigate to: ${tab}`);
  router.push(tab);
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

watch(activeSideView, updateTrianglePosition);

onMounted(() => {
  window.addEventListener('resize', updateTrianglePosition);
  window.addEventListener('keydown', handleKeydown);
  window.addEventListener('keyup', handleKeyup);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateTrianglePosition);
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
  justify-content: space-between;
  padding: 18px;
  height: 110px;
  background-color: #00a6ce;
  transition: transform 0.2s ease;
  transform: translateY(0);
}

.logo {
  height: 90px;
  object-fit: contain;
}

.nav-center {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-tabs {
  display: flex;
  gap: 1rem;
  font-size: 17px;
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  transition: color 0.4s ease;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 700;
  height: 110px;
  align-items: center;
}

.nav-tabs .tab {
  cursor: pointer;
  padding: 0px 20px;
  height: 100%;
  transition: background-color 0.3s ease;
  display: flex;
  align-items: center;
  /* background-color: red; */
}

.nav-tabs .tab .expand-icon {
  margin-left: 5px;
  font-size: 20px;
  align-self: center;
}

.nav-tabs .tab:hover {
  color: #e6e4e4;
}

.shop-all-btn-section {
  margin-right: 40px;
}

.shop-all-btn {
  font-size: 20px;
  color: #fff;
  font-weight: 700;
  font-family: Arial, Helvetica, sans-serif;
  padding: 15px 30px;
  border: 2px solid white;
  transition: background-color 0.3s ease, color 0.3s ease;
  cursor: pointer;
}

.shop-all-btn:hover {
  color: #e6e4e4;
  border: 2px solid #e6e4e4;
}

.nav-actions {
  display: flex;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 1rem;
  position: relative;
}

.divider {
  height: 25px;
  width: 1px;
  background-color: white;
  margin: 0 5px;
  align-self: center;
}

.material-symbols-outlined {
  font-size: 24px;
  cursor: pointer;
}

.search-icon,
.profile-icon,
.cart-icon {
  color: white;
  font-size: 29px;
}

.search-icon:hover,
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

.triangle {
  content: '';
  position: absolute;
  top: calc(100% - 10px);
  height: 0;
  width: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  left: 0;
  transform: translateX(-50%);
  transition: left 0.3s ease;
}

</style>
