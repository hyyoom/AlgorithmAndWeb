<template>
<div class="d-flex justify-content-center flex-row row container">
  <form class="d-flex justify-content-center" @submit="handleFormSubmit">
    <p>이름 <input :v-model="addName" type="text" class="m-2"></p>
    <p>{{ addName }}</p>
    <p>직함 <input :v-model="addtitle" type="text" class="m-2"></p>
    <input type="submit" value="명함 추가" class="m-2">
  </form>

  <p v-if="businessCards.length">현재 보유중인 명함 수 : {{businessCards.length}}</p>
  <p v-else>명함이 없습니다. 새로운 명함을 추가해 주세요</p>
  <BusinessCardDetail
  class="col-5"
  v-for="(card,idx) in businessCards"
  :business-cards="card"
  @on-click="checkClick(idx)"
  />
</div>
</template>

<script setup>
  import { createApp,ref } from 'vue'
  import BusinessCardDetail from '@/components/BusinessCardDetail.vue';
  const addName= ref('')
  const addtitle= ref('')

  const checkClick = function(idx){
    businessCards.value.splice(idx,1)
  }
  const handleFormSubmit = function (event) {
    event.preventDefault(); // 기본 동작 방지
    // 여기에 폼 제출과 관련된 로직을 추가할 수 있습니다.
    console.log(addName)

  };

  const businessCards = ref([
    {name: '일론 머스크', title: '테슬라 테크노킹'},
    {name: '래리 엘리슨', title: '오라클 창업주'},
    {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
    {name: '래리 페이지', title: '구글 공동창업주'},
    {name: '래리 페이지', title: '구글 공동창업주'},
  ])

  // const apps = createApp({
  //   setup(event){
  //     event.preventDefault()
  //     return {

  //     }
  //   }
  // })
  // apps.mount('#apps')

</script>

<style scoped>
</style>