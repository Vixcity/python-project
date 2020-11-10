layui.use(['jquery', 'util'], function () {
    var $ = layui.jquery,
        util = layui.util;
    $(window).load(function () {
        $("#loading").fadeOut(500);
        new WOW().init();
    })
    util.fixbar();;
    $('.next').click(function () {
        $('html,body').animate({
            scrollTop: $('#section1').outerHeight() + 1
        }, 600);
    });
    $('#menu').on('click', function () {
        var mark = $(this).attr('data-mark');
        if (mark === 'false') {
            $('body').attr({ 'style': "overflow:hidden;padding-right:17px;" });
            $(this).removeClass('menu_open').addClass('menu_close');
            $('layui-fixbar').css({'display':'none'});
            //open
            $('#navgation').removeClass('navgation_close').addClass('navgation_open');
            $(this).attr({ 'data-mark': "true" });
        } else {
            $('body').removeAttr('style');
            $(this).removeClass('menu_close').addClass('menu_open');
            $('layui-fixbar').css({'display':'block'});
            //close
            $('#navgation').removeClass('navgation_open').addClass('navgation_close');
            $(this).attr({ 'data-mark': "false" });
        }
    });

});