import React from "react";
import Typography from "@material-ui/core/Typography";
import "./TeamItem.scss";
import GroupIcon from "@material-ui/icons/Group";
import CircularProgress from "@material-ui/core/CircularProgress";

function TeamItem() {
  return (
    <div className="teamItem">
      <div className="teamItem-column lhs">
        <Typography variant="h6" noWrap>
          Mobile Team
        </Typography>
        {/* <GroupIcon /> */}
      </div>
      <div className="teamItem-column rhs">
        <Typography variant="subtitle2" noWrap>
          0%
        </Typography>
        <CircularProgress
          className="teamItem-column-progress"
          variant="static"
          size={22}
          thickness={4.0}
          value={75}
        />
      </div>
    </div>
  );
}

export default TeamItem;
