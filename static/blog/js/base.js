// 深色主题滚动行为初始化
document.addEventListener('DOMContentLoaded', function() {
    // 导航栏Headroom初始化已在base.html中通过jQuery执行

    // 响应式移动端菜单关闭
    $('.navbar-collapse .nav-link').on('click', function() {
        if ($('.navbar-collapse').hasClass('show')) {
            $('.navbar-toggler').trigger('click');
        }
    });
});