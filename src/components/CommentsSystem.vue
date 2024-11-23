<template>
    <div class="container justify-content-center mt-5 border-left border-right">
        <!-- Input field for new comments -->
        <div class="d-flex justify-content-center pt-3 pb-2">
            <input
                type="text"
                v-model="newComment"
                @keyup.enter="addComment"
                placeholder="+ Vui lòng nhập câu bình luận"
                class="form-control addtxt"
            />
        </div>
        
        <!-- Render comments dynamically -->
        <div class="d-flex justify-content-center py-2" v-for="(comment, index) in comments" :key="index">
            <div class="second py-2 px-2">
                <span class="text1">{{ comment.text }}</span>
                <div class="d-flex justify-content-between py-1 pt-2">
                    <div>
                        <img :src="comment.avatar" width="18" height="18">
                        <span class="text2">{{ comment.author }}</span>
                    </div>
                    <div>
                        <span class="text3">{{ comment.classification }}</span>  <!-- Classification result -->
                    </div>
                </div>

                <div v-if="comment.isLoading">
                    <p>Loading...</p>  
                </div>
                
                <!-- Display translation and classification results after backend response -->
                <div v-if="!comment.isLoading && comment.translatedText">
                    <p><strong>Câu văn đã dịch:</strong> {{ comment.translatedText }}</p>
                    <p><strong>Kết quả và xác suất phân loại:</strong> {{ comment.prediction }}</p>
                    
                    <p><strong>Thời gian dịch:</strong> {{ comment.translationTime }} seconds</p>
                    <p><strong>Thời gian phân loại:</strong> {{ comment.classificationTime }} seconds</p>
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
            newComment: "",
            comments: [],
        };
    },
    methods: {
        addComment() {
            if (this.newComment.trim() !== "") {
                const newComment = {
                    text: this.newComment,
                    author: "Anonymous",
                    avatar: "https://i.imgur.com/tPvlEdq.jpg",
                    upvotes: "",
                    translatedText: "",
                    prediction: "",
                    classificationTime: "",
                    translationTime: "",
                    classification: "",  // Add a new field to store classification label
                    probability: "",  // Add a new field to store classification probability
                };

                // Add comment locally
                this.comments.unshift(newComment);

                // Send comment to Python backend
                axios
                    .post("http://127.0.0.1:5000/add_comment", { text: this.newComment })  // Only send text
                    .then((response) => {
                        const { translated_text, prediction, probability, translation_time, classification_time } = response.data;

                        // Log the response to console
                        console.log(`New Comment Received: ${this.newComment}`);
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
                        this.comments[0] = updatedComment;  // Update the first comment (index 0)

                        console.log("Comment processed successfully:", response.data);
                    })
                    .catch((error) => {
                        console.error("Error sending comment:", error);
                    });

                this.newComment = ""; // Clear the input field
            }
        },
    },
};
</script>


<style lang="css" scoped>
body{
	background-color: #fff;
}
.container{
	background-color: #eef2f5;
	width: 100vw;
}
.addtxt{
	padding-top: 10px;
	padding-bottom: 10px;
	text-align: center;
	font-size: 13px;
	width: 100vw;
	background-color: #e5e8ed;
	font-weight: 500;
}
.form-control:focus {
    color: #000;
}

.second{
	width: 100vw;
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