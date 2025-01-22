import { createRouter, createWebHistory } from 'vue-router';

import Home from '../views/Home.vue';
import SecondPage from '../views/SecondPage.vue';

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
		path: '/item/:itemName',
		name: 'ItemView',
		component: Item,
		props: true
  }
]

const router = createRouter({
	history: createWebHistory('/'),
	routes
});

export default router;