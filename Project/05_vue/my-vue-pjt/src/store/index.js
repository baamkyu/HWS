import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    wantMovies: []
  },
  getters: {
  },
  mutations: {
    CREATE_MOVIE(state, wantMovie) {
      state.wantMovies.push(wantMovie)
    }
  },
  actions: {
    createWantMovies(context, wantMovies) {
      const wantMovies = {
        title: wantMovies,
        isCompleted: false,
      }
      context.commit('CREATE_MOVIE', wantMovie)
    }
  },
  modules: {
  }
})
