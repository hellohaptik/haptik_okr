import React from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(16),
    display: 'flex',
    padding:'10px',
    flexDirection: 'column',
    alignItems: 'center',
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 3),
  },
  parent: {
    backgroundColor: 'white',
  }
}));

export default function UserLoginView() {
  const classes = useStyles();

  return (
    <Container component="main" maxWidth="xs" borderRadius={16} className={classes.parent}>
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
            alignItems="center">
            <Button
              type="submit"
              variant="contained"
              size="large"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>

            <Link href="#"
              underline="always"
            >
              {"Forgot password?"}
            </Link>

            <Link href="/registration"
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