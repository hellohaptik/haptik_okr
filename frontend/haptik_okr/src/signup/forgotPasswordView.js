import { preLoginStyles } from "./styles.js";
import React from "react";
import Link from "@material-ui/core/Link";
import Avatar from "@material-ui/core/Avatar";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import { Container, TextField, Grid, Button } from "@material-ui/core";

export default function ForgotPasswordView() {
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
          Reset Password
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
          <Grid
            container
            direction="column"
            justify="center"
            alignItems="center"
          >
            <Button
              type="submit"
              variant="contained"
              size="large"
              color="primary"
              className={classes.submit}
              disabled
            >
              Send Verification email
            </Button>
            <Link href="/" underline="always" className={classes.submit}>
              {"Go back to Login"}
            </Link>
          </Grid>
        </form>
      </div>
    </Container>
  );
}
