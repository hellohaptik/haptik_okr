import React, { useState } from 'react';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
import Slider from '@material-ui/core/Slider';
import IconButton from '@material-ui/core/IconButton';
import SettingIcon from '@material-ui/icons/MoreVert';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';

function OkrRowView(props) {
  const [progress, setProgress] = React.useState(props.progress);
  const [anchorElement, setAnchorElement] = React.useState(null);

  const handleClick = event => {
    setAnchorElement(event.currentTarget);
  };

  const handleEdit = () => {
    handleClose();
    alert("Edit clicked");
  };

  const handleDiscard = () => {
    handleClose();
    alert("Discard clicked");
  };

  const handleClose = () => {
    setAnchorElement(null);
  };

  const handleProgressChange = (event, newValue) => {
    setProgress(newValue);
  };

  return (
      <TableRow>
        <TableCell align="left">{props.isObjective ? 'O' : 'KR'}</TableCell>
        <TableCell align="left">{props.title}</TableCell>
        <TableCell align="left">
          <Slider
            defaultValue={progress}
            step={10}
            onChange={handleProgressChange}
          />
        </TableCell>
        <TableCell align="left">{progress}</TableCell>
        <TableCell align="left">
          <div>
          <IconButton color="primary" onClick={handleClick} component="span">
            <SettingIcon />
          </IconButton>
          <Menu
            anchorEl={anchorElement}
            keepMounted
            onClose={handleClose}
            open={Boolean(anchorElement)}
          >
            <MenuItem onClick={handleEdit}>Edit</MenuItem>
            <MenuItem onClick={handleDiscard}>Discard</MenuItem>
          </Menu>
          </div>
        </TableCell>
      </TableRow>
  );
}
export default OkrRowView;