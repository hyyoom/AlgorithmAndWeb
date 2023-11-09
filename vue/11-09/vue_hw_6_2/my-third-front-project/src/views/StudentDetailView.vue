<template>
  <div>
    <h1>학생 상세 정보 페이지 입니다.</h1>
    <p>{{ studentName }}</p>
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'

  const route = useRoute()
  const studentName = route.params.detail
  console.log(route.params)
</script>

<style lang="scss" scoped>

</style>
