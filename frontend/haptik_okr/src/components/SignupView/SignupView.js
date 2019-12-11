import React from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import { preLoginStyles } from "../styles.js";
import Container from "@material-ui/core/Container";

function SignupView() {
  const classes = preLoginStyles();

  function handleSubmit(event) {
    alert("A name was submitted: ");
    event.preventDefault();
  }
  return (
    <Container component="main" maxWidth="xs" className={classes.parent}>
      <CssBaseline />
      <div className={classes.paper}>
        <form className={classes.form} onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email"
            name="email"
            autoComplete="email"
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Confirm Password"
            type="password"
            id="confirm_password"
          />
          <Grid
            container
            justify="center"
            direction="column"
            alignItems="center"
          >
            <Button
              type="submit"
              variant="contained"
              size="large"
              color="primary"
              className={classes.submit}
            >
              Register
            </Button>
            <Link href="/" underline="always" className={classes.submit}>
              {"Already have an account? Login"}
            </Link>
          </Grid>
        </form>
      </div>
    </Container>
  );
}

export default SignupView;
