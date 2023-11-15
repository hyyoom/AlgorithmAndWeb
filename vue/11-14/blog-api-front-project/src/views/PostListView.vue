<template>
  <div class="full-screen-container d-flex flex-column align-items-center justify-content-center">
    <h1>유형민의 dsaf</h1>
    <p class="text-secondary">Welcome to my personal blog!</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBackDataStore } from '@/stores/backdata'
import { RouterLink } from 'vue-router'
// import PostList from '@/components/PostList.vue'


</script>

<style scoped>
.full-screen-container {
  height: 100vh; /* 높이를 화면 전체의 높이로 설정합니다. */
  width: 100%; /* 너비를 화면 전체의 너비로 설정합니다. */
  background-color: gainsboro;
}
</style>