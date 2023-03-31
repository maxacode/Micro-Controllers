html = f"""
<!DOCTYPE html>
<html>
<head>
<title>lil-J v2 Robot Control</title>
</head>
<center><b>
<form action="./forward">
<input type="submit" value="Forward" style="height:120px; width:120px" />
</form>
<table><tr>
<td><form action="./left">
<input type="submit" value="Left" style="height:120px; width:120px" />
</form></td>
<td><form action="./stop">
<input type="submit" value="Stop" style="height:120px; width:120px" />
</form></td>
<td><form action="./right">
<input type="submit" value="Right" style="height:120px; width:120px" />
</form></td>
</tr></table>
<form action="./back">
<input type="submit" value="Back" style="height:120px; width:120px" />
</form>
</body>
</html>
"""