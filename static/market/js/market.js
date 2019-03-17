$(function () {
    var index=$.cookie('index')
    // console.log(index)
    if (index){
        $('.type-slider li').eq(index).addClass('active')
    }else {
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        console.log('侧边栏单击成功')

        $.cookie('index',$(this).index(),{expires:3,path:'/'})




    })









    // 第一步：先处理综合类型和综合排序单击切换事件

    // 设立开关，控制全部类型的取反
    var category_bt=false
    $('#category_bt').click(function () {
        console.log("全部类型单击成功")

        category_bt=!category_bt

        category_bt ? categoryShow() : categoryHide()

    })

    // 设立开关，控制综合排序开关
    var sort_bt=false
    $('#sort_bt').click(function () {
        console.log("综合排序呢单击成功")

        sort_bt=!sort_bt

        sort_bt ? sortShow() : sortHide()

    })

    // 蒙层点击
    $('.bounce-view').click(function () {
        var category_bt=false
        categoryHide()

        var sort_bt=false
        sortHide()
    })








        // 设置全部类型 开函数
    function categoryShow() {
        sortHide()
        var sort_bt=false
        $('.bounce-view')[0].style.display='block'
        $('#category_bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')

    }
            // 设置全部类型 关函数
     function categoryHide() {

        $('.bounce-view')[0].style.display='none'
        $('#category_bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')

    }



    // 设置综合排序 开函数
    function sortShow() {
        var category_bt=false

        categoryHide()
        $('.bounce-view')[1].style.display='block'
        $('#sort_bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')

    }

    function sortHide() {

        $('.bounce-view')[1].style.display='none'
        $('#sort_bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')

    }

    $('.bt-wrapper .glyphicon-minus').hide()
    $('.bt-wrapper .num').hide()

    // 购物车 加 操作
    $('.bt-wrapper .glyphicon-plus').click(function () {

        var $that=$(this)
        // console.log('加操作')

        var goodid=$(this).attr('goodid')

        // console.log(11111111111111)

        // console.log(goodid)

        data={
            'goodid':goodid,
        }

        $.get('/addcart',data,function (response) {
            // console.log(response)
            if (response.status==0){
                window.open('/login',target='_self')
            }else if (response.status==1){
                // console.log(response)
                $that.prev().show().html(response.number)
                $that.prev().prev().show()
            }

        })

    })

    // 购物车减操作
    $('.bt-wrapper .glyphicon-minus').click(function () {

        console.log('Minus-operation')

        var goodid=$(this).attr('goodid')

        var $that=$(this)

        data={
            'goodid':goodid,
        }

        $.get('/minuscart',data,function (response) {
            console.log(response)
            $that.next().html(response.number)
            if (response.number==0){
                $that.next().hide()
                $that.hide()
            }
        })


    })






})