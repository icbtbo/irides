<template>
  <div class="commentBox">
        <div class="title">
			<h3>所有评论</h3>
	    </div>
        <p v-if="comment.length==0">暂无评论，我来发表第一篇评论！</p>
        <div v-else>
            <div class="comment" v-for="(item,index) in comment" v-bind:index="index" >
                <b>{{item.name}}<span>{{item.time}}</span></b>
                <p @click="changeCommenter(item.name,item.id,index)">{{item.content}}</p>
                <div v-if="item.reply.length > 0">
                    <div class="reply" v-for="reply in item.reply">
                        <b>{{reply.responder}}&nbsp;&nbsp;回复&nbsp;&nbsp;{{reply.reviewers}}<span>{{reply.time}}</span></b>
                        <p @click="changeCommenter(reply.responder,reply.id,index)">{{reply.content}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name:'comment-content',
  props:['comment'],
  methods: {
    changeCommenter: function(name,id,index) {
        this.$emit("change",name,id,index);
    }
  }
}
</script>

<style>
.reply{
    position: relative;
    left: 45px;
}
.comment b, .reply b{
    color: darkgreen;
}
.comment span, .reply span{
    color:black;
}
</style>
