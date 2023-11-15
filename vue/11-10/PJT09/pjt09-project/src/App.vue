<template>
  <nav class="container">
    <RouterLink class="m-2" to="/">Home</RouterLink>
    <RouterLink class="m-2" to="/detail">상세 페이지</RouterLink>
    <RouterLink class="m-2" to="/cart">메인 페이지</RouterLink>


  </nav>
  <RouterView></RouterView>
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router' 
import CartView from './views/CartView.vue';
import HomeView from './views/HomeView.vue';
import ProductDetailView from './views/ProductDetailView.vue';





</script>

<style scoped>

</style>