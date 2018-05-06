<template lang="pug">
  div.container
    div
      h1 Edit user
      el-form(:model="ruleForm", :rules="rules", ref="ruleForm", label-width="180px" class="bord")
        el-form-item(label="Username", prop="username" )
          el-input(v-model="ruleForm.username", style="width:240px")

        el-form-item(label="Email", prop="email" )
          el-input(v-model="ruleForm.email", style="width:240px")

        el-form-item
          el-button(type="primary", @click="submitForm('ruleForm')") Update
          el-button(@click="resetForm('ruleForm')") Back

</template>

<script>

  import axios from 'axios'

  export const HTTP = axios.create({
    baseURL: 'http://localhost:8000/api/'
  })

  export default {
    name: 'EditUser',
    data () {
      return {
        ruleForm: {
          username: '',
          email: ''
        },
        rules: {
          username: [
            { required: true, message: 'Please input Username', trigger: 'blur' },
            { min: 3, max: 10, message: 'Length should be 3 to 10', trigger: ['blur', 'change'] }
          ],
          email: [
            { required: true, message: 'Please input email address', trigger: 'blur' },
            { type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change'] }
          ]
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            HTTP.put('/users/', this.ruleForm)
              .then((response) => {
                this.$message({
                  message: 'User updated.',
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
