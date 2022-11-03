<template>
  <div>
    <h1>짜장면 먹고 로또</h1>
    <button @click="lottoNumber">Get Lucky Numbers</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function() {
    return {
      lottonums: _.range(1, 46)
    }
  },
  methods: {
    lottoNumber: function() {
      this.$emit('lotto-num', _.sampleSize(this.lottonums, 6))
    }
  }
}
</script>

<style>

</style>