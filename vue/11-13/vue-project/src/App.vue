<template>
  <div class="bg-secondary d-flex justify-content-center">
    <RouterLink class="m-2 text-white" to="/">Home</RouterLink>
    <RouterLink class="m-2 text-white" to="/product">Product</RouterLink>
    <RouterLink class="m-2 text-white" to="/favorite">Favorite <span v-show="store.CountFavorite > 0">{{store.CountFavorite}}</span></RouterLink>
  </div>
  <RouterView></RouterView>
</template>

<script setup>
import { useRouter,RouterView, RouterLink } from 'vue-router'
import { useProductStore } from '@/stores/products'
import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'
import FavoriteView from '@/views/FavoriteView.vue'

const store = useProductStore()
console.log(store.CountFavorite)
</script>


<style scoped>

</style>