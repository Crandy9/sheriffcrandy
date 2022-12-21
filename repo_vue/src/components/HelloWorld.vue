<template>
  <!-- give some padding to keep it under transparent navbar -->
  <div class="hello" style="color:green; padding-top: 2rem;">
    <!-- coming from HomeView.vue -->
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>