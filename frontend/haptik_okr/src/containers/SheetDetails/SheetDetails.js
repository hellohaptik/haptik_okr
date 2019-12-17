import React, { useState } from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import { makeStyles } from '@material-ui/core/styles';
import testdata from './testdata.json';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableHead from '@material-ui/core/TableHead';
import Paper from '@material-ui/core/Paper';
import OkrRowView from "./OkrRowView";

const useStyles = makeStyles({
  parent: {
    display: 'flex',
    backgroundColor: 'white',
    paddingBottom: '50px',
  },
  paper: {
    overflow: 'auto',
    marginTop: '50px',
    flexDirection: 'column',
  }
});
function SheetDetails() {
  const classes = useStyles();
  const [data, setData] = useState(testdata);

  return (
    <div className={classes.parent}>
      <Container component="main" >
        <CssBaseline />
        {data.body.objectives.map(function (objectiveItem) {
          return (
            <Paper className={classes.paper}>
              <Table>
                <colgroup>
                  <col width="5%" />
                  <col width="60%" />
                  <col width="20%" />
                  <col width="5%" />
                  <col width="5%" />
                </colgroup>
                {/* Objective header view */}
                <TableHead>
                  <OkrRowView
                    id={objectiveItem.id}
                    title={objectiveItem.title}
                    progress={objectiveItem.progress}
                    isObjective="true" />
                </TableHead>
                {/* Objective key results view*/}
                <TableBody>
                  {objectiveItem.keyresults.map(function (item) {
                    return (
                      <OkrRowView
                        id={item.id}
                        title={item.title}
                        progress={item.progress}
                        idObjective="false" />
                    )
                  })}
                </TableBody>
              </Table>
            </Paper>
          )
        })}
      </Container>
    </div>
  );
}

export default SheetDetails;
