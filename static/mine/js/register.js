$(function () {
    $('.register').width(innerWidth)
    console.log('1111111')
    $('#username').blur(function () {
        var username=$(this).val()

        if (username.length==0){
            $('#error_username').hide()
        }

        $('#error_username').css('display','block')

        console.log(username)
        // console.log($(this.val()))
        data={
            'username':username,
        }

        $.get('/check_01',data,function (response) {
            console.log(response)
            if (response.status==0){
                $('#error_username').html('用户邮箱已被注册').css('color','red')
            }else if (response.status==1){
                $('#error_username').html('用户邮箱可使用').css('color','green')
            }
        })
    })




})