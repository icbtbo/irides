<template>
  <!-- RegModal -->
  <div class="modal fade" id="RegModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="myModalLabel">注册</h4>
        </div>
        <div class="modal-body">
            <!-- 模态框中注册表单 -->
            <form id="RegForm" action="" >
                <div class="form-group">
                  <label for="RegAccount">账号</label>
                  <input type="text" class="form-control" id="RegAccount" name="RegAccount"  placeholder="账号">
                </div>
                <div class="form-group">
                  <label for="RegPassword">密码</label>
                  <input type="password" class="form-control" id="RegPassword" name="RegPassword" placeholder="密码">
                </div>
                <div class="form-group">
                  <label for="ConfirmPwd">再次输入密码</label>
                  <input type="password" class="form-control" id="ConfirmPwd" name="ConfirmPwd" placeholder="确认密码">
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
                <button type="submit" class="btn btn-default" id="reg">注册</button>
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
$(document).ready(function(){
  $("#RegForm").validate({
      // debug:true,
      rules:{
          RegAccount: {
              required: true,
              minlength: 4
          },
          RegPassword: {
              required: true,
              minlength: 6
          },
          ConfirmPwd:{
            required:true,
            minlength:6,
            equalTo: "#RegPassword"
          }
      },
      messages:{
          RegAccount: {
              required: "请输入账号",
              minlength: "账号应不少于四位"
          },
          RegPassword: {
              required: "请输入密码",
              minlength: "密码应不少于六位"
          },
          ConfirmPwd: {
              required: "请输入密码",
              minlength: "密码应不少于六位",
              equalTo: "两次密码输入不一致"
          },
      },
      focusCleanup: true,
      success: "valid",
      submitHandler: function () {
        // alert('come in');
          var data = {
              username: $("#RegAccount").val(),
              password: $("#RegPassword").val()
              // pwdagain: $("#PwdAgain").val()
              // "username": "admddfgetsd4",
              // "password": "password4"
          };
          console.log(data);
          $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:5000/api/users',//后端接口
              contentType: "application/json",
              data: JSON.stringify(data),
              dataType: "json",
              complete: function (res) {
                  if (res.responseJSON) {
                      console.log(res.responseJSON);
                      alert('注册成功');
                      $('#RegModal').modal('hide');
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
// $(document).ready(function(){
//     $("#reg").click(function(){
//         var data = {
//             username: $("#RegAccount").val(),
//             password: $("#RegPassword").val()
//             // pwdagain: $("#PwdAgain").val()
//             // "username": "admddfgetsd4",
//             // "password": "password4"
//         };
//         console.log(data);
//         $.ajax({
//             type: 'POST',
//             url: 'http://127.0.0.1:5000/api/users',//后端接口
//             contentType: "application/json",
//             data: JSON.stringify(data),
//             dataType: "json",
//             complete: function (res) {
//                 if (res.responseJSON.data) {
//                     alert(res.responseJSON.data);
//                 }
//                 else {
//                   alert("服务端发生错误");
//                 }
//             },
//             // success: function(){
//             //   console.log('success');
//             // },
//             // error: function(){
//             //   console.log('error');
//             // }
//         });
//     });
// });
export default {

}
</script>

<style>

</style>
