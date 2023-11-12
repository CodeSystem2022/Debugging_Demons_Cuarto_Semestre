/* ===============CLASE 05 - LUNES-18/09/2023=============== */
import app from "./app.js";
import {pool} from "./db.js";

pool.query("SELECT NOW()", (err, res) => {
    console.log(err, res);
    app.listen(3000);
    console.log("Server on port", 3000);
    pool.end();
})

