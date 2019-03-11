$(function () {
    $('.register').width(innerWidth)
    console.log('1111111')

    // 注册邮箱失焦事件
    $('#username').blur(function () {
        var username=$(this).val()

        if (username==''){
            return
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
                $('#email_check').removeClass('form-group has-success has-feedback').addClass('form-group has-error has-feedback')
                $('#error_username').html('用户邮箱已被注册').css('color','red')
                $('#email_check02').removeClass('glyphicon glyphicon-ok form-control-feedback').addClass('glyphicon glyphicon-remove form-control-feedback')
            }else if (response.status==1){
                $('#email_check').removeClass('form-group has-error has-feedback').addClass('form-group has-success has-feedback')
                $('#error_username').html('用户邮箱可使用').css('color','green')
                $('#email_check02').removeClass('glyphicon glyphicon-remove form-control-feedback').addClass('glyphicon glyphicon-ok form-control-feedback')
            }
        })
    })

    // 密码输入失焦事件
    $('#password').blur(function () {
        var password=$(this).val()
        // console.log(password)

        data={
            'password':password,
        }

        $.get('/check_02',data,function (response) {
            // console.log(response)
            if (response.status==0){
                $('#password_check').removeClass('form-group has-success has-feedback').addClass('form-group has-error has-feedback')
                $('#password_check02').removeClass('glyphicon glyphicon-ok form-control-feedback').addClass('glyphicon glyphicon-remove form-control-feedback')
            }else if (response.status==1){
                $('#password_check').removeClass('form-group has-error has-feedback').addClass('form-group has-success has-feedback')
                $('#password_check02').removeClass('glyphicon glyphicon-remove form-control-feedback').addClass('glyphicon glyphicon-ok form-control-feedback')
            }
        })
    })

    // 密码再次输入失焦事件
    $('#password_again').blur(function () {
        var password_again=$(this).val()
        var password=$('#password').val()
        // console.log(password)
        // console.log(password_again)

        data={
            'password_again':password_again,
            'password':password
        }

        $.get('/check_03',data,function (response) {
            // console.log(response)
            if (response.status==0){
                $('#password_again_check').removeClass('form-group has-success has-feedback').addClass('form-group has-error has-feedback')
                $('#password_again_check02').removeClass('glyphicon glyphicon-ok form-control-feedback').addClass('glyphicon glyphicon-remove form-control-feedback')
            }else if (response.status==1){
                $('#password_again_check').removeClass('form-group has-error has-feedbackform-group has-success has-feedback').addClass('form-group has-success has-feedback')
                $('#password_again_check02').removeClass('glyphicon glyphicon-remove form-control-feedback').addClass('glyphicon glyphicon-ok form-control-feedback')
            }
        })
    })

    $('#name').blur(function () {

        name=$(this).val()
        console.log(name)

        if (name.length==0){
            $('#name_check').removeClass('form-group has-success has-feedback').addClass('form-group has-error has-feedback')
            $('#name_check02').removeClass('glyphicon glyphicon-ok form-control-feedback').addClass('glyphicon glyphicon-remove form-control-feedback')
        }else {
             $('#name_check').removeClass('form-group has-error has-feedback').addClass('form-group has-success has-feedback')
            $('#name_check02').removeClass('glyphicon glyphicon-remove form-control-feedback').addClass('glyphicon glyphicon-ok form-control-feedback')
        }

    })


})