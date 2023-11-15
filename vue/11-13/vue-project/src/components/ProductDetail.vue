<template>
    <div class="m-3 divBox col-3 d-flex flex-column justify-content-center align-items-center">
      <p>{{ product.name }}</p>
      <img :src="product.ImagePath" alt="">
      <p># {{ product.price }}</p>
      <p @click="changeFavorite(product)" :class="{isfavorite:product.isFavorite}">favorite</p>
    </div>
</template>

<script setup>
// import { useProductStore } from '@/stores/products'
const props = defineProps({
  product:Object
})


const changeFavorite = function(product){
  product.isFavorite = !product.isFavorite
}

</script>

<style scoped>
.divBox
{
  border: solid black 1px;
}
img{
  width: 100%;
}
.isfavorite{
  text-decoration: line-through;
}
</style>