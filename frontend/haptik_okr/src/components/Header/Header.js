import React from "react";
import Moment from "moment";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
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

function getQuarterMonths(quarterInfo) {
  return (
    Moment.unix(quarterInfo.quarter_start_date).format("DD-MMM") +
    " to " +
    Moment.unix(quarterInfo.quarter_end_date).format("DD-MMM")
  );
}

function Header({ quarterInfo }) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.appbar}>
        <Toolbar className={classes.toolbar_lhs}>
          <Typography variant="h5" noWrap>
            {quarterInfo.name}
          </Typography>
          <Typography variant="caption" noWrap align="center">
            {getQuarterMonths(quarterInfo)}
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

Header.defaultProps = {
  quarterInfo: {
    id: 1,
    name: "Q4 2019-20",
    quarter_start_date: 1569888000000,
    quarter_end_date: 1869888000000,
    is_current: true
  }
};

export default Header;
