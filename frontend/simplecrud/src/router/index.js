import Vue from 'vue'
import Router from 'vue-router'
import UserList from '@/components/UserList'
import AddUser from '@/components/AddUser'
import DeleteUser from '@/components/UserDelete'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserList',
      component: UserList
    },
    {
      path: '/add',
      name: 'AddUser',
      component: AddUser
    },
    {
      path: '/:user_id/delete',
      name: 'DeleteUser',
      component: DeleteUser
    }
  ]
})
