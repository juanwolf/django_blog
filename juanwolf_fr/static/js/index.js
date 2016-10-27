var language_available = ["en", "fr"];

function detectPageLanguage() {
    var path = window.location.pathname,
        pathArray = path.split('/');
    $language = pathArray[1];
    $("#language-selection-select").val($language);
}

function saveLanguageChoosen($language) {
    document.cookie = "";
    var d = new Date();
    var exdays = 7;
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    console.log("language received = " + $language);
    document.cookie = "lang=" + $language + ";expires=" + expires + ";domain=.juanwolf.fr;path=/";
}

function redirect($language) {
    var path = window.location.pathname,
        pathArray = path.split('/');
    pathArray[1] = $language;
    var newPath = pathArray[1];
    for (var i = 2; i < pathArray.length; i++) {
        newPath += "/" + pathArray[i];
    }
    document.location.href = window.location.protocol + "//" + window.location.host + "/" + newPath;
}

function positionFooter() {
    var contentHeight = $("nav").height() + $('body > div').height() + $("footer").height();
    if (contentHeight < $(window).height()) {
        $('footer').addClass("footer-tall-screen");
    } else {
        $('footer').removeClass("footer-tall-screen");
    }
}

$(document).ready(function () {
    hljs.initHighlightingOnLoad();
    detectPageLanguage();
    positionFooter();
    console.log("Bonjour");
    $(window).resize(positionFooter);

    $("#menu-button").click(function () {
        var hasClassActived = $("#menu-link-list").hasClass("active-true");
        $("#menu-link-list").removeClass();
        $(".container").removeClass("active-true");
        $(".container").removeClass("active-false");
        if (!hasClassActived) {
            $("#menu-link-list").addClass("active-true");
            $(".container").addClass("active-true");
        } else {
            $("#menu-link-list").addClass("active-false");
            $(".container").addClass("active-false");
        }
    });
    
    $(".container").click(function() {
        var hasClassActived = $("#menu-link-list").hasClass("active-true");
        if (hasClassActived) {
            $("#menu-link-list").removeClass();
            $(".container").removeClass("active-true");
            $(".container").removeClass("active-false");
            $("#menu-link-list").addClass("active-false");
            $(".container").addClass("active-false");
        }
        
    });

    $('#language-selection-select').customSelect();
    $("#language-selection-select").change(function () {
        saveLanguageChoosen($(this).val());
        redirect($(this).val());
    });

    $("#language-select-blog").customSelect();
    $("#language-select-blog").change(function () {
        $(this).parent("form").submit();
    });
});