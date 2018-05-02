## css <br>
jssor 패키지 적용 시, 

```
<style>
	/*jssor slider loading skin spin css*/
	.jssorl-009-spin img {
		animation-name: jssorl-009-spin;
		animation-duration: 1.6s;
		animation-iteration-count: infinite;
		animation-timing-function: linear;
	}

	@keyframes jssorl-009-spin {
		from { transform: rotate(0deg); }
		to { transform: rotate(360deg); }
	}
</style>
```
<br>

## javaScript <br>

import package path below.
aready have js_packages ([Jquery][0], [jssor_thumbnail_factory][1]) << follow link.
<pre>
<!-- this plugin needed to use jquery -->
<script src="js/jssor.slider-27.1.0.min.js" type="text/javascript"></script>
<script src="js/thumbnail_load.js" type="text/javascript"></script>
</pre>

to next, asign a tag block\<div\> for load thumbnail.
```
<div id="thumbnail_block">
<!-- Loading Screen -->
	<div id="thumbnail_area" data-u="slides" style="cursor:default;width:950px;height:100px;overflow:hidden;">
     </div>
</div>
```


[API document Link][2]







[0]:http://jquery.com/download/ ("jquery")
[1]:https://www.jssor.com/demos/image-slider.slider ("여러 종류의 Slide 샘플과 패키지 소스를 얻을 수 있습니다.")
[2]:https://www.jssor.com/development/ ("Package 사이트")
