$(function () {
    $('.cart').width(innerWidth)

    total()

    // 选择框选中
    $('.confirm-wrapper').click(function () {
        // console.log('选中成功')

        cartid=$(this).attr('cartid')

        var $that=$(this)

        console.log(cartid)

        data={
            'cartid':cartid,
        }

        $.get('/changestatus',data,function (response) {
            // console.log(response)
            if (response.status==1){
                if (response.isselect){
                    var $span=$that.find('span')
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                    // console.log(111111111111111111111)
                    total()
                }else{
                    var $span=$that.find('span')
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                    // console.log(222222222222222222)
                    total()
                }
            }
        })



    })


    // 全选/全部取消处理
    $('.bill-left .all').click(function () {
        console.log(55555555555555)


        var isall=$(this).attr('isall')
        console.log(isall)



        isall=(isall=='false') ? true : false

        $(this).attr('isall',isall)
        $that=$(this)

        console.log(isall)

        data={
            'isall':isall
        }

        if (isall){
                $('.confirm-wrapper span').removeClass('no').addClass('glyphicon glyphicon-ok')
            }else{
                $('.confirm-wrapper span').removeClass('glyphicon glyphicon-ok').addClass('no')
            }

        $.get('/changeall',data,function (response) {
            console.log(response)
            if (isall){
                $that.find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
            }else {
                $that.find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
            }

        })

        total()
    })

    // 算术功能
    function total() {
        console.log('ppppppppppp')

        var sum=0

        $('.confirm-wrapper').each(function () {
            console.log(111111111111111111)
            if ($(this).find('span').is('.glyphicon-ok')){
                console.log(222222222222)
                var price=parseInt($(this).next().find('p').eq(1).attr('price'))
                var number=parseInt($(this).next().find('p').eq(2).attr('num'))

                console.log(price,typeof(price))
                console.log(number,typeof(number))

                sum+=price*number

            }
        })

        console.log(sum)
        $('.total b').html(sum)



    }




})