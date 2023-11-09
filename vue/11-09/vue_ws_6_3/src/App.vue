<template>
  <div >
    <div class="div1 line">
      <div class="line div2 width">
        <h2>Quiz 퀴즈</h2>
      </div>
      <div class="line width div3">
        여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!
      </div>
      
      <br>
      <nav class="line width nav1">
        <span>
          <RouterLink class="white" to="/">Home </RouterLink> |
          <RouterLink class="white" to="/quiz">Quiz </RouterLink> |
        </span>
      </nav>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
  .line{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
  .div1 {
    background-color: lightgray;
    width: 800px;
    margin: auto;
    padding: 15px;
  }
  .div2 {
    background-color: orange;
    color: white;
  }
  .width {
    width: 90%;
    margin: auto;
  }
  .div3{
    background-color: white;
    height: 100px;
  }
  .nav1 {
    color: white;
    background-color: black;
    text-decoration: none;
   
  }
  .white {
    color: white;
    text-decoration: none;
  }
</style>