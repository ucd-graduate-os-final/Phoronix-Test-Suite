// sidebar.js

import React from 'react';
import { slide as Menu } from 'react-burger-menu';


export default props => {
  return (
    <Menu>
      <a className="menu-item" href="/">Home</a>
      <a className="menu-item" href="#">Standard VM</a>
      <a className="menu-item" href="#">Docker VM</a>
      <a className="menu-item" href="#">Nested VM</a>
    </Menu>
  );
};