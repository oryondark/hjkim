```javascript
<script src="jquery.min.js"></script>
<script src="jssor.slider.min.js"></script>
<script>
    jQuery(document).ready(function ($) {
        var options = { $LazyLoading: 0 }; // default '1' will to load all.
        var jssor1_slider = new $JssorSlider$("jssor_1", options);
    });
</script>
<div id="jssor_1" style="position:relative;top:0px;left:0px;width:980px;height:380px;overflow:hidden;">
    <div data-u="slides" style="position:absolute;top:0px;left:0px;width:980px;height:380px;overflow:hidden;">
        // you want to use lazyloading, must be changed img.src to img.data-src2
        <div><img data-u="image" data-src2="image1.jpg" /></div>
        <div><img data-u="image" data-src2="image2.jpg" /></div>
    </div>
</div>
```
