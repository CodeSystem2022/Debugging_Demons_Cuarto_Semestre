/* ===============CLASE 05 - LUNES-18/09/2023=============== */
import pg from "pg";

export const pool = new pg.Pool({
    port: 5432,
    host: "localhost",
    user: "postgres",
    password: "postgres",
    database: "PERN",
});

pool.on("connect", () => {
    console.log("Conectado a la base de datos");
});