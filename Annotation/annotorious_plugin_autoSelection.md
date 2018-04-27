I had been created to auto-selection.js for contribute Annotorious.

This is function of method created below. <br>

forked in annotorious 


Method
=======
auto-selector.js | <br>

+ annotorious.plugin.autoSelector.prototype.onInitAnnotator = function(annotator)
> **must be set to CurrentSelector('rect');**<br>

+ annotorious.plugin.autoSelector.Selector.prototype._attachListeners = function()
> start annotorious handler.<br>
> **if you want to create to new function, then maybe have to declare this inner function.<br>
> Can do it !!**<br>

+ annotorious.plugin.autoSelector.Selector.prototype.getName = function()
> that is return type something for want **tag box type.**<br>

+ annotorious.plugin.autoSelector.Selector.prototype.stopSelection = function()
> **finish**<br>

+ annotorious.plugin.autoSelector.Selector.prototype.startSelection = function(x, y)
> **Annotorious Entry point.**<br>
> this function get pointer from mouse click. <br>
> Is this like main and you **must be declare attachListeners() in it.**<br>
> and recommended to call delete geometry job.<br>

+ annotorious.plugin.autoSelector.Selector.prototype.getSupportedShapeType = function()
> it's important method.<br>
> primary type [ polygon, rect ] <br>
> Maybe you set to the other type( polygon..?? ), have to modified geometry if then no rect type.

+ annotorious.plugin.autoSelector.Selector.prototype.getShape = function()
> for set tagbox and for save geometry information create to this.<br>
> getShape call by attachListeners()<br>
> and it return box type, and **it return geometry for sending json data.**<br>

+ annotorious.plugin.autoSelector.Selector.prototype.drawShape = function()
> **no more to needed.**

+ annotorious.plugin.autoSelector.Selector.prototype.drawRect = function(click_x, click_y)
> it is __**my custom drawing tool for auto sketch.**__<br>
> code example below.<br>

<pre>
//TODO:simple code
attachListeners(shape) {
   self.drawRect(self._anchor.x, self._anchor.y);
   try{
      fireEvent("onSelectedCompleted",{mouseEvent:event, shape:shape, viewportBounds: getViewportBounds())
   }
}
</pre>
