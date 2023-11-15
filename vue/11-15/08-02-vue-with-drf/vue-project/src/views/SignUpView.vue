<template>
  <div>
    <h1>SignUP</h1>
    <form @submit.prevent="signup">
      <input v-model.trim="username" type="text">
      <input v-model.trim="password1" type="password">
      <input v-model.trim="password2" type="password">
      <input type="submit">

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'


const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signup = function(){
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value,
  }
  store.signUp(payload)
}

</script>

<style>

</style>
