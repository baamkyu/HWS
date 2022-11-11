<template>
  <div class="view">
    <h2>전체 영화 목록 페이지</h2>
    <MovieCard
      v-for="(movie, index) in movieList"
      :key="index"
      :movie="movie"
    />
    <button @click="getMovieList">getMovieList</button>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'MovieView',
  components: {
    MovieCard
  },
  data() {
    return {
      movieList: []
    }
  },
  created() {
    this.getMovieList()
  },
  methods: {
    getMovieList() {
      const getMovieDataURL = 'https://api.themoviedb.org/3/movie/top_rated'  
      console.log(API_KEY)
      axios({
        method: 'get',
        url: getMovieDataURL,
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
      .then((response) => {
        const movieData = response.data.results
        // const movieData = console.log(response)
        this.movieList = movieData
      })
      .catch((response) => {
        console.log(response)
      })
    }
  }
}
</script>

<style>


</style>