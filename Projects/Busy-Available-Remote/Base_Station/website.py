html = """<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
.buttonGreen { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
.buttonRed { background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Busy or Available Base Station</h1></center>

<form><center>
<p><h2>%s<p>
<center> <button class="buttonGreen" name="reload" value="Reload" type="submit">Reload</button>

<h1> Green Light - Just Right</h1>
<center> <button class="buttonGreen" name="Available" value="Available" type="submit">Available</button>
<button class="buttonRed" name="Busy" value="Busy" type="submit">Busy</button>
<input type="number" id="duration" name="duration" min="1" max="500">

</form>
<br><br>
</body></html>
"""



