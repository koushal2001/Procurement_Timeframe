const express = require("express");
const app = express();
const bodyParser = require('body-parser');
const { spawn } = require("child_process");

var cors = require('cors')

app.use(cors()) // Use this after the variable declaration

app.use(bodyParser.json())

app.post("/model",(req,res)=>{

    EST_COST = req.body.EST_COST;
    MODEOFTENDER = req.body.MODEOFTENDER;
    METHOD_OF_PURCHASE = req.body.METHOD_OF_PURCHASE;
    FINANCIAL_POWER_CODE = req.body.FINANCIAL_POWER_CODE;
    CFA_CODE = req.body.CFA_CODE;
    CONCURRENCE_BY = req.body.CONCURRENCE_BY;
    BUDGET_HEAD_CODE = req.body.BUDGET_HEAD_CODE;
    IS_PAC = req.body.IS_PAC;
    input_data = [EST_COST ,MODEOFTENDER , METHOD_OF_PURCHASE,FINANCIAL_POWER_CODE, CFA_CODE,CONCURRENCE_BY, BUDGET_HEAD_CODE , IS_PAC]
   
    const python = spawn("python", ["./input.py", input_data ],{ shell: true });
    
    var processed_data;
    python.stdout.on("data", function (data) {
        processed_data = data.toString();
    });
    python.stderr.on("data", data => {
        console.error(`stderr: ${data}`);
    })
    python.on("exit", (code) => {
        
        res.send(processed_data);

    });

    
})

app.listen(4000, () => {
    console.log(`server is running on port 4000`);
})
// module.exports = app;
