<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">MyTube</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink to="/"><a class="nav-link" href="#">Home</a></RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/search"><a class="nav-link" href="#">Search</a></RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink to="/later"><a class="nav-link" href="#">Later</a></RouterLink>

        </li>
      </ul>
    </div>
  </div>
</nav>
  <div>
    <RouterView></RouterView>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'

</script>


<style scoped>

</style>