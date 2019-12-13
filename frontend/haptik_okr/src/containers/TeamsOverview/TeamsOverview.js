import React from "react";
import "./TeamsOverview.scss";
import Header from "../../components/Header";
import TeamItem from "./TeamItem";

function TeamsOverview({ teams_progress }) {
  return (
    <div>
      <Header></Header>
      <div className="tableContainer">
        {teams_progress.map((teamProgress, i) => {
          return (
            <TeamItem
              key={teamProgress.sheet_id}
              team={teamProgress}
            ></TeamItem>
          );
        })}
      </div>
    </div>
  );
}

TeamsOverview.defaultProps = {
  teams_progress: [
    {
      sheet_id: 1,
      team_name: "Test",
      team_progress: 0
    },
    {
      sheet_id: 2,
      team_name: "Mobile Team",
      team_progress: 75
    },
    {
      sheet_id: 3,
      team_name: "Platform NextGen",
      team_progress: 0
    },
    {
      sheet_id: 4,
      team_name: "Platform Enterprise",
      team_progress: 0
    },
    {
      sheet_id: 5,
      team_name: "Marketing",
      team_progress: 0
    },
    {
      sheet_id: 6,
      team_name: "Machine Learning",
      team_progress: 0
    }
  ]
};

export default TeamsOverview;
