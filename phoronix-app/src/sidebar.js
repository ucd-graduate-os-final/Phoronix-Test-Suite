// sidebar.js

import React from 'react';
import { slide as Menu } from 'react-burger-menu';

export default props => {
  return (
    <Menu>
      <a className="menu-item" href="/">Home</a>
      <a className="menu-item" href="/laravel">Standard VM</a>
      <a className="menu-item" href="/angular">Docker VM</a>
      <a className="menu-item" href="/react">Nested VM</a>
    </Menu>
  );
};