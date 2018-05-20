<template>
  <!-- Upload_Picture_Modal -->
  <div class="modal fade" id="UploadpicModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="myModalLabel">上传图片</h4>
        </div>
        <div class="modal-body">
            <!-- 模态框中注册表单 -->
            <form id="uploadForm">
                <div class="form-group">
                    <label for="file">选择图片</label>
                    <input id="file" type="file" name="file" class="form-control"/>
                </div>
                <div class="form-group">
                    <label for="tags">图片标签</label>
                    <input id='tags' placeholder="图片标签" class="form-control"/>
                </div>
                <div class="form-group">
                    <label for="desc">图片描述</label>
                    <input id="desc" placeholder="图片描述" class="form-control"/>
                </div>
                <button id="upload" type="button">上传</button>
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
        // var tags = $('#tags').val().split(" ");
        var formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);
        formData.append('tags', $('#tags').val());
        formData.append('desc', $('#desc').val());
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/api/upload_pic',//后端接口
            data: formData,
            dataType: "json",
            headers:{
                'Authorization':'Bearer' + ' ' + $.cookie('token')
            },
            cache:false,
            contentType: false, // 这两句一定要加上，否则数据会被序列化，
            processData:false,  // 而导致后端不能识别
        }).done(function(res){
            console.log('success');
            $("#UploadpicModal").modal("hide")
        }).fail(function(res){
            console.log('fail');
        });
    });
});

export default {

}
</script>

<style>

</style>