const express = require("express");
const tareaRouter = express.Router();

const tareasController = require("../controllers/tareas");

tareaRouter.get("/", tareasController.getAll);
tareaRouter.get("/:id", tareasController.getOne);
tareaRouter.post("/", tareasController.save);

module.exports = tareaRouter;
