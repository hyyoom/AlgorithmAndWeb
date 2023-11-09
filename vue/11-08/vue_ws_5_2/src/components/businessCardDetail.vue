<template>
  <div class="divSts container d-flex flex-column bg-light">
      <h5 class="mt-3 mb-1 fw-bold">이름 : {{businessCards.name}}</h5>
      <p>직함 : {{businessCards.title}}</p>
  </div>
  </template>
  
  <script setup>
    const card = defineProps({businessCards:Object})

  </script>
  
  <style scoped>
  .divSts {
    border: solid 1px;
    margin: 20px; 
  }
  </style>