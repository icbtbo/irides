<template>
    <div>
        <LoginModel />
        <RegModel />
        <Uploadpic />
        <Header v-on:pics="showpics" />
        <div id="main">
          <waterfall
          :align="align"
          :line-gap="200"
          :min-line-gap="100"
          :max-line-gap="220"
          :single-max-width="300"
          :watch="items"
          @reflowed="reflowed"
          ref="waterfall"
        >
          <!-- each component is wrapped by a waterfall slot -->
          <waterfall-slot
            v-for="(item, index) in items"
            :width="item.width"
            :height="item.height"
            :order="index"
            :key="item.index"
            move-class="item-move"
          >
            <!-- <div class="item" :style="item.style" :index="item.index"></div> -->
            <div class="pic">
              <img :src="item.src" />
            </div>
          </waterfall-slot>
        </waterfall>
        </div>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import LoginModel from "../components/LoginModel.vue";
import RegModel from "../components/RegModel.vue";
import Uploadpic from "../components/Uploadpic.vue";
import Waterfall from 'vue-waterfall/lib/waterfall'
import WaterfallSlot from 'vue-waterfall/lib/waterfall-slot'
import alert from 'vue-strap/src/alert';
var ItemFactory = (function () {

  var lastIndex = 0

  function generateRandomItems (count) {
    var items = [], i, aitems = []
    $.ajax({
      async: false,
      type: 'GET',
      url: 'http://127.0.0.1:5000/api/pictures?number=' + lastIndex,
      dataType: 'json',
      success:function(res){
        console.log('success');
        aitems = res.data;
        // console.log(aitems);
      },
      error:function(){
        console.log('error');
      }
    });
    for (i = 0; i < aitems.length; i++) {
      items[i] = {
        src: aitems[i].address,
        index: lastIndex++,
        width: 100 + ~~(Math.random() * 50),
        height: 100 + ~~(Math.random() * 50)
      }
    }
    return items
  }

  // function getRandomColor () {
  //   var colors = [
  //     'rgba(21,174,103,.5)',
  //     'rgba(245,163,59,.5)',
  //     'rgba(255,230,135,.5)',
  //     'rgba(194,217,78,.5)',
  //     'rgba(195,123,177,.5)',
  //     'rgba(125,205,244,.5)'
  //   ]
  //   return colors[~~(Math.random() * colors.length)]
  // }

  return {
    get: generateRandomItems
  }

})();
export default {
  components: { Header, alert, LoginModel, RegModel,Uploadpic,Waterfall,WaterfallSlot},
  data: function() {
    return {
      align: 'center',
      items: ItemFactory.get(50),
      isBusy: false
    };
  },
  methods: {
              addItems: function () {
                if (!this.isBusy && this.items.length < 500) {
                  this.isBusy = true
                  this.items.push.apply(this.items, ItemFactory.get(50))
                }
              },
              shuffle: function () {
                this.items.sort(function () {
                  return Math.random() - 0.5
                })
              },
              reflowed: function () {
                this.isBusy = false
              },
              showpics: function(data){
                console.log(data)
                this.items = data
              }
  },
  mounted(){
    var that = this;
          document.getElementById("main").addEventListener('click', function () {
            // console.log(that.items)
            that.shuffle()
            // app.$refs.waterfall.$emit('reflow') // manually trigger reflow action
          }, false)
          window.addEventListener('scroll', function () {
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop
            if (scrollTop + window.innerHeight >= document.body.clientHeight) {
              that.addItems()
            }
          })
  }
};
</script>

<style>
body {
  margin: 5px;
  font-family: Helvetica, sans-serif;
}
#main{
	position: relative;
	top: 50px;
}
img{
  height: 100%; width: 100%; object-fit: fill; 
}
.pic{
  height: 100%; width: 100%;
  padding: 10px;
	border: 1px solid #ccc;
	border-radius: 5px;
	box-shadow: 0 0 5px #ccc;

}
.vue-waterfall-slot{
  padding: 15px 0 0 15px !important;
}
/* .item {
  position: absolute;
  top: 5px;
  left: 5px;
  right: 5px;
  bottom: 5px;
  font-size: 1.2em;
  color: rgb(0,158,107);
}
.item:after {
  content: attr(index);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
} */
.wf-transition {
  transition: opacity .3s ease;
  -webkit-transition: opacity .3s ease;
}
.wf-enter {
  opacity: 0;
}
      .item-move {
        transition: all .5s cubic-bezier(.55,0,.1,1);
        -webkit-transition: all .5s cubic-bezier(.55,0,.1,1);
      }
</style>