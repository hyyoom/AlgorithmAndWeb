<template>
  <div>
    <div class="div1 line">
    <h4>{{ quiz.pk }}번 문제. {{quiz.question}}</h4>
    <p>정답입력</p>
    <input v-model="inputValue" @keyup.enter="pressEnter(quiz)" type="text" :id="quiz.pk" >

  </div>

  </div>
</template>

<script setup>
import {ref} from 'vue'

  import { useRoute, useRouter} from 'vue-router'
  const props = defineProps({
    quiz: Object,
  })
  const router = useRouter(props.quiz)
  const inputValue = ref('')
  const pressEnter = function(){
    router.push({ name: 'quizAnswer', params: {id: props.quiz.pk, answer:props.quiz.question},query:{answer:inputValue.value} })
  }



</script>

<style scoped>
      .div1 {
    background-color: lightgray;
    width: 800px;
    margin: 15px;
    border: 1px black solid;
    padding: 15px;
  }
  .line{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    
  }
</style>