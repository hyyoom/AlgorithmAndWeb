<template>
  <div class="container m-5">
    <p class="m-3">category 종류:</p>
    <form @submit.prevent="makeCategory" class="m-3 d-flex flex-column justify-content-center align-items-center">
      <input v-model.trim="inputTexts" type="text">
      <input class="btn btn-primary text-center" type="submit" value="카테고리 생성">
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useBackDataStore } from '@/stores/backdata.js'
import axios from 'axios'

const store = useBackDataStore()
const inputTexts = ref('')
const router = useRouter()

const makeCategory = function(){
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/categorycreate/`,
    data : {
      name : inputTexts.value
    }
    })
    .then((res) => {
        console.log(res)
        router.push({ name: 'Main' })
    })
    .catch((err) => {
      console.log(err)
    })
  }



</script>



<style scoped>
input{
  width: 100%;
}

div{
  border: solid black 1px;
}
</style>