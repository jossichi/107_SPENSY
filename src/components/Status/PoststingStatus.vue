<template>
    <div class="container mt-5 mb-5">
      <div class="row d-flex align-items-center justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <!-- Post Header -->
            <div class="d-flex justify-content-between p-2 px-3">
              <div class="d-flex flex-row align-items-center">
                <img :src="post.author.avatar" width="50" class="rounded-circle" />
                <div class="d-flex flex-column ml-2">
                  <span class="font-weight-bold">{{ post.author.name }}</span>
                  <small class="text-primary">{{ post.author.relationship }}</small>
                </div>
              </div>
              <div class="d-flex flex-row mt-1 ellipsis">
                <small class="mr-2">{{ post.time }}</small>
                <i class="fa fa-ellipsis-h"></i>
              </div>
            </div>
            <!-- Post Content -->
            <img :src="post.image" class="img-fluid" />
            <div class="p-2">
              <p class="text-justify">{{ post.content }}</p>
              <hr />
              <!-- Post Actions -->
              <div class="d-flex justify-content-between align-items-center">
                <div class="d-flex flex-row icons d-flex align-items-center">
                  <i class="fa fa-heart" @click="likePost"></i>
                  <i class="fa fa-smile-o ml-2"></i>
                </div>
                <div class="d-flex flex-row muted-color">
                  <span>{{ post.comments.length }} comments</span>
                  <span class="ml-2">Share</span>
                </div>
              </div>
              <hr />
              <!-- Comments Section -->
              <div class="comments">
                <div v-for="(comment, index) in post.comments" :key="index" class="d-flex flex-row mb-2">
                  <img :src="comment.avatar" width="40" class="rounded-image" />
                  <div class="d-flex flex-column ml-2">
                    <span class="name">{{ comment.name }}</span>
                    <small class="comment-text">{{ comment.text }}</small>
                    <div class="d-flex flex-row align-items-center status">
                      <small>Like</small>
                      <small>Reply</small>
                      <small>Translate</small>
                      <small>{{ comment.time }}</small>
                    </div>
                  </div>
                </div>
                <!-- Add Comment -->
                <div class="comment-input">
                  <input
                    v-model="newComment"
                    type="text"
                    class="form-control"
                    placeholder="Add a comment..."
                    @keyup.enter="addComment"
                  />
                  <div class="fonts">
                    <i class="fa fa-camera"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      post: {
        author: {
          name: "Jeanette Sun",
          avatar: "https://i.imgur.com/UXdKE3o.jpg",
          relationship: "Colleagues",
        },
        time: "20 mins",
        image: "https://i.imgur.com/xhzhaGA.jpg",
        content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.",
        comments: [
          {
            name: "Daniel Frozer",
            avatar: "https://i.imgur.com/9AZ2QX1.jpg",
            text: "I like this a lot! Thanks a lot.",
            time: "18 mins",
          },
          {
            name: "Elizabeth Goodman",
            avatar: "https://i.imgur.com/1YrCKa1.jpg",
            text: "Thanks for sharing!",
            time: "8 mins",
          },
        ],
      },
      newComment: "",
    };
  },
  methods: {
    likePost() {
      alert("You liked the post!");
    },
    addComment() {
      if (this.newComment.trim() !== "") {
        this.post.comments.push({
          name: "You",
          avatar: "https://i.imgur.com/placeholder.jpg", // Placeholder for user's avatar
          text: this.newComment.trim(),
          time: "Just now",
        });
        this.newComment = "";
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800&display=swap");
body {
  background-color: #eee;
  font-family: "Poppins", sans-serif;
  font-weight: 300;
}
.card {
  border: none;
}
.ellipsis {
  color: #a09c9c;
}
hr {
  color: #a09c9c;
  margin-top: 4px;
  margin-bottom: 8px;
}
.muted-color {
  color: #a09c9c;
  font-size: 13px;
}
.ellipsis i {
  margin-top: 3px;
  cursor: pointer;
}
.icons i {
  font-size: 25px;
  cursor: pointer;
}
.icons .fa-heart {
  color: red;
}
.icons .fa-smile-o {
  color: yellow;
  font-size: 29px;
}
.rounded-image {
  border-radius: 50% !important;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  width: 50px;
}
.name {
  font-weight: 600;
}
.comment-text {
  font-size: 12px;
}
.status small {
  margin-right: 10px;
  color: blue;
  cursor: pointer;
}
.form-control {
  border-radius: 26px;
}
.comment-input {
  position: relative;
}
.fonts {
  position: absolute;
  right: 13px;
  top: 8px;
  color: #a09c9c;
}
.form-control:focus {
  color: #495057;
  background-color: #fff;
  border-color: #8bbafe;
  outline: 0;
  box-shadow: none;
}
</style>
