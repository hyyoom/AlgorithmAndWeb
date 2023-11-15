<template>
  <div class="container">
    <h5 @click="goBack"> 뒤로가기</h5>
    <h1>비디오 검색</h1>
    <div class="input-group mb-3">
      <input v-model="inputValue" type="" class="form-control">
      <button @click="searchVideo" class="btn btn-primary" type="button">검색</button>
    </div>

    <!-- <div class="d-flex flex-wrap">
      <div class="m-2 makeVideoCard col-12 col-sm-6 col-md-4 col-lg-3"
      v-for="video in videoList" 
      :key="video.id.videoId">
        <img @click="onClick(video)" :src="video.snippet.thumbnails.default.url" :alt="video.snippet.title">
        <p >{{ video.snippet.title }}</p>
      </div>
    </div> -->
    <VideoListComponent
      :videoList="videoList"
    />
  </div>
</template>

<script setup>
import VideoDetailView from '@/views/VideoDetailView.vue'
import VideoListComponent from '@/components/VideoListComponent.vue'
import { RouterView, RouterLink, useRouter, useRoute } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const router = useRouter()
const inputValue = ref('')
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const videoList = ref([])

const goBack = function(){
  router.push('/')
}

const searchVideo = function(){
  axios({
    url:API_URL,
    params:{
      type : 'video',
      part : 'snippet',
      key : 'AIzaSyB45zN4TL3WO0pGKQcVPhByfX6M00FLQPg',
      q : inputValue.value
    }
  })
  .then((response)=>{
    videoList.value = response.data.items
  })
}

// const onClick = function(video){
//   localStorage.setItem('video', JSON.stringify(video))
//   router.push('/detail')
// }

</script>

<style scoped>
.makeVideoCard{
  border: solid black 1px;
  width : 400px;

}
.makeVideoCard img{
  width : 100%;
}
</style>
