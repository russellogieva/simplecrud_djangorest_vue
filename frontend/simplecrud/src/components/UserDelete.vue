<template lang="pug">
  div.container
    div.bord
        h1 Delete user
        p The action cannot be undone.
        el-button(type="danger", @click="deleteUser") Delete
        el-button(type="info", @click="cancel") Cancel
</template>

<script>

import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/'
})

export default {
  name: 'DeleteUser',
  methods: {
    deleteUser () {
      var userId = this.$route.params.user_id
      console.log(userId)
      HTTP.delete('/users/' + userId + '/')
        .then(res => {
          this.$message({
            message: 'User deleted.',
            type: 'success'
          })
          this.$router.push({name: 'UserList'})
        })
        .catch(error => console.log(error))
    },
    cancel () {
      this.$router.push({name: 'UserList'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 100%;
  max-width: 1040px;
  margin: 20px auto 0;
}

.bord {
  border: 2px solid rgba(93, 93, 93, 0.39);
  border-radius: 5px;
  padding: 20px;
  width: 300px;
}

p {
  padding-bottom: 10px;
}

</style>
