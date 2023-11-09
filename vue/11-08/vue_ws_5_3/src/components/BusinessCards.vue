<template>
<div class="d-flex justify-content-center flex-row row container">
  <BusinessCardDetail
  class="col-5"
  v-for="(card,idx) in businessCards"
  :business-cards="card"
  @on-click="checkClick(idx)"
  />
</div>
</template>

<script setup>
  import {ref} from 'vue'
  import BusinessCardDetail from '@/components/BusinessCardDetail.vue';

  const checkClick = function(idx){
    console.log("ss", idx)
    businessCards.value.splice(idx,1)
  }

  const businessCards = ref([
    {name: '일론 머스크', title: '테슬라 테크노킹'},
    {name: '래리 엘리슨', title: '오라클 창업주'},
    {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
    {name: '래리 페이지', title: '구글 공동창업주'},
    {name: '래리 페이지', title: '구글 공동창업주'},
  ])
</script>

<style scoped>
</style>