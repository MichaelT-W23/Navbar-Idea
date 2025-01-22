<template>
	<p class="title">Our Story</p>
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
	color: red;
	font-family: Arial, sans-serif;
}

</style>