var i = 0;
var id;
var pr = false;
var ne = false;

function galleryR() {
    var i=Math.floor((Math.random() * 16) + 1);
    var t = 40;
    var k = 1500 / t;
    var p = 1 / k;
    var c;

    document.getElementById("gallery1").src = "/static/img/image1.jpg";
    document.getElementById("gallery1").style.opacity = 1;
    document.getElementById("gallery2").src = "/static/img/image2.jpg";
    document.getElementById("gallery2").style.opacity = 0;

    function timeout() {
        if ((pr) || (ne)) {
            c = k + 1;
        }
        if (c <= k) {
            document.getElementById("gallery1").style.opacity = parseFloat(document.getElementById("gallery1").style.opacity) - p;
            document.getElementById("gallery2").style.opacity = parseFloat(document.getElementById("gallery2").style.opacity) + p;
            c++;
        } else {
            clearInterval(id);
            if ((!pr) && (!ne)) {
                if (i == 0 || i < 16) {
                    i++;
                }
                else
                if (i == 16) {
                    i = 1;
                }
                document.getElementById("gallery1").src = "/static/img/image" + i + ".jpg";
                document.getElementById("gallery1").style.opacity = 1;
                if (i < 16) {
                    document.getElementById("gallery2").src = "/static/img/image" + (i + 1) + ".jpg";
                    document.getElementById("gallery2").style.opacity = 0;
                } else {
                    document.getElementById("gallery2").src = "/static/img/image1.jpg";
                    document.getElementById("gallery2").style.opacity = 0;
                }
            }
            if (pr) {
                pr = false;
            } else
            if (ne) {
                ne = false;
            }
            c = 1;
            setTimeout(function() {
                id = setInterval(timeout, t);
            }, 1000);
        }
    }

    c = 1;
    setTimeout(function() {
        id = setInterval(timeout, t);
    }, 1000);
}

window.onload = galleryR;

var myCenter = new google.maps.LatLng(45.253992, 9.989992);
var marker;

function initialize() {
    var mapProp = {
        center: new google.maps.LatLng(45.253992, 9.989992),
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROAD
    };
    var map = new google.maps.Map(document.getElementById("map"), mapProp);

    var marker = new google.maps.Marker({
        position: myCenter
    });

    marker.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);

