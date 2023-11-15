<template>
  <div>
    <h1>여기는 레이터</h1>
    <VideoListComponent
      :videoList="videoList"
    />
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import VideoListComponent from '@/components/VideoListComponent.vue'
const videoList = ref([])
onMounted(()=>{
  videoList.value = JSON.parse(localStorage.getItem('saveVideo')) || []
})
</script>

<style scoped>

</style>