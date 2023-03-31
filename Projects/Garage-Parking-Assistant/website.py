html = """<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
.buttonGreen { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
.buttonRed { background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Garage Parking Assitant - Control Panel - Subaru</h1></center>

<form><center>
<p><h2>%s<p>
<center> <button class="buttonGreen" name="reload" value="Reload" type="submit">Reload</button>

<h1> Green Light - Just Right</h1>
<center> <button class="buttonGreen" name="justrightAdd" value="Add" type="submit">Add 5</button>
<button class="buttonRed" name="justrightMinus" value="Minus" type="submit">Subtract 5</button>
<input type="number" id="justrightInput" name="quantity" min="1" max="500">
</form>
<br><br>
<form><center>
<h1> Blue Light - To Far</h1>
<center> <button class="buttonGreen" name="tofarAdd" value="Add" type="submit">Add 5</button>
<button class="buttonRed" name="tofarMinus" value="Minus" type="submit">Subtract 5</button>
</form>
<br><br>
<form><center>
<h1> Red Light - To Close</h1>
<center> <button class="buttonGreen" name="tocloseAdd" value="Add" type="submit">Add 5</button>
<button class="buttonRed" name="tocloseMinus" value="Minus" type="submit">Subtract 5</button>
</form>
<br><br>
</body></html>
"""

"""
red = "toclose"
green = "justright"
blue = "tofar"
"""