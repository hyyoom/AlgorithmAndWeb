<template>
  <li @click="onClick">
    <!-- {{ video }} -->
    <img :src="video.snippet.thumbnails.default.url" alt="">
    <!-- <p>id : {{ video.id.videoId }}</p> -->
    <p>{{ video.snippet.title }}</p>
  </li>
</template>

<script setup>
  const emit = defineEmits(['itemSelect'])
  const props = defineProps({
    video:Object
  })

  const onClick = function(){
    emit('itemSelect',props.video)
  }
</script>

<style  scoped>

</style>