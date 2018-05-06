<template lang="pug" id="user-delete">
  el-button(type="success" class="my-button" plain) Add New User
</template>

<script>
  export default {
    temlate: '#user-delete'
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js MyAPP'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .my-button {
    margin-top: 20px;
  }
</style>
