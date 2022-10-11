const url = "http://localhost:8000/tweets/";
const { createApp } = Vue;

createApp({
  data() {
    return {
      tweets: [""],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get(url);
        this.tweets = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async newTweet() {
      try {
        const response = await axios.post(url, {
          author: this.name,
          content: this.content,
        });
        this.tweets.unshift(response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tweets on page load
    this.getData();
  },
}).mount("#app");
