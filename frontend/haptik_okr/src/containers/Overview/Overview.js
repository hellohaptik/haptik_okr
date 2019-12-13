import React from "react";
import "./Overview.scss";
import Header from "../../components/Header";
import TeamItem from "./TeamItem";

function Overview() {
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

export default Overview;
