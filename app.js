const express = require("express");
const app = express();
const bodyParser = require('body-parser');
const { spawn } = require("child_process");

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/model",(req,res)=>{

    EST_COST_RANGE = req.body.EST_COST_RANGE;
    MODEOFTENDER = req.body.MODEOFTENDER;
    METHOD_OF_PURCHASE = req.body.METHOD_OF_PURCHASE;
    FINANCIAL_POWER_CODE = req.body.FINANCIAL_POWER_CODE;
    CFA_CODE = req.body.CFA_CODE;
    CONCURRENCE_BY = req.body.CONCURRENCE_BY;
    BUDGET_HEAD_CODE = req.body.BUDGET_HEAD_CODE;
    IS_PAC = req.body.IS_PAC;
    input_data = [EST_COST_RANGE ,MODEOFTENDER , METHOD_OF_PURCHASE,FINANCIAL_POWER_CODE, CFA_CODE,CONCURRENCE_BY, BUDGET_HEAD_CODE , IS_PAC]
    const python = spawn("python", ["model.py", input_data ]);
    

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

app.listen(3000, () => {
    console.log(`server is running on port 3000`);
})
// module.exports = app;