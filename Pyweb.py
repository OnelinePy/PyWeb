from optparse import Option
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel

web = FastAPI()

@web.get("/Age/",response_class=HTMLResponse)
def dob():
 return """<!DOCTYPE html>
<html>
<body>
<center><h1>Hi This Is OneLinePy</h1>
<h4>I'M Karthick.M From Narasu's Sarathy Institute Of Technoogy</h4></center>
</body>
</html>
"""

@web.put("/Year")
async def Year():
 return {"Year":1973}
