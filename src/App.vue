<template>
  <h1>Summarizer</h1>
  <p>Welcome to Summarizer! Insert your text below to get it summarized.</p>
  <form id="ruleForm">
    <textarea
      v-model="input"
      form="ruleForm"
      rows="15"
      cols="40"
      placeholder="Provide the text here"
    ></textarea>
    <br />
    <button style="margin: 1rem 1rem 0 0" v-on:click.prevent="createSummary">
      Create Summary
    </button>
    <button v-on:click.prevent="clear">Clear</button>
    <p>{{ output }}</p>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      input: "",
      output: "",
    };
  },
  methods: {
    clear() {
      this.input = "";
      this.output = "";
    },
    async createSummary() {
      let data = {
        text: this.input,
      };
      try {
        let response = await axios.post(
          window.location.href + "summary",
          data
        );
        this.output = response.data;
      } catch (error) {
        this.output = error;
      }
    },
  },
};
</script>