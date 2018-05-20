<template lang="pug">
<div id="main">
  <Header @pics="showpics"/>
  <LoginModel />
  <RegModel />
  <Uploadpic />
  <CommentMod />
  #app
    vue-waterfall-easy(:imgsArr="imgsArr",@scrollLoadImg="fetchImgsData")
      template( scope="props")
        p.some-info 第{{props.index+1}}张图片
        p.some-info {{props.value.tags}}
        p.some-info {{props.value.info}}
        //- button.comment(data-toggle="modal" data-target="#LoginModal" :data-picid="props.index+1") 评论
</div>
</template>

<script>
var ItemFactory = (function () {

  var lastIndex = 0

  function generateRandomItems (count) {
    var items = [], i, aitems = []
    $.ajax({
      async: false,
      type: 'GET',
      url: 'http://127.0.0.1:5000/api/pictures?number=' + count,
      dataType: 'json',
      success:function(res){
        console.log('success');
        aitems = res.data;
        console.log(aitems);
      },
      error:function(){
        console.log('error');
      }
    });
    for (i = 0; i < aitems.length; i++) {
      items[i] = {
        picid: aitems[i].id,
        src: aitems[i].address,
        tags: aitems[i].tags.join(' '),
        info: aitems[i].dsepriction
      }
      
    }
    return items
  }
  return {
    get: generateRandomItems
  }

})();
import vueWaterfallEasy from '../components/vue-waterfall-easy.vue'
import LoginModel from '../components/LoginModel.vue'
import RegModel from '../components/RegModel.vue'
import Uploadpic from '../components/Uploadpic.vue'
import Header from '../components/Header.vue'
import CommentMod from '../components/CommentMod.vue'
export default {
  name: 'app',
  data() {
    return {
      imgsArr: []
    }
  },
  components: {
    vueWaterfallEasy,Header,LoginModel,RegModel,Uploadpic,CommentMod
  },
  methods: {
    showpics: function(data){
      if(data.length == 0)
        alert('搜索不到相关图片！')
      this.imgsArr = data;
    },     
    fetchImgsData() {
      this.imgsArr = this.imgsArr.concat(ItemFactory.get(this.imgsArr.length))
      // this.imgsArr.push.apply(this.imgsArr, this.fetchImgsArr)
    }
  },
  created() {
    this.imgsArr = ItemFactory.get(0)
  },
}
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
html,
body,
#app {
  top: 50px;
  // height: 100%;
}
#app {
  font-family: microsoft yahei;
  overflow: auto;
  .some-info {
    line-height: 1.6;
    text-align: center;
  }
  .comment{
    text-align: center;
    width: 100%;
  }
}
</style>