<template>
	<p class="title">Best Sellers</p>
	<LinkBtn
		:path="'/'"
		:buttonText="'Go to Home page'">
	</LinkBtn>
</template>


<script setup>
import LinkBtn from '../components/RouterBtn.vue';
</script>


<style scoped>

.title {
	font-size: 25px;
	color: green;
	font-family: Arial, sans-serif;
}

</style>