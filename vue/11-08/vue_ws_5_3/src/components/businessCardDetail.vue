<template>
  <div class="divSts container d-flex flex-column bg-light">
      <h5 class="mt-3 mb-1 fw-bold">이름 : {{businessCards.name}}</h5>
      <p>직함 : {{businessCards.title}}</p>
      <button class="btn-sm" @click="onClick">명함 삭제</button>
  </div>
  </template>
  
  <script setup>
    const card = defineProps({businessCards:Object})
    const emit = defineEmits(['onClick'])

    const onClick = function(){
      emit('onClick', card)
    }
  </script>
  
  <style scoped>
  .divSts {
    border: solid 1px;
    margin: 20px; 
  }
  </style>