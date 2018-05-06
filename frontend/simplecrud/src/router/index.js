import Vue from 'vue'
import Router from 'vue-router'
import UserList from '@/components/UserList'
import AddUser from '@/components/AddUser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserList',
      component: UserList
    },
    {
      path: '/adduser',
      name: 'AddUser',
      component: AddUser
    }
  ]
})
