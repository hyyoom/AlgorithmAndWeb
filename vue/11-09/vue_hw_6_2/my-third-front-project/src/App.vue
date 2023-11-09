<template>
  <div>
    <MainPage/>
    <RouterLink class="me-3" :to="{name:'some'}">Some</RouterLink>
    <RouterLink class="me-3" :to="{name:'other'}">Other</RouterLink>
    <RouterLink :to="{name:'students'}">Students</RouterLink>
    <RouterView></RouterView>
  </div>
  
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SomeView from '@/views/SomeView.vue';
import OtherView from '@/views/OtherView.vue';
import MainPage from '@/components/MainPage.vue';
</script>

<style lang="scss" scoped>

</style>