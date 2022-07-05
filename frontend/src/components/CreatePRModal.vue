<template>
  <v-card light color="#BDD6D0" class="create-pr-card">
    <v-card-title>
      Create Pull Request
      <v-spacer></v-spacer>
      <v-btn color="#fda855" fab x-small @click=closeModal>
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-text class="white text--primary">
      <v-text-field
          v-model="title"
          label="Title"
          outlined
          single-line>
      </v-text-field>
      <v-text-field
          v-model="branch"
          label="branch"
          outlined
          single-line>
      </v-text-field>
      <v-textarea
          v-model="body"
          label="Body"
          outlined
      >
      </v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="#fda855" @click=createPullRequest>Create Pull Request</v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
import {create_pull_request} from "@/helpers/Services";

export default {
  name: "CreatePRModal.vue",
  data () {
    return {
      title: '',
      body: '',
      branch: '',
    }
  },
  methods:{
    closeModal(){
      this.$emit("showCreatePR",false)
    },
    createPullRequest(){
      create_pull_request(this.title,this.body,this.branch)
      this.closeModal()
    },
  },
}
</script>

<style scoped>
  .create-pr-card {
    min-width: 600px;
  }
</style>
