<template>
  <div>
    <p  v-for="student of students" @click="goDetail(student)">이름 : {{ student.name }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const students = ref([
    {name : '김하나'},
    {name : '김두리'},
    {name : '김서이'},
  ])

  const goDetail = function (student){
    router.push({name : 'studentsDetail', params: {detail : student.name}})
  }
</script>

<style lang="scss" scoped>

</style>