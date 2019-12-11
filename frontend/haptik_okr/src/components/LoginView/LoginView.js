import React from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import { preLoginStyles } from "../styles.js";
import Container from "@material-ui/core/Container";

function LoginView() {
  const classes = preLoginStyles();

  return (
    <Container component="main" maxWidth="xs" className={classes.parent}>
      <CssBaseline />
      <div className={classes.paper}>
        <form className={classes.form}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
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
              Sign In
            </Button>

            <Link href="#" underline="always">
              {"Forgot password?"}
            </Link>

            <Link
              href="/registration"
              underline="always"
              className={classes.submit}
            >
              {"Don't have an account? Sign Up"}
            </Link>
          </Grid>
        </form>
      </div>
    </Container>
  );
}

export default LoginView;
