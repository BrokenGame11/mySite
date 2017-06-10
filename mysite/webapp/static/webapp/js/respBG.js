
var bg = $("#bg1, #bg2");

function resizeBackground() {
    bg.height($(window).height() + 60);
}

$(window).resize(resizeBackground);
resizeBackground();
