const express = require("express");
const authRouter = express.Router();

const authController = require("../controllers/users");

authRouter.post("/login", authController.login);
authRouter.post("/register", authController.register);
authRouter.get("/me/:user", authController.profile);

module.exports = authRouter;
