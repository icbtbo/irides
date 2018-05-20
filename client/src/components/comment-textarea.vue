<template>
  <div class="commentBox">
	    <div class="title">
			<h3>发表评论</h3>
	    </div>
		<div class="form-group">
			<label v-if="type" for="comment_text">你回复&nbsp;{{name}}</label>
			<textarea id="comment_text" value="请填写评论内容" v-model="commentText" class="form-control"></textarea>
		</div>
		<button class="btn" @click="addComment">发表</button>
		<button class="btn" @click="canelComment">取消</button>
	</div>
</template>

<script>
export default {
  props: ['type','name'],
	data: function(){
		return {commentText:""}
	},
	methods: {
		addComment: function() {
			this.$emit("submit",this.commentText);
			this.commentText = "";
		},
		canelComment: function() {
			this.$emit("canel");
			this.commentText = "";
		}
	}
}
</script>
<style>
.commentBox h3{
	position: relative;
	font-size: 15px;
	top: 7px;
	left: 7px;
}
.title{
	width: 100%;
	height: 29px;
	background-color: #DDDDDD;
}
</style>
