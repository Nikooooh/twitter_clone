document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/tweets/")
    .then((response) => response.json())
    .then((data) => {
      const feed = document.getElementById("feed");
      data.forEach((tweet) => {
        const tweetElement = document.createElement("div");
        tweetElement.textContent = tweet.content;
        feed.appendChild(tweetElement);
      });
    });
});
