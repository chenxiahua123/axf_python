$(function () {
    $('.cart').width(innerWidth)

    // 选择框选中
    $('.confirm-wrapper').click(function () {
        console.log('选中成功')

        cartid=$(this).attr('cartid')

        var $that=$(this)

        console.log(cartid)

        data={
            'cartid':cartid,
        }

        $.get('/changestatus',data,function (response) {
            console.log(response)
            if (response.status==1){
                if (response.isselect){
                    var $span=$that.find('span')
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                    console.log(111111111111111111111)
                }else{
                    var $span=$that.find('span')
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                    console.log(222222222222222222)
                }
            }
        })

    })


})