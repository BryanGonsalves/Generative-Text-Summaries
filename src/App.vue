<template>
  <h1>Summarizer</h1>
  <p>Welcome to Summarizer! Insert your text below to get it summarized.</p>
  <form id="ruleForm">
      <textarea v-model="input" form="ruleForm" rows="20" cols="40" placeholder="Provide the text here"></textarea>
      <br/>
      <button style="margin-top: 0.5rem;" v-on:click.prevent="clear">Clear</button>
  </form>
</template>

<script>
export default {
  name: 'App',
  data() {
      return {
          input: ""
      }
  },
  methods: {
      clear() {
          this.input = ""
      },
  }
}
</script>