/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import 'react-native-gesture-handler';

import Icon from 'react-native-vector-icons/AntDesign';
import React from 'react';
import {StatusBar} from 'react-native';

import Router from './src/Navigation/Root';

const App: () => ReactNode = () => {
  return (
    <>
      <StatusBar barStyle= "dark-content" />
      <Router />
    </>    
  );
};

export default App;
