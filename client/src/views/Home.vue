<template>
    <div>
        <Model />
        <Header />
        <el-container>
          <el-main>
          </el-main>
        </el-container>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import Model from "../components/Model.vue";
import alert from 'vue-strap/src/alert';
export default {
  components: { Header, alert, Model},
  data: function() {
    return {};
  }
};
</script>

<style scoped>
.el-header {
  /* border: 1px solid blue; */
}
.el-main {
  /* border: 1px solid red; */
}
</style>