<template>
  <div class="card m-3">
    <div class="d-flex flex-column">
      <h2 class="fw-bold align-self-center m-3">가수 이름</h2>
      <img class="my-4 rounded-circle align-self-center" src="@/assets/singer.jpg" alt="">
      <p class="align-self-center m-3">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Facilis, ducimus laboriosam quibusdam a atque et dolores dicta, fugit laborum ad fuga, voluptatibus omnis expedita eius amet pariatur inventore voluptatum molestiae.</p>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  img{
    width:30%
  }
  div{
    border: solid black 1px;
  }
  .card{
    display: inline-block;
    width : 40%;
    margin:20px
  }
</style>