<template>
  <header>
    <div class="container d-flex justify-content-center align-items-center  bg-primary mt-3" style=" width: 350px; height:150px;">
      <h1 class="text-white fw-bold">명함 관리 페이지</h1>
    </div>
  </header>
  <main>
    <p class="text-center mt-3">명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
  </main>
  <h1 class="fw-bold text-center m-3">보유 명함 목록</h1>
  <article class="d-flex justify-content-center text-center">
    <businessCards/>
  </article>
  <footer class="footer">
      <p class="text-center mt-4">2023 My Business Cards</p>
  </footer>

</template>

<script setup>
  import businessCards from './components/businessCards.vue';
  import BusinessCardDetail from './components/BusinessCardDetail.vue';
  


</script>

<style scoped>
    .footer {
      position: fixed;
      left: 0;
      bottom: 0;
      height: 70px;
      width: 100%;
      background-color: #807c7c;
      color: black;
    }
    
</style>