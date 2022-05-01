import React from 'react';
import {View, Text} from 'react-native';
import HomeMap from '../../components/HomeParada';
import HomeAdd from '../../components/HomeAdd';
import AddScreen from '../AddScreenFGC';
import HomeParada from '../../components/HomeParada';

const HomeScreen = (props) => {
    return (
        <View style={{ height: '100%' }}>
            <HomeAdd />
        </View>
    );
};

export default HomeScreen;