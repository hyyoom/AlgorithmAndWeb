

<template>
  <header class="container">
    <SearchBarComponent/>
  </header>
  <main class="container">
    <div class="d-flex flex-row justify-content-between">
      <div>
        <VideoDetailComponent
        :video-selected="selectedVideo"
        />
      </div>
      <div>
        <VideoListComponent
         :video-list="videoList"
         @item-select="onItemSelect"/>
      </div>
    </div>
  </main>
</template>

<script setup>
  import axios from 'axios'
  import SearchBarComponent from '@/components/SearchBarComponent.vue'
  import VideoDetailComponent from '@/components/VideoDetailComponent.vue'
  import VideoListComponent from '@/components/VideoListComponent.vue'
  
  import { ref, onMounted } from 'vue'
  
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const videoList = ref([])
  const onItemSelect = function(video){
    // console.log('다올라왔다!',video)
    selectedVideo.value = video
  }

    axios({
      url:API_URL,
      params:{
        type : 'video',
        part : 'snippet',
        key : 'AIzaSyAagmRDZ70FQ2unuBmlpX2S1lipGCQ7h1o',
        q : 'ssafy'
      }
    })
    .then((response)=>{
      console.log(response.data)
      videoList.value = response.data.items
    })

  const selectedVideo = ref(null)
  const keyword = ref('')

</script>

<style scoped>
  
</style>
