import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home.vue';
import SecondPage from '../views/SecondPage.vue';

import BestSellers from '../views/BestSellers.vue';
import OurStory from '../views/OurStory.vue';
import ShopAll from '../views/ShopAll.vue';

import Item from '../views/Item.vue'


const routes = [
	{
		path: '/',
		component: Home
	},
	{
		path: '/second-page',
		component: SecondPage
	},
	{
		path: '/best-sellers',
		component: BestSellers
	},
	{
		path: '/our-story',
		component: OurStory
	},
	{
		path: '/shop-all',
		component: ShopAll
	},
	{
		path: '/item/:itemName',
		name: 'ItemView',
		component: Item,
		props: true
  }
]

const router = createRouter({
	history: createWebHistory('/Navbar-Idea/'),
	routes
});

export default router;