<template>
  <div class="line">
  <div class="line">
    <form @submit.prevent="createQuiz">
    <h3>퀴즈 생성</h3>
    <label for="question">문제</label>
    <input type="text" name="question" id="question" v-model="question">
    <label for="answer">답안</label>
    <input type="text" name="answer" id="answer" v-model="answer">
    <button>퀴즈 생성</button>
  </form>
  </div>
</div>
</template>

<script setup>
  import {ref} from 'vue'
  const question =ref('')
  const answer = ref('')
  const emit = defineEmits(['createQuiz'])
  const createQuiz = function() {
    const quizInfo = {question:question.value,answer:answer.value}
    emit('createQuiz', quizInfo)
    question.value=''
    answer.value=''

  }
</script>

<style scoped>
  .line{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    width: 830px;
    background-color: lightgray;
  }
button {
  background-color: blue;
  text-align: center;
  color: white;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 10px
}
</style>