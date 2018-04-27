<template>
  <!-- Upload_Picture_Modal -->
  <div class="modal fade" id="UploadpicModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="myModalLabel">注册</h4>
        </div>
        <div class="modal-body">
            <!-- 模态框中注册表单 -->
            <form id="uploadForm">
                <input id="file" type="file" name="file"/>
                <button id="upload" type="button"></button>
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
    $("#upload").click(function(){
        var formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/api/upload_pic',//后端接口
            data: formData,
            dataType: "json",
            headers:{
                'Authorization':'Bearer' + ' ' + $.cookie('token')
            },
            contentType: false,
            cache:false,
            processData:false,
        }).done(function(res){
            console.log('success');
            $("#UploadpicModal").modal("hide")
        }).fail(function(res){
            alert('请先登录！');
            console.log('fail');
            console.log($.cookie('token'))
        });
    });
});

export default {

}
</script>

<style>

</style>