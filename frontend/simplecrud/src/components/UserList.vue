<template lang="pug">
  div.container
    el-button(type="success"  plain,   style="margin-top: 15px; margin-bottom: 5px;", @click="openAddUser", icon="el-icon-plus")
    div(style="margin-bottom: 20px; width:380px")
      el-input(placeholder="Input username", v-model="search_result", style="width:180px")
      el-button(type="success", style="margin-left: 5px", @click="getUser", icon="el-icon-search")
    el-table(:data="users", border, style="width: 100%")
      el-table-column(prop="id", label="ID", width="180")
      el-table-column(prop="username", label="Username", width="180")
      el-table-column(prop="email", label="Email", width="180")

      el-table-column(
      prop="role",
      label="Role",
      :filters="[{ text: 'admin', value: 'admin' }, { text: 'user', value: 'user' }, { text: 'manager', value: 'manager' }]",
      :filter-method="filterTag",
      filter-placement="bottom-end")
        template(slot-scope="scope")
          el-tag(
          :type="scope.row.role | statusFilter"
          disable-transitions) {{scope.row.role}}
      el-table-column(label="Operations")
        template(slot-scope="scope")
          el-button(size="mini", @click="openUpdate(scope.row.id , scope.row.username, scope.row.email, scope.row.role)", icon="el-icon-edit")
          el-button(size="mini", type="danger", @click="openDelete(scope.row.id)") Delete

    div(style="margin-top: 20px")
      el-button(type="info" plain, @click='getUsers', icon="el-icon-refresh")
</template>

<script>

import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/'
})

export default {
  name: 'UserList',
  data () {
    return {
      users: []
    }
  },
  search_result: '',
  methods: {

    getUser () {
      var url = '/users/'
      if (this.search_result !== '' || this.search_result !== null) {
        url = `/users/?username=${this.search_result}`
      }
      HTTP.get(url)
        .then(res => {
          this.users = res.data
        })
        .catch(error => console.log(error))
    },

    getUsers () {
      HTTP.get('/users/')
        .then(res => {
          this.users = res.data
          this.search_result = ''
        })
        .catch(error => console.log(error))
    },

    filterTag (value, row) {
      return row.role === value
    },

    openUpdate (id, username, email, role) {
      console.log(id, username)
      this.$router.push({name: 'UpdateUser', params: {user_id: id, user_name: username, user_email: email, user_role: role}})
    },

    openDelete (id) {
      console.log(id)
      this.$router.push({name: 'DeleteUser', params: {user_id: id}})
    },
    openAddUser () {
      this.$router.push({name: 'AddUser'})
    }
  },

  mounted: function () {
    this.getUsers()
  },

  filters: {
    statusFilter (status) {
      const statusMap = {
        admin: 'danger',
        user: 'warning',
        manager: 'success'
      }
      return statusMap[status]
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
