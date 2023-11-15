<template>
  <div class="row d-flex ms-5">
    <h1>상품 목록 페이지</h1>
    <ProductDetail
    v-for="product of productListForFavorite"
    :key="product.id"
    :product="product"/>
    
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue'
import { useProductStore } from '@/stores/products'
const store = useProductStore()
const productListForFavorite = store.isFavorite
console.log(productListForFavorite)

</script>

<style scoped>

</style>