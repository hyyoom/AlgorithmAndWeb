import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBackDataStore = defineStore('backdata', () => {
  const posts = ref([])
  const API_URL = `http://127.0.0.1:8000`

  const setPosts = function(){
    axios({
      method : 'get',
      url : `${API_URL}/api/v1/postlist/`
    })
    .then((res)=>{
      posts.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  return { setPosts, posts, API_URL }
})
