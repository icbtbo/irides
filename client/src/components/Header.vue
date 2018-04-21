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
                <li><a href="#">上传图片</a></li>
                <li><a  data-toggle="modal" href="#myModal">登陆</a></li>
                <li><a href="#">注册</a></li>
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
    return {};
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
</style>
