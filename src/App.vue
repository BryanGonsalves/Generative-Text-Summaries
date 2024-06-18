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
    <label for="persona">Persona </label>
    <input
      type="text"
      style="margin: 1rem 0 1rem 0"
      placeholder="Enter a persona"
      id="persona"
      v-model="persona"
    />
    <br />
    <label for="selectWordCount">Word Limit </label>
    <select v-model="wordCount" id="selectWordCount">
      <option value="50">50</option>
      <option value="100">100</option>
      <option value="150">150</option>
    </select>
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
      wordCount: "50",
      persona: "Human",
    };
  },
  methods: {
    clear() {
      this.input = "";
      this.output = "";
      this.wordCount = "50";
      this.persona = "Human";
    },
    async createSummary() {
      let data = {
        text: this.input,
        wordCount: Number(this.wordCount),
        persona: this.persona,
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