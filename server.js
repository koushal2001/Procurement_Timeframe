const express = require("express");
const app = express();
const bodyParser = require('body-parser');
const { spawn } = require("child_process");

var cors = require('cors')

app.use(cors()) // Use this after the variable declaration

app.use(bodyParser.json())

app.post("/model",(req,res)=>{

    TOTAL_COST = req.body.TOTAL_COST
    MODE_OF_TENDER_CODE = req.body.MODE_OF_TENDER_CODE
    FINANCIAL_POWER_CODE = req.body.FINANCIAL_POWER_CODE
    FINANCIAL_POWER_SERIAL_NO = req.body.FINANCIAL_POWER_SERIAL_NO
    CFA_CODE = req.body.CFA_CODE
    // UO_NO = req.body.UO_NO
    GEM_CONTRACT_NO = req.body.GEM_CONTRACT_NO
    BUDGET_HEAD_CODE = req.body.BUDGET_HEAD_CODE
    BUDGET_HEAD_DESCRIPTION = req.body.BUDGET_HEAD_DESCRIPTION
    // AGAINST_SANCTION_NO = req.body.AGAINST_SANCTION_NO
    MINOR_HEAD = req.body.MINOR_HEAD
    UNITCODE = req.body.UNITCODE
    ESTIMATED_COST = req.body.ESTIMATED_COST
    DIVISION_NO = req.body.DIVISION_NO
    FIN_POWER = req.body.FIN_POWER
    FIN_POWER_DEMAND_FS = req.body.FIN_POWER_DEMAND_FS
    BUDGET_HEAD_DESCRIPTION_1 = req.body.BUDGET_HEAD_DESCRIPTION_1
    // CONCURRENCE_BY = req.body.CONCURRENCE_BY
    APPROVAL_AMOUNT = req.body.APPROVAL_AMOUNT
    SUPPLY_ORDER_DATE = req.body.SUPPLY_ORDER_DATE

    input_data = [
        TOTAL_COST,
        MODE_OF_TENDER_CODE,
        FINANCIAL_POWER_CODE,
        FINANCIAL_POWER_SERIAL_NO,
        CFA_CODE,
        GEM_CONTRACT_NO,
        BUDGET_HEAD_CODE,
        BUDGET_HEAD_DESCRIPTION,
        MINOR_HEAD,
        UNITCODE,
        ESTIMATED_COST,
        DIVISION_NO,
        FIN_POWER,
        FIN_POWER_DEMAND_FS,
        BUDGET_HEAD_DESCRIPTION_1,
        APPROVAL_AMOUNT,
        SUPPLY_ORDER_DATE
    ]
   
    const python = spawn("python3", ["./server_input.py", input_data ],{ shell: true });
    
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
