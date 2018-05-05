<template>
    <!-- CommentModal -->
    <div class="modal fade" id="CommentModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">登录</h4>
            </div>
            <div class="modal-body">
                <!-- 模态框中评论内容 -->
                <div id="comment">
                    <comment-content v-bind:comment="comment" v-on:change="changCommmer"></comment-content>
                    <comment-textarea v-bind:type="type" v-bind:name="oldComment" v-on:submit="addComment" v-on:canel="canelCommit"></comment-textarea>
                </div>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import commentContent from './comment-content.vue'
import commentTextarea from './comment-textarea.vue'

export default {
  components:{
      commentContent,commentTextarea
  },
  data(){ 
      return {
        commenter: "session",   //评论人，这里会从session拿
        type: 0,                //0为评论作者1为评论别人的评论
        oldComment: null,       //久评论者的名字
        chosedIndex: -1,        //被选中的评论的index
        article: {
            title: "当归泡水喝的九大功效",
            time: "2016-07-12",
            read:50,
            content: ""
        },
        comment: []   //评论内容
      }
    },
    methods: {
        //格式化时间
        getTime() {
            var now = new Date();
            var year = now.getFullYear();
            var month = now.getMonth()+1;
            var day = now.getDate();
            month.length < 2 ?  "0" + month : month;
            day.length < 2 ?  "0" + day : day;
            return year+"-"+month+"-"+day;
        },
        //添加评论
        addComment: function(data) {
            if(this.type == 0) {
                this.comment.push({
                    name: 'session',
                    time: this.getTime(),
                    content: data,
                    reply: []
                });
                //服务器端,待定
            }else if(this.type == 1){
                this.comment[this.chosedIndex].reply.push({
                    responder: 'session',
                    reviewers:this.comment[this.chosedIndex].name,
                    time: this.getTime(),
                    content: data
                });
                this.type = 0;
            }
        },
        //监听到了点击了别人的评论
        changCommmer: function(name,index) {
            this.oldComment = name;
            this.chosedIndex = index;
            this.type = 1;
        },
        //监听到了取消评论
        canelCommit: function() {
            this.type = 0;
        }
    }
}
</script>
