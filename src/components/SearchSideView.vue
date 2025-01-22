<template>
  <transition name="slide">
    <div class="side-view-container">
      <p class="search-title">Search</p>
      <button class="close-btn" @click="emitClose">
        Close
        <span class="material-symbols-outlined close-icon">close</span>
      </button>
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search for items..."
        class="search-bar"
      />
      <p v-if="searchQuery.trim() !== ''" class="results-text">
        Showing results for {{ searchQuery }}
      </p>
      <p v-if="searchQuery.trim() !== '' && filteredItems.length === 0" 
        class="empty-results-text">
        We couldn't find any items for {{ searchQuery }}, try our 
          <span
            @click="goToSearchPage"
            class="search-page-link">
            search page</span>.
      </p>
      <ul>
        <li
          v-for="item in filteredItems"
          :key="item.id"
          class="menu-item"
        >
          <div @click="goToItem(item)" class="item-link">
            <img
              :src="`../images/${item.Images[0]}`"
              alt="item.DisplayName"
              class="item-image"
            />
            <div class="item-details">
              <div class="item-header">
                <span class="item-name">{{ item.DisplayName }}</span>
                <span class="item-emoji">{{ item.Emoji }}</span>
              </div>
              <span class="item-price">{{ item.DisplayPrice }}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </transition>
</template>


<script setup>
import { ref, computed } from 'vue';
import menuData from "../../data/menu.json";
import { useRouter } from 'vue-router';

const router = useRouter();
const { MenuItems } = menuData;

const emit = defineEmits(["close"]);

const emitClose = () => {
  emit("close");
};

const searchQuery = ref("");

const filteredItems = computed(() => {
  if (searchQuery.value.trim() === "") {
    return [];
  }

  return MenuItems.filter((item) =>
    item.DisplayName.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const goToItem = (item) => {
  router.push({ 
    name: 'ItemView', 
    params: {
      itemName: item.Name 
    } 
  });

  emitClose();
};

const goToSearchPage = () => {
  console.log("SEARCH PAGE");
  router.push("/second-page");
  emitClose();
}

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
  top: 17px;
  right: 10px;
  background: none;
  color: #000;
  border: none;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: flex-end;
}

.close-icon {
  font-size: 16px;
}

.close-btn:hover .close-icon {
  color: red;
}

.search-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #00a6ce;
}

.search-bar {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 40px;
  margin-top: 0.75rem;
  font-size: 16px;
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

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 12px;
}

.menu-item {
  display: flex;
  background-color: #ececec;
  border-radius: 8px;
  overflow: hidden;
}

.menu-item:hover {
  background-color: #d7d7d7;
  cursor: pointer;
}

.results-text {
  color: #464747;
  line-height: 1.5;
  margin-top: -5px;
  margin-bottom: 10px;
  font-weight: 550;
}

.empty-results-text {
  color: #686868;
  margin-top: -10px;
  font-size: 18px;
}

.search-page-link {
  color: #00a6ce;
}

.search-page-link:hover {
  color: darkblue;
  cursor: pointer;
}

.item-link {
  display: flex;
  align-items: flex-start;
  text-decoration: none;
  color: inherit;
  width: 100%;
  padding: 9px;
}

.item-image {
  width: 70px;
  height: 70px;
  object-fit: cover;
  border-radius: 8px;
  flex-shrink: 0;
}

.item-details {
  display: flex;
  flex-direction: column;
  margin-left: 1rem;
}

.item-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.item-name {
  font-weight: bold;
  font-size: 17px;
  margin-right: auto;
}

.item-emoji {
  font-size: 1.5rem;
  margin-left: 0.5rem;
}

.item-price {
  font-size: 15px;
  color: #555;
  margin-top: 0.3rem;
}

</style>
