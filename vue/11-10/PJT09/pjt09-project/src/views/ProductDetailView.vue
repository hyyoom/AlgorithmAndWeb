<template>
  <div class="product-card">
    <h1>pd.detail</h1>
      <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
      </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router';
import {computed} from 'vue'
import axios from 'axios'

const route = useRoute()
const product = ref('')
const productId = route.params.productId
const storeURL = `https://fakestoreapi.com/products/${productId}`
axios.get(storeURL)
.then((response)=>{
  product.value = response.data
})
.catch((error)=>{
  console.log(error)
})
console.log(productId)

</script>

<style lang="scss" scoped>
.product-card{
  border: 1px solid black;
  width: 220px;
}
.product-card img{
  width: 200px;
  height: 200px;
  object-fit: fill;
}

.product-list{
  flex-wrap: wrap;
  gap: 10px
}
</style>