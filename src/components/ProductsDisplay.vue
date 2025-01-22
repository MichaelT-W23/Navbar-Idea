<template>
  <div 
    class="products-display" 
    @mouseenter="handleMouseEnter" 
    @mouseleave="handleMouseLeave"
  >
    <div class="products-container">
      <div 
          v-for="product in productData" 
          :key="product.name" 
          class="product-item"
          @click="goToView(product.route)"
      >
        <img :src="getImagePath(product.path)" :alt="product.name" class="product-image" />
        <p class="product-name">{{ product.name }}</p>
      </div>
    </div>
  </div>
</template>


<script setup>
import { useRouter } from 'vue-router';

const emit = defineEmits(['mouseenter', 'mouseleave']);

const router = useRouter();

const handleMouseEnter = () => {
  emit('mouseenter');
};

const handleMouseLeave = () => {
  emit('mouseleave');
};

const getImagePath = (relativePath) => {
  return new URL(`../../images/${relativePath}`, import.meta.url).href;
};

const goToView = (route) => {
  router.push(route);
  handleMouseLeave();
}

const productData = [
  {
    name: "Ginger Molasses",
    path: "GingerMolasses/GingerMolasses.jpg",
    route: "/item/Ginger_Molasses_Cookies"
  },
  {
    name: "Banana Bread",
    path: "BananaBread/BananaBread1.jpg",
    route: "/item/Banana_Bread"
  },
  {
    name: "Cinnamon Rolls",
    path: "CinnamonRolls/CinnamonRolls1.jpg",
    route: "/item/Cinnamon_Rolls"
  },
  {
    name: "Blueberry Zucchini",
    path: "BlueberryZucchini/BlueberryZucchini.jpg",
    route: "/item/Blueberry_Zucchini"
  },
  {
    name: "Brown Butter",
    path: "BrownButterCookies/BrownButterCookies1.jpg",
    route: "/item/Brown_Butter_Cookies"
  },
  {
    name: "Pumpkin Donuts",
    path: "PumpkinDonuts/PumpkinDonuts1.jpg",
    route: "/item/Pumpkin_Donuts"
  },
  {
    name: "Italian Bread",
    path: "ItalianBread/ItalianBread1.jpg",
    route: "/item/Italian_Bread"
  }
];

</script>


<style scoped>
.products-display {
  position: absolute;
  top: 110px;
  left: 0;
  width: 100%;
  height: 210px;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 15;
  padding: 20px;
}

.products-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  color: #333;
  font-family: Arial, sans-serif;
  font-size: 16px;
}

.product-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  text-align: center;
}

.product-item:hover {
  cursor: pointer;
}

.product-item:hover .product-name {
  text-decoration: underline;
}

.product-image {
  width: 130px;
  height: 130px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 10px;
}

</style>
