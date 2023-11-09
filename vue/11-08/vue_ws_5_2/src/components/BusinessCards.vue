<template>
<div class="d-flex justify-content-center flex-row row container">
  <BusinessCardDetail
  class="col-5"
    v-for="card in businessCards"
    :business-cards="card"
  />
</div>
</template>

<script setup>
  import {ref} from 'vue'
  import BusinessCardDetail from '@/components/BusinessCardDetail.vue';
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