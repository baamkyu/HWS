<template>
  <div id="app">
    <TheLunch @pick-one="pickOneEvent"/>
    <h3>{{ lunchmenu }}</h3>
    <hr>
    <TheLotto @lotto-num="lottoNumEvent"/>
    <h3> {{ lottonums }}</h3>
  </div>
</template>

<script>
import TheLotto from '@/components/TheLotto'
import TheLunch from '@/components/TheLunch'

export default {
  name: 'App',
  components: {
    TheLotto,
    TheLunch
  },
  data: function() {
    return {
      lunchmenu: '',
      lottonums: [],
    }
  },
  methods: {
    pickOneEvent: function (data) {
      this.lunchmenu = data
    },
    lottoNumEvent: function(numbers) {
      this.lottonums = numbers
      this.lottonums.sort()
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
