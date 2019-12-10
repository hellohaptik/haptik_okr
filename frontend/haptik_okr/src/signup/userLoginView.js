import React from "react";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import { preLoginStyles } from "./styles.js";
import Container from "@material-ui/core/Container";

import Avatar from "@material-ui/core/Avatar";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";

export default function UserLoginView() {
  const classes = preLoginStyles();

  return (
    <Container
      component="main"
      maxWidth="xs"
      borderRadius={16}
      className={classes.parent}
    >
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign In
        </Typography>
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

            <Link href="/forgotpassword" underline="always">
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
