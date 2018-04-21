// $("#FormInfo").validate({
//     rules: {
//         Account: {
//             required: true,
//             minlength: 4
//         },
//         Password: {
//             required: true,
//             minlength: 6
//         }
//     },
//     messages: {
//         Account: {
//             required: "请输入账号",
//             minlength: "账号应不少于四位"
//         },
//         Password: {
//             required: "请输入密码",
//             minlength: "密码应不少于六位"
//         }
//     },
//     focusCleanup: true,
//     success: "valid",
//     submitHandler: function () {
//         var data = {
//             username: Account.value,
//             password: Password.value
//         };
//         console.log(data);
//         $.ajax({
//             type: 'POST',
//             url: "http://127.0.0.1:5000/api/auth",//后端接口
//             data: JSON.stringify(data),
//             dataType: "json",
//             success: function (res) {
//                 if (res.responseJSON.token) {
//                     alert(res.responseJSON.token);
//                 }
//                 else {
//                     alert("服务端发生错误")
//                 }
//             }
//         });
//     }
// });
$(document).ready(function(){
    $("#submit").click(function(){
        // $.ajax({
        //     type: 'POST',
        //     url: "http://127.0.0.1:5000/api/auth",//后端接口
        //     data: JSON.stringify(data),
        //     dataType: "json",
        //     complete: function (res) {
        //         if (res.responseJSON.token) {
        //             alert(res.responseJSON.token);
        //         }
        //         else {
        //             alert("服务端发生错误")
        //         }
        //     }
        // });
        alert("呵呵哒！");
    });
});