<template>
  <h1>Summarizer</h1>
  <p>Welcome to Summarizer! Insert your text below to get it summarized.</p>
  <form id="ruleForm">
      <textarea v-model="input" form="ruleForm" rows="20" cols="40" placeholder="Provide the text here"></textarea>
      <br/>
      <button style="margin: 0.5rem 0.5rem 0 0;" v-on:click.prevent="createSummary">Create Summary</button>
      <button v-on:click.prevent="clear">Clear</button>
  </form>
  <p>{{ output }}</p>
</template>

<script>
export default {
  name: 'App',
  data() {
      return {
          input: "",
          output: ""
      }
  },
  methods: {
      clear() {
          this.input = "",
          this.output = ""
      },
      createSummary() {
          this.output = this.input
      }
  }
}
</script>