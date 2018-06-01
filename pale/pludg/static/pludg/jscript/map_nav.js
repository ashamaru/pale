var canvas = document.getElementById('map_nav_canvas');
var ctx = canvas.getContext('2d');

ctx.fillStyle = 'lime';
ctx.fillRect(0, 0, 400, 400);

ctx.fillStyle = 'purple';
ctx.fillRect(0, 0, 299,149);

var image = new Image();
image.src = "/static/pludg/images/main_map.png";

ctx.imageSmoothingEnabled = true;
ctx.drawImage(image, 0, 0, 1200, 600);