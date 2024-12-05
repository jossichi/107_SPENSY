<template>
  <div class="container justify-content-center mt-5 border-left border-right">
    <!-- Render statuses dynamically -->
    <div
      v-for="(status, index) in statuses"
      :key="index"
      class="d-flex flex-column py-2">
      <div class="second py-2 px-2">
        <p><strong>Trạng thái:</strong> {{ status.text }}</p>
        <div v-if="status.image">
          <img
            :src="status.image"
            alt="Uploaded Image"
            class="img-fluid mt-2" />
        </div>

        <!-- Comment Input for each post -->
        <div class="d-flex justify-content-center pt-3 pb-2">
          <input
            v-model="status.newComment"
            @keyup.enter="addComment(status)"
            placeholder="+ Vui lòng nhập câu bình luận"
            class="form-control addtxt" />
        </div>
        <div class="container mt-5">
          <div class="row d-flex justify-content-center">
            <div class="col-md-8">
              <div
                v-for="(comment, commentIndex) in status.comments"
                :key="commentIndex"
                class="d-flex justify-content-center py-2">
                <div class="second py-2 px-2">
                  <span>
                    <small class="font-weight-bold text-primary">{{
                      comment.author
                    }}</small
                    ><br />
                    <small class="font-weight-bold">{{ comment.text }}</small>
                  </span>
                </div>
                <small>{{ calculateTimeAgo(comment.timestamp) }}</small>
              </div>
              <div class="card p-3">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="user d-flex flex-row align-items-center">
                    <img
                      src="https://i.imgur.com/hczKIze.jpg"
                      width="30"
                      class="user-img rounded-circle mr-2" />
                    <span
                      ><small class="font-weight-bold text-primary"
                        >User-014</small
                      ><br />
                      <small class="font-weight-bold"
                        >Hmm, This poster looks cool</small
                      ></span
                    >
                  </div>

                  <small>2 days ago</small>
                </div>
              </div>

              <div class="card p-3 mt-2">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="user d-flex flex-row align-items-center">
                    <img
                      src="https://i.imgur.com/C4egmYM.jpg"
                      width="30"
                      class="user-img rounded-circle mr-2" />
                    <span
                      ><small class="font-weight-bold text-primary"
                        >User-422</small
                      ><br />
                      <small class="font-weight-bold"
                        >Loving your work and profile!
                      </small></span
                    >
                  </div>

                  <small>3 days ago</small>
                </div>

                <div
                  class="action d-flex justify-content-between mt-2 align-items-center">
                  <div class="icons align-items-center">
                    <i class="fa fa-check-circle-o check-icon text-primary"></i>
                  </div>
                </div>
              </div>

              <div class="card p-3 mt-2">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="user d-flex flex-row align-items-center">
                    <img
                      src="https://i.imgur.com/0LKZQYM.jpg"
                      width="30"
                      class="user-img rounded-circle mr-2" />
                    <span
                      ><small class="font-weight-bold text-primary"
                        >User-763</small
                      >
                      <small class="font-weight-bold"
                        ><br />Really cool Which filter are you using?
                      </small></span
                    >
                  </div>

                  <small>3 days ago</small>
                </div>
              </div>

              <div class="card p-3 mt-2">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="user d-flex flex-row align-items-center">
                    <img
                      src="https://i.imgur.com/ZSkeqnd.jpg"
                      width="30"
                      class="user-img rounded-circle mr-2" />
                    <span
                      ><small class="font-weight-bold text-primary"
                        >User-259</small
                      >

                      <small class="font-weight-bold"
                        ><br />Thanks
                      </small></span
                    >
                  </div>

                  <small>3 days ago</small>
                </div>

                <div
                  class="action d-flex justify-content-between mt-2 align-items-center">
                  <div class="icons align-items-center">
                    <i class="fa fa-check-circle-o check-icon text-primary"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Render comments dynamically for each status -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      statuses: [
        {
          text: "This is the first post. Feel free to leave a comment!",
          image:
            "https://scontent.fhan11-1.fna.fbcdn.net/v/t39.30808-6/421145065_2388711054670515_2749220410013483800_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=105&ccb=1-7&_nc_sid=2285d6&_nc_ohc=E5M6mQx2RH8Q7kNvgGlqZIU&_nc_zt=23&_nc_ht=scontent.fhan11-1.fna&_nc_gid=Ad6IMLSt2BmVHKz7HA8_Qc8&oh=00_AYD9xRuTAudKW6B5Ge6Il1s_CxzxBnLIyNhBMZtb_vswBg&oe=674E232E",
          comments: [],
          newComment: "",
        },
        {
          text: "This is the second post. Share your thoughts in the comments.",
          image:
            "https://scontent.fhan11-1.fna.fbcdn.net/v/t39.30808-6/464264762_1043515390806199_4841784333295455722_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=aa7b47&_nc_ohc=7KpMHo73M48Q7kNvgGA9yXM&_nc_zt=23&_nc_ht=scontent.fhan11-1.fna&_nc_gid=AMpttSKJDS4ifE8C5xdHe0c&oh=00_AYDwjou2ZCp5EVoUIvjj6mP_xSgB5RWa0cxlbEbuV_sdNg&oe=674E10E8",
          comments: [],
          newComment: "",
        },
      ],
    };
  },
  methods: {
    // Calculate the time ago for a given timestamp
    calculateTimeAgo(timestamp) {
      if (!timestamp) return "Không xác định"; // Handle undefined or invalid timestamps

      const now = new Date();
      const time = new Date(timestamp);

      if (isNaN(time.getTime())) return "Không xác định"; // Return "Không xác định" if invalid

      const diff = Math.floor((now - time) / 1000); // Difference in seconds

      if (diff < 60) return `${diff} giây trước`;
      if (diff < 3600) return `${Math.floor(diff / 60)} phút trước`;
      if (diff < 86400) return `${Math.floor(diff / 3600)} giờ trước`;
      return `${Math.floor(diff / 86400)} ngày trước`;
    },

    addComment(status) {
      const newCommentText = status.newComment.trim();
      if (!newCommentText) return;

      const newComment = {
        text: newCommentText,
        author: "Processing...", // Placeholder for the author
        avatar: "https://i.imgur.com/tPvlEdq.jpg",
        translatedText: "",
        classification: "",
        timestamp: new Date(), // Adding timestamp here
      };

      // Add the comment locally
      status.comments.unshift(newComment);

      axios
        .post("http://127.0.0.1:5000/add_comment", { text: newCommentText })
        .then((response) => {
          const {
            translated_text,
            prediction,
            probability,
            translation_time,
            classification_time,
            user_id,
          } = response.data;

          // Update the comment with backend data
          Object.assign(newComment, {
            author: `${user_id}`,
            translatedText: translated_text,
            classification: prediction === 0 ? "Tích cực" : "Tiêu cực",
            probability: (probability * 100).toFixed(2),
            translationTime: translation_time,
            classificationTime: classification_time,
          });

          console.log("Comment processed:", response.data);
        })
        .catch((error) => {
          console.error("Error processing comment:", error);
          newComment.author = "Error retrieving User ID"; // In case of error
        });

      status.newComment = ""; // Clear the input field
    },
  },
};
</script>
<style lang="css" scoped>
.img-fluid {
  width: 60%;
}
body {
  background-color: #fff;
}
.container {
  background-color: #eef2f5;
  width: 100%;
}
.addtxt {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 13px;
  width: 100%;
  background-color: #e5e8ed;
  font-weight: 500;
}
.form-control:focus {
  color: #000;
}

.second {
  width: 100%;
  background-color: white;
  border-radius: 4px;
  box-shadow: 10px 10px 5px #aaaaaa;
}
.text1 {
  font-size: 13px;
  font-weight: 500;
  color: #56575b;
}
.text2 {
  font-size: 13px;
  font-weight: 500;
  margin-left: 6px;
  color: #56575b;
}
.text3 {
  font-size: 20px;
  font-weight: bold;
  margin-right: 4px;
  color: #828386;
}
.text3o {
  color: #00a5f4;
}
.text4 {
  font-size: 13px;
  font-weight: 500;
  color: #828386;
}
.text4i {
  color: #00a5f4;
}
.text4o {
  color: white;
}
.thumbup {
  font-size: 13px;
  font-weight: 500;
  margin-right: 5px;
}
.thumbupo {
  color: #17a2b8;
}
</style>
