import React from "react";
import "./TeamsOverview.scss";
import Header from "../../components/Header";
import TeamItem from "./TeamItem";

function TeamsOverview() {
  return (
    <div>
      <Header></Header>
      <div className="tableContainer">
        <TeamItem></TeamItem>
        <TeamItem></TeamItem>
        <TeamItem></TeamItem>
        <TeamItem></TeamItem>
        <TeamItem></TeamItem>
        <TeamItem></TeamItem>
      </div>
    </div>
  );
}

export default TeamsOverview;
