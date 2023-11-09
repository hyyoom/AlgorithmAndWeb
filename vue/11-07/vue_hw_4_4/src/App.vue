<template>
  <div>
    <input type="text" v-model="inputText">
    <p :class="inputText">제대로 입력하면 색이 바뀝니당.</p>
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  const inputText = ref()
  console.log(inputText.value)

</script>

<style  scoped>
.red{
  color : red;
}
.blue{
  color : blue;
}
.green{
  color : green;
}

</style>