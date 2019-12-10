import { makeStyles } from "@material-ui/core/styles";

export const preLoginStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(16),
    display: "flex",
    padding: "10px",
    flexDirection: "column",
    alignItems: "center"
  },
  form: {
    width: "100%",
    marginTop: theme.spacing(1)
  },
  submit: {
    margin: theme.spacing(3, 0, 3)
  },
  parent: {
    backgroundColor: "white"
  }
}));
