<template>
    <div class="d-flex flex-wrap">
      <div class="m-2 makeVideoCard col-12 col-sm-6 col-md-4 col-lg-3"
      v-for="video in videoList" 
      :key="video.id.videoId">
        <img @click="onClick(video)" :src="video.snippet.thumbnails.default.url" :alt="video.snippet.title">
        <p >{{ video.snippet.title }}</p>
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
  videoList : Array
})

const router = useRouter()
const onClick = function(video){
  localStorage.setItem('video', JSON.stringify(video))
  router.push('/detail')
}
</script>

<style scoped>

</style>