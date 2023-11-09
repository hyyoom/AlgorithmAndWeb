<template>
  <div>
    <h1>여기는 리스트</h1>
    <ul>
      <VideoListItemComponent
      v-for="video of videoList"
      :key="video.id.videoId"
      :video="video"
      @item-select="onItemSelect"/>
    </ul>
  </div>
</template>

<script setup>
  import VideoListItemComponent from '@/components/VideoListItemComponent.vue'
  defineProps({videoList:Array})
  const emit = defineEmits(['itemSelect'])
  const onItemSelect = function(video){
    // console.log('아이템이 선택되었습니다.')
    // console.log(video)
    emit('itemSelect',video)
  }
</script>

<style scoped>

</style>