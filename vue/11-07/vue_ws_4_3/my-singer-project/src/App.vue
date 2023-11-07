<template>
  <div>
    <MainPage/>
    <singerList/>
    <div class="d-flex justify-content-center">
      <SingerDetail/>
      <SingerDetail/>
    </div>
  </div>
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue';
  import SingerDetail from '@/components/singer/SingerDetail.vue';
  import singerList from '@/components/singerList.vue';
</script>

<style scoped>

</style>