<template>
	<p class="title">Shop All</p>
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
	color: blue;
	font-family: Arial, sans-serif;
}

</style>