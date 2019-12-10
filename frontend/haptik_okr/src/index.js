import React from "react";
import ReactDOM from "react-dom";
import UserRegistrationView from "./signup/userRegistrationView";
import UserLoginView from "./signup/userLoginView";
import ForgotPasswordView from "./signup/forgotPasswordView";
import * as serviceWorker from "./serviceWorker";
import { Route, BrowserRouter as Router } from "react-router-dom";

const routing = (
  <Router>
    <div>
      <Route exact path="/" component={UserLoginView} />
      <Route exact path="/registration" component={UserRegistrationView} />
      <Route exact path="/forgotpassword" component={ForgotPasswordView} />
    </div>
  </Router>
);

ReactDOM.render(routing, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
