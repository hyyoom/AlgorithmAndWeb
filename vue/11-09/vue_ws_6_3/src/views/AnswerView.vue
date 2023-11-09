<template>
  <div>

  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
// console.log(route)
const params = ref(route.params)
const query = ref(route.query)
console.log(params.value.id)





</script>

<style scoped>

</style>