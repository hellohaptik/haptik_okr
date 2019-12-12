import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";

import LoginView from "./containers/LoginView";
import SignupView from "./containers/SignupView";
import OverView from "./containers/Overview";
import Header from "./components/Header";

import { Route, BrowserRouter as Router } from "react-router-dom";
import { ThemeProvider } from "@material-ui/core/styles";
import { createMuiTheme } from "@material-ui/core/styles";
import blueGrey from "@material-ui/core/colors/blueGrey";

const theme = createMuiTheme({
  palette: {
    primary: blueGrey
  }
});

const routing = (
  <ThemeProvider theme={theme}>
    <Router>
      <div>
        <Route exact path="/" component={OverView} />
        <Route exact path="/registration" component={SignupView} />
      </div>
    </Router>
  </ThemeProvider>
);

ReactDOM.render(routing, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
