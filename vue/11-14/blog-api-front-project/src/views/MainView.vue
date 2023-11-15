<template>
  <div class="full-screen-container d-flex flex-column align-items-center justify-content-center">
    <h1>유형민의 블로그</h1>
    <p class="text-secondary">Welcome to my personal blog!</p>
    <p v-for="ca of category">{{ca.name}}</p>
  </div>
</template>

<script setup>
import { onMounted,ref } from 'vue';
import { useBackDataStore } from '@/stores/backdata'
import axios from 'axios'
const store = useBackDataStore()
const category = ref(null)

onMounted(()=>{
  axios({
      method : 'GET',
      url : `http://127.0.0.1:8000/api/v1/categorycreate/`
    })
    .then((res)=>{
      category.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }
)


</script>

<style scoped>
.full-screen-container {
  height: 100vh; /* 높이를 화면 전체의 높이로 설정합니다. */
  width: 100%; /* 너비를 화면 전체의 너비로 설정합니다. */
  background-color: gainsboro;
}
</style>