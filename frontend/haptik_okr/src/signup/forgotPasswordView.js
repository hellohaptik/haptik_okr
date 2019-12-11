import { preLoginStyles } from "./styles.js";
import React, { useState } from "react";
import Link from "@material-ui/core/Link";
import Avatar from "@material-ui/core/Avatar";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import { Container, TextField, Grid, Button } from "@material-ui/core";

export default function ForgotPasswordView() {
  const classes = preLoginStyles();

  const [isUsernameEmpty, setUsernameEmpty] = useState(true);

  function usernameChanged(event) {
    setUsernameEmpty(event.target.value.length === 0);
  }

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
        <Typography component="h1" variant="h5" gutterBottom>
          Reset Password
        </Typography>
        <Typography variant="body2">
          Please provide the email address that you and we will send you an
          email that will allow you to reset your password
        </Typography>
        <form className={classes.form}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Username"
            name="email"
            autoComplete="email"
            autoFocus
            onChange={usernameChanged}
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
              disabled={isUsernameEmpty}
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
