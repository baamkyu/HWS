<template>
  <div>
    <h2>랜덤 영화 출력 페이지</h2>
    <button @click="randomMovie">button</button>
      <br>
      <img :src="posterUrl" alt="none">
      <p>제목 : {{ selectedMovie.title }}</p>
      <p>줄거리 : {{ selectedMovie.overview }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'RandomView',
  data() {
    return {
      selectedMovie: [],
      movieList: [],
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    getMovieList() {
      const getMovieDataURL = 'https://api.themoviedb.org/3/movie/top_rated'  
      // console.log(API_KEY)
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
    },
    randomMovie() {
      this.selectedMovie = _.sample(this.movieList)
    }
  },
  computed: {
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w185'+this.selectedMovie.poster_path
    }
  },
  created() {
    this.getMovieList()
    // this.randomMovie()
  },
}
</script>

<style>

</style>