<template lang="pug">
  div.container
    div

      el-form(:model="ruleForm", :rules="rules", ref="ruleForm", label-width="180px" class="bord")
        el-form-item(label="Username", prop="username" )
          el-input(v-model="ruleForm.username", style="width:240px")

        el-form-item(label="Email", prop="email" )
          el-input(v-model="ruleForm.email", style="width:240px")

        el-form-item(label="Role" prop="role")
          el-select(v-model="ruleForm.role" placeholder="Role")
            el-option(label="Admin" value="admin")
            el-option(label="User" value="user")
            el-option(label="Manager" value="manager")
        el-form-item
          el-button(type="primary", @click="submitForm('ruleForm')") Create
          el-button(@click="resetForm('ruleForm')") Reset

</template>

<script>

import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/'
})

export default {
  name: 'AddUser',
  data () {
    return {
      ruleForm: {
        username: '',
        email: '',
        role: ''
      },
      rules: {
        username: [
          { required: true, message: 'Please input Username', trigger: 'blur' },
          { min: 3, max: 10, message: 'Length should be 3 to 10', trigger: ['blur', 'change'] }
        ],
        email: [
          { required: true, message: 'Please input email address', trigger: 'blur' },
          { type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change'] }
        ],
        role: [
          { required: true, message: 'Please select Role', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          HTTP.post('/users/', this.ruleForm)
            .then((response) => {
              this.$message({
                message: 'User added.',
                type: 'success'
              })
              this.$router.push({name: 'UserList'})
            })
            .catch((err) => {
              console.log(err)
            })
        } else {
          this.$message.error('Oops, fill all text field.')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
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
  padding-top: 25px;
}

</style>
