<template>
  <div>
    <h1>Home</h1>
    <div v-if="productisEmpty" class="d-flex product-list" >
      <div v-for="product in products" :key="product.id" class="product-card">
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="addCart(product)">장바구니 추가</button>

      </div>
    </div>

  </div>
</template>
<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';

const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'

const router = useRouter()
const goDetail = function(product){
  router.push(`/detail/${product.id}`)
}


axios.get(storeURL)
.then((response)=>{
  products.value = response.data
})
.catch((error)=>{
  console.log(error)
})

const productisEmpty = computed(()=>{
  return products.value.length > 0 ? true : false
})

const addCart = (product)=>{
  //하나의 데이터만 저장하는것
  //문제점은 덮어 쓰기 되어버린다.
  // localStorage.setItem('cart', JSON.stringify(product))
  // const tmp = localStorage.getItem('cart')
  // console.log(tmp)

  //여러 데이터 저장
  //중복 체크
  //localStorage에서 객체 형태로 데이터 가져오는데 없다면 빈 리스트 반환
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []

  //중복된 제품이 있는지 확인
  const isDuplicate = existingCart.length > 0 && existingCart.find(item=>item.id===product.id)
  //중복이 아니라면 추가

  if (isDuplicate){
    existingCart.push(product)
  }
  else{
    alert("이미 있는 상품")
  }

  localStorage.setItem('cart', JSON.stringify(existingCart))
}



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