<template>
  <QuizCreate
  @create-quiz="updateQuiz" />


  <div>
    <QuizDetail v-for="quiz in sortedQuizList"
    :key="quiz.pk"
    :quiz="quiz"
    />

</div>
</template>

<script setup>
import QuizCreate from '@/components/QuizCreate.vue';
import QuizDetail from '@/components/QuizDetail.vue';
  import {ref, computed} from 'vue'
  
  let pk = 1
  const quizlist = ref([{
    pk: pk++, 
    question: 'Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?', 
    answer: 'flask'
  },
  {
    pk: pk++, 
    question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?', 
    answer: 'input'
  },
  {
    pk: pk++, 
    question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?', 
    answer: 'post'
  },
  {
    pk: pk++, 
    question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?', 
    answer: 'virtualenv'
  },
  {
    pk: pk++, 
    question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?', 
    answer: 'html'
  }])
  


const sortedQuizList = computed(() => {
  // quizlist를 내림차순으로 정렬
  return [...quizlist.value].sort((a, b) => b.pk - a.pk);
});
  const updateQuiz = function(quizInfo){
    quizlist.value.push({
    pk: pk++,
    question: quizInfo.question,
    answer: quizInfo.answer,
  });

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
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    
  }
</style>