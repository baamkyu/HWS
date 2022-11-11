<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'movies' }">Movie</router-link> |
      <router-link :to=" {name: 'random' }">Random</router-link> |
      <router-link :to=" {name: 'watchList' }">WatchList</router-link>
    </nav>
    <router-view/>
  </div>
</template>



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
