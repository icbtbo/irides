<template>
  <!-- LoginModal -->
  <div class="modal fade" id="LoginModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="myModalLabel">登录</h4>
        </div>
        <div class="modal-body">
            <!-- 模态框中登录表单 -->
            <form id="LoginForm" action="" method="post">
                <div class="form-group">
                  <label for="Account">Account</label>
                  <input type="text" class="form-control" id="Account" name="Account" placeholder="账号">
                </div>
                <div class="form-group">
                  <label for="Password">Password</label>
                  <input type="password" class="form-control" id="Password" name="Password" placeholder="密码">
                </div>
                <!-- <div class="form-group">
                  <label for="exampleInputFile">File input</label>
                  <input type="file" id="exampleInputFile">
                  <p class="help-block">Example block-level help text here.</p>
                </div> -->
                <!-- <div class="checkbox">
                  <label>
                    <input type="checkbox"> Check me out
                  </label>
                </div> -->
                <button type="submit" class="btn btn-default" id="submit">登录</button>
              </form>
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
// $(document).ready(function(){
//     $("#submit").click(function(){
//         var data = {
//             username: $("#Account").val(),
//             password: $("#Password").val()
//         };
//         console.log(data);
//         $.ajax({
//             type: 'POST',
//             url: 'http://127.0.0.1:5000/api/auth',//后端接口
//             data: JSON.stringify(data),
//             dataType: "json",
//             complete: function (res) {
//                 if (res.responseJSON.token) {
//                     alert(res.responseJSON.token);
//                 }
//                 else {
//                     alert("服务端发生错误");
//                 }
//             }
//         });
//     });
// });
$(document).ready(function(){
  $("#LoginForm").validate({
      // debug:true,
      rules:{
          Account: {
              required: true,
              minlength: 4
          },
          Password: {
              required: true,
              minlength: 6
          },
      },
      messages:{
          Account: {
              required: "请输入账号",
              minlength: "账号应不少于四位"
          },
          Password: {
              required: "请输入密码",
              minlength: "密码应不少于六位"
          },
      },
      focusCleanup: true,
      success: "valid",
      submitHandler: function () {
        // alert('come in');
          var data = {
              username: $("#Account").val(),
              password: $("#Password").val()
              // pwdagain: $("#PwdAgain").val()
              // "username": "admddfgetsd4",
              // "password": "password4"
          };
          console.log(data);
          $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:5000/api/auth',//后端接口
              contentType: "application/json",
              data: JSON.stringify(data),
              dataType: "json",
              complete: function (res) {
                  if (res.responseJSON.token) {
                      console.log(res);
                      $.cookie('token',res.responseJSON.token,{path:'/'})
                      $("#LoginModal").modal("hide")
                      location.reload(true); 
                  }
                  else {
                    alert("服务端发生错误");
                  }
              },
              // success: function(){
              //   console.log('success');
              // },
              // error: function(){
              //   console.log('error');
              // }
          });
      }
  });
});
export default {

}
</script>

<style>

</style>
