
<template>
  <header>
    <div>
      <nav class="navStyle text-center d-flex align-items-center justify-content-center">
        <RouterLink :to="{name:'Main'}"><p class="text-white m-0 me-4">Home</p></RouterLink>
        <RouterLink :to="{name:'PostList'}"><p class="text-white m-0 me-4">PostList</p></RouterLink>
        <RouterLink :to="{name:'category'}"><p class="text-white m-0 me-4">CategoryCreate</p></RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useBackDataStore } from '@/stores/backdata.js'


const store = useBackDataStore()
store.setPosts()


</script>




<style scoped>
.navStyle{
  background: gray;
  height: 50px;

}
</style>
