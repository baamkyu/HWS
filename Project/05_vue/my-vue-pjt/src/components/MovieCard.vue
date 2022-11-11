<template>
  <div class="card">
    <img :src="posterUrl" alt="none">
    <div class="cardbody">
      <p>제목 : {{ movie.title }}</p>
      <p>줄거리 : {{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieCard',  
  props: {
    movie: Object,
  },
  computed: {
      posterUrl() {
        return 'https://image.tmdb.org/t/p/w185'+this.movie.poster_path
    },
  }
}
</script>

<style>

.card{		
  display: inline-block;
  width: 300px;
}

.cardbody{
  overflow: hidden;
  width: 300px;
  height: 300px;
}

</style>