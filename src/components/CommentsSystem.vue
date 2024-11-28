<template>
    <div class="container justify-content-center mt-5 border-left border-right">
        <!-- Render statuses dynamically -->
        <div v-for="(status, index) in statuses" :key="index" class="d-flex flex-column py-2">
            <div class="second py-2 px-2">
                <p><strong>Trạng thái:</strong> {{ status.text }}</p>
                <div v-if="status.image">
                    <img :src="status.image" alt="Uploaded Image" class="img-fluid mt-2" />
                </div>
                
                <!-- Comment Input for each post -->
                <div class="d-flex justify-content-center pt-3 pb-2">
                    <input
                        v-model="status.newComment"
                        @keyup.enter="addComment(status)"
                        placeholder="+ Vui lòng nhập câu bình luận"
                        class="form-control addtxt"
                    />
                </div>

                <!-- Render comments dynamically for each status -->
                <div v-for="(comment, commentIndex) in status.comments" :key="commentIndex" class="d-flex justify-content-center py-2">
                    <div class="second py-2 px-2">
                        <span class="text1">{{ comment.text }}</span>
                    </div>
                </div>
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
                    image: "https://scontent.fhan11-1.fna.fbcdn.net/v/t39.30808-6/421145065_2388711054670515_2749220410013483800_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=105&ccb=1-7&_nc_sid=2285d6&_nc_ohc=E5M6mQx2RH8Q7kNvgGlqZIU&_nc_zt=23&_nc_ht=scontent.fhan11-1.fna&_nc_gid=Ad6IMLSt2BmVHKz7HA8_Qc8&oh=00_AYD9xRuTAudKW6B5Ge6Il1s_CxzxBnLIyNhBMZtb_vswBg&oe=674E232E", // Replace with actual image URL
                    comments: [],  // Array for comments specific to this post
                    newComment: "",  // New comment text for this post
                    is_post: true,
                },
                {
                    text: "This is the second post. Share your thoughts in the comments.",
                    image: "https://scontent.fhan11-1.fna.fbcdn.net/v/t39.30808-6/464264762_1043515390806199_4841784333295455722_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=aa7b47&_nc_ohc=7KpMHo73M48Q7kNvgGA9yXM&_nc_zt=23&_nc_ht=scontent.fhan11-1.fna&_nc_gid=AMpttSKJDS4ifE8C5xdHe0c&oh=00_AYDwjou2ZCp5EVoUIvjj6mP_xSgB5RWa0cxlbEbuV_sdNg&oe=674E10E8", // Replace with actual image URL
                    comments: [],  // Array for comments specific to this post
                    newComment: "",  // New comment text for this post
                    is_post: true,
                }
            ],
        };
    },
    methods: {
        // Add comment for a specific status
        addComment(status) {  // Removed the 'index' parameter
            const newCommentText = status.newComment.trim();
            if (newCommentText !== "") {
                const newComment = {
                    text: newCommentText,
                    author: "Anonymous",
                    avatar: "https://i.imgur.com/tPvlEdq.jpg",
                    upvotes: "",
                    translatedText: "",
                    prediction: "",
                    classificationTime: "",
                    translationTime: "",
                    classification: "",  
                    probability: "",
                    is_post: false,
                };

                // Add comment locally to the corresponding status
                status.comments.unshift(newComment);

                // Send comment to Python backend
                axios
                    .post("http://127.0.0.1:5000/add_comment", { text: newCommentText })  // Only send text
                    .then((response) => {
                        const { translated_text, prediction, probability, translation_time, classification_time } = response.data;

                        // Log the response to console
                        console.log(`New Comment Received: ${newCommentText}`);
                        console.log(`Translated Text: ${translated_text}`);
                        console.log(`Prediction Result: ${prediction}`);
                        console.log(`Classification Probability: ${probability}`);
                        console.log(`Translation Time: ${translation_time} seconds`);
                        console.log(`Classification Time: ${classification_time} seconds`);

                        // Now, update the comment in the array with backend data
                        const updatedComment = {
                            ...newComment,  // Keep the original data
                            translatedText: translated_text,
                            prediction: prediction,
                            probability: probability,  // Store the probability
                            translationTime: translation_time,
                            classificationTime: classification_time,
                            classification: prediction === 0 ? "Tích cực" : "Tiêu cực",
                        };

                        // Directly update the comment in the array
                        status.comments[0] = updatedComment;  // Update the first comment (index 0)

                        console.log("Comment processed successfully:", response.data);
                    })
                    .catch((error) => {
                        console.error("Error sending comment:", error);
                    });

                status.newComment = ""; // Clear the input field for this status
            }
        },
    },
};
</script>

<style lang="css" scoped>
.img-fluid{
    width: 60%;
    
}
body{
	background-color: #fff;
}
.container{
	background-color: #eef2f5;
	width: 100%;
}
.addtxt{
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

.second{
	width: 100%;
	background-color: white;
	border-radius: 4px;
	box-shadow: 10px 10px 5px #aaaaaa;
}
.text1{
	font-size: 13px;
    font-weight: 500;
    color: #56575b;
}
.text2{
	font-size: 13px;
    font-weight: 500;
    margin-left: 6px;
    color: #56575b;
}
.text3{
	font-size: 20px;
    font-weight: bold;
    margin-right: 4px;
    color: #828386;
}
.text3o{
	color: #00a5f4;

}
.text4{
	font-size: 13px;
    font-weight: 500;
    color: #828386;
}
.text4i{
	color: #00a5f4;
}
.text4o{
	color: white;
}
.thumbup{
	font-size: 13px;
    font-weight: 500;
    margin-right: 5px;
}
.thumbupo{
	color: #17a2b8;
}
</style>