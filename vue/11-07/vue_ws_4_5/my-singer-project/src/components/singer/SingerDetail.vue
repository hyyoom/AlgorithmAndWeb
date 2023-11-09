<template>
  <div class="card m-3">
    <div class="d-flex divs flex-column">
      <h2 class="fw-bold align-self-center m-3">가수 이름</h2>
      <img class="my-4 rounded-circle align-self-center" src="@/assets/singer.jpg" alt="">
      <div class="d-flex justify-content-evenly">
        <div class="border border-2 m-3">
          <h3 class="text-center">앨범 제목</h3>
          <p class="text-center">노래 목록1</p>
          <p class="text-center">노래 목록2</p>
          <p class="text-center">노래 목록3</p>
        </div>
        <div class="border border-2 m-3">
          <h3 class="text-center">앨범 제목</h3>
          <p class="text-center">노래 목록1</p>
          <p class="text-center">노래 목록2</p>
          <p class="text-center">노래 목록3</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  img{
    width:30%
  }
  .divs{
    border: solid black 1px;
  }
  .card{
    display: inline-block;
    width : 40%;
    margin:20px
  }
</style>