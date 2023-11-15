<template>
  <div class="container m-3">
    <h5 @click="goBack"> 뒤로가기</h5>
    
    <h2>{{ tmp.snippet.title }}</h2>
    <iframe width="560" height="315" :src="videoUrl" frameborder="0"></iframe>
    <p>{{ tmp.snippet.description }} </p>
    <button @click="onClick(saveStatus)" class="btn btn-primary">{{ saveStatus }}</button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const tmp = JSON.parse(localStorage.getItem('video'))
const saveStatus = ref('')
const videoUrl = computed(() => {
  if (tmp && tmp.id && tmp.id.videoId) {
    return `https://www.youtube.com/embed/${tmp.id.videoId}`
  }
  return ''
})

const goBack = function(saveStatus){
  router.push('/search')
}

const existingCart2 = JSON.parse(localStorage.getItem('saveVideo')) || []
const isDuplicate2 = existingCart2.length > 0 && existingCart2.find((item) => item.id.videoId === tmp.id.videoId)
//isD~ True 라면 동영상이 있는거니까
if (isDuplicate2){
  saveStatus.value='동영상 저장 취소'
  console.log(saveStatus.value, "1")
}
else{
  saveStatus.value='동영상 저장'
  console.log(saveStatus.value, "2")
}




const onClick = function(){
  const existingCart = JSON.parse(localStorage.getItem('saveVideo')) || []
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id.videoId === tmp.id.videoId)

  if(!isDuplicate) {
    alert('장바구니에 추가합니다')
    existingCart.push(tmp)
    saveStatus.value='동영상 저장 취소'
  } else {
    alert("삭제됨")
    saveStatus.value='동영상 저장'
    const itemidx = existingCart.findIndex((item)=>item.id.videoId === tmp.id.videoId)
    existingCart.splice(itemidx, 1)
  }
  localStorage.setItem('saveVideo', JSON.stringify(existingCart))
  // router.push('/cart')
}
</script>

<style scoped>

</style>
