import React from "react";

import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { makeStyles, useTheme } from "@material-ui/core/styles";
import MoreIcon from "@material-ui/icons/MoreVert";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1
  },
  appbar: {
    flexDirection: "row"
  },
  toolbar_lhs: {
    flexDirection: "column",
    flexGrow: 1,
    alignItems: "flex-start",
    justifyContent: "center"
  }
}));

function Header() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.appbar}>
        <Toolbar className={classes.toolbar_lhs}>
          <Typography variant="h6" noWrap>
            Q3 2019-20
          </Typography>
          <Typography variant="caption" noWrap align="center">
            1-Jan to 30-Dec
          </Typography>
        </Toolbar>
        <Toolbar edge="end">
          <Typography variant="body1" noWrap>
            Simranjot
          </Typography>
          <IconButton
            aria-label="display more actions"
            edge="end"
            color="inherit"
          >
            <MoreIcon />
          </IconButton>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Header;
