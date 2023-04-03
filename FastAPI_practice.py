from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app = FastAPI()

class Item(BaseModel):
    name: str
    price:float
    is_offer: Union[bool, None] = None



@app.get("/", response_class=HTMLResponse)
def main():
    html  = """
    <html>
        <head>
        <title> FAST API </title>
        <script>
            function gid(id){ // only String
                return document.getElementById(id);
            }
        
        document.addEventListener("DOMContentLoaded", function(){
            var sendBtn = document.getElementById("sendBtn");
            var addBtn = document.getElementById("addBtn");
            var form = document.getElementById("form");
            var data_div = document.getElementsByClassName("data-section");

            sendBtn.addEventListener('click',() => {
                const model_id = document.getElementById("model_id").value;
                const sequential_id = document.getElementById("sequential_id").value;
                const dUrl = 'http://100.100.100.24:8080/himed2/.live?';
                const rUrl = 'http://172.16.250.20/himed2/.live?';

                var param = {};

                for(let i=0; i< data_div.lenth; i++){
                    param[] = 
                }

               
                var data = {"data":[]}
                const kics = dUrl+"model_id="+model_id+"&sequential_id="+sequential_id;
                /*
                fetch(kics)
                .then((res)=>res.json())
                .thrn((data)=>console.log(data));*/
            });

            addBtn.addEventListener('click',() => {
                var new_div = document.createElement('div');
                var new_input_key = document.createElement('input');
                var new_input_value = document.createElement('input');

                new_div.setAttribute('class','data-section');
                new_input_key.setAttribute('name','key');
                new_input_key.setAttribute('placeholder','키');
                new_input_value.setAttribute('name','value');
                new_input_value.setAttribute('placeholder','값');
                new_div.append(new_input_key);
                new_div.append(new_input_value);

                form.append(new_div);
            });
        });
        </script>
        </head>
        <style>
            .frame{float:left;}
        </style>
        <body>
            <h1>FAST API Form</h1>
            <div style="height:100%;width:40%;" class="frame">
            <form id="form" name="form" action="/">
                <div>
                    <select id="model_id">
                        <option value="">선택</option>
                        <option value="">ast</option>
                        <option value="">biz</option>
                        <option value=""></option>
                    </select>
                    <input type="text" id="sequential_id" placeholder="모델명">
                </div>
                <div class="data-section">
                    <input type="text" id="key" name="key" placeholder="키">
                    <input type="text" id="value" name="value" placeholder="값">
                </div>
            </form>
            <button id="addBtn">추가</button>
            <button id="sendBtn">전송</button>
            </div>
            <div style="height:100%;width:40%;" class="frame">
                <div id="result" contenteditable="false" style="width:350px; height:350px; border: 1px solid black;     margin-bottom: 33px;"></div>
            </div>
        </body>
    </html>
    """
    return html

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "q":q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name":item.name,"item_id":item_id}
