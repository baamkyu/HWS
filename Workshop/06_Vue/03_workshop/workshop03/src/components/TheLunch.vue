<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="pickOne">Pick One</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function() {
    return {
      menu: ['국밥', '짜장면', '햄버거']
    }
  },
  methods: {
    pickOne: function() {
      this.$emit('pick-one', _.sample(this.menu))
    }

    
  },
}
</script>

<style>

</style>