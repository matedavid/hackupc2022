import React from 'react';
import { View } from 'react-native';
import HomeMap from '../../components/HomeParada';
import HomeAdd from '../../components/HomeAdd';
import AddScreen from '../AddScreenFGC';
import HomeParada from '../../components/HomeParada';

const HomeScreen = (props) => {
    return (
        <View style={{ height: '100%' }}>
            {/*Paradas*/}
            <HomeParada />
            {/*Where button*/}
            <HomeAdd />
        </View>
    );
};

export default HomeScreen;