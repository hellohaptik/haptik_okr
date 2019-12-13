import React from "react";
import "./TeamItem.scss";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";

const useStylesProgress = makeStyles({
  root: {
    position: "relative",
    marginLeft: 12
  },
  top: {
    color: "#eeeeee"
  },
  bottom: {
    color: "primary",
    position: "absolute",
    left: 0
  }
});

function BorderCircularProgress(props) {
  const classes = useStylesProgress();

  return (
    <div className={classes.root}>
      <CircularProgress
        variant="static"
        className={classes.top}
        size={22}
        value={100}
        thickness={4}
      />
      <CircularProgress
        variant="static"
        className={classes.bottom}
        size={22}
        thickness={4}
        {...props}
      />
    </div>
  );
}

function TeamItem({ team }) {
  return (
    <div className="teamItem">
      <div className="teamItem-column lhs">
        <Typography variant="h6" noWrap>
          {team.team_name}
        </Typography>
      </div>
      <div className="teamItem-column rhs">
        <Typography variant="subtitle2" noWrap>
          {team.team_progress}%
        </Typography>
        <BorderCircularProgress value={team.team_progress} />
      </div>
    </div>
  );
}

export default TeamItem;
