<template>
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
	<div class="container-fluid"> 
        <div class="navbar-header">
            <a class="navbar-brand title" href="#">irides</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"> 
    		<ul class="nav navbar-nav">
                <form class="navbar-form navbar-left">
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search">
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a data-toggle="modal" href="#UploadpicModal">上传图片</a></li>
                <li v-if="Islogin1 == true" class="dropdown navbar-right">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        {{username}}
                        <b class="caret"></b>
                    </a>
                    <ul class="dropdown-menu">
                        <!-- <li><a href="#">login</a></li> -->
                        <li @click="logout"><a href="#">logout</a></li>
                    </ul>
                </li>
                <li v-if="Islogin1 == false"><a data-toggle="modal" href="#LoginModal">登陆</a></li>
                <li v-if="Islogin2 == false"><a data-toggle="modal" href="#RegModal">注册</a></li>
                <!-- <li class="dropdown navbar-right">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        account
                        <b class="caret"></b>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="#">login</a></li>
                        <li><a href="#">logout</a></li>
                    </ul>
                </li> -->
            </ul>
        </div>
	</div>
</nav>
    <!-- <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=上传>
    </form> -->
</template>

<script>
export default {
  data() {
    return {
        username:'',
        Islogin1: false,
        Islogin2: false
    }
  },
  methods:{  
      logout:function(){
          this.username = '';
          this.Islogin1 = false;
          this.Islogin2 = false;
          $.cookie('token', null);
      }   
  },
  mounted(){
                          console.log(this.username);
                    console.log(this.Islogin1);
        var that = this;
        if($.cookie('token') != null){
            $.ajax({
                async: false,
                type: 'GET',
                url: 'http://127.0.0.1:5000/api/user',
                dataType: 'json',
                // contentType: "application/json",
                headers:{
                'Authorization':'Bearer' + ' ' + $.cookie('token')
                },
                success:function(res){
                    console.log('success');
                    // console.log(res);
                    that.username = res.username;
                    that.Islogin1 = true;
                    that.Islogin2 = true;
                    console.log(that.username + 'here');
                    console.log(that.Islogin1);
                },
                error:function(){
                    console.log('error');
                }
            });
        }
        else{
            alert('token已失效！');
        }
    }
};
</script>

<style scoped>
.title{
    font-size: 30px;
}
.navbar-right{
    margin-right: 50px;
}
/* .nav>div{
    position: relative;
    display: block;
} */
a{
    outline: none;
}
</style>
