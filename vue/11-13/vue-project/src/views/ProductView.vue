<template>
  <div class="row d-flex ms-5">
    <h1>상품 목록 페이지</h1>
    <ProductDetail
    v-for="product of store.productList"
    :key="product.id"
    :product="product"/>
    
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue'
import { useProductStore } from '@/stores/products'
  const store = useProductStore()
  // console.log(store.productList)


</script>

<style scoped>

</style>