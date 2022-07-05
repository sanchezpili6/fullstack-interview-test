<template>
  <v-card light color="#BDD6D0" min-width="500px">
    <v-card-title>
      {{pull_request.title}}
      <v-spacer></v-spacer>
      <v-btn color="#fda855" fab x-small @click=closeModal>
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-subtitle>{{pull_request.author}}</v-card-subtitle>
    <v-card-text class="white text--primary">
      <p>{{pull_request.date}}</p>
      <div
          class="body"
          v-html="markdownToHTML(pull_request.body)"
      ></div>
    </v-card-text>
    <v-card-actions v-show="pull_request.status != 'closed'" >
      <v-spacer></v-spacer>
      <v-btn  color="#fda855" @click=closePullRequest>Close Pull Request</v-btn>
      <v-spacer></v-spacer>
      <v-btn color="#fda855" @click=mergePullRequest>Merge Pull Request</v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
import {get_pull_request} from "@/helpers/Services";
import {close_pull_request} from "@/helpers/Services";
import {merge_pull_request} from "@/helpers/Services";
import {marked} from "marked";
export default {
  name: "PullRequestDetailsModal.vue",
  mounted() {
    this.getPullRequest()
  },
  props: ["pull_request_number"],
  data () {
    return {
      pull_request: {},
    }
  },
  methods:{
    async getPullRequest(){
      this.pull_request = await get_pull_request(this.pull_request_number)
    },
    async closePullRequest(){
      await close_pull_request(this.pull_request.number)
      this.closeModal()
    },
    async mergePullRequest(){
      await merge_pull_request(this.pull_request.number)
      this.closeModal()
    },
    closeModal(){
      this.$emit("showModal",false)
    },
    markdownToHTML(markdown){
      const createDOMPurify = require('dompurify');
      const DOMPurify = createDOMPurify();
      let sanitizedHTML = DOMPurify.sanitize(marked(markdown))
      return sanitizedHTML.replace(/<img/g, '<img style="max-width:600px;"')
    },
  },
}
</script>

<style scoped>
  .body{
    min-width: 300px;
    max-width: 700px;
    max-height: 650px;
    padding: 10px;
    overflow-y: scroll;
  }
</style>
