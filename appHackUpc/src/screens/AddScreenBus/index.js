import React, { useState } from 'react';
import { View, TextInput, SafeAreaView, Text } from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';
import Icon from 'react-native-vector-icons/AntDesign';

import axios from 'axios';

const AddScreenBus = (props) => {
    const [busLineText, setBusLineText] = useState('');
    const [stopText, setStopText] = useState('');
    const [departureTime, setDepartureTime] = useState('');

    const navigation = useNavigation();
    const goToHome = () => {
        navigation.navigate('Home')
    }

    const submit = () => {
        axios.post("http://10.0.2.2:5000/api/bus/add", {
            'user': 1,
            "lineName": busLineText,
            "stopName": stopText,
            "time": departureTime.length == 0 ? null : departureTime
        })
            .then((res) => {
                if (res.data.status) {
                    goToHome();
                } else {
                    console.log("ERROR:" + res.data.data)
                }
            })
    }

    return (
        <SafeAreaView>
            <View style={styles.container}>

                <TextInput value={busLineText} onChangeText={setBusLineText}
                    style={styles.textInput} placeholder="Bus line" />

                <TextInput value={stopText} onChangeText={setStopText}
                    style={styles.textInput} placeholder="Stop" />

                <TextInput value={departureTime} onChangeText={setDepartureTime}
                    style={styles.textInput} placeholder="Departure time" />

            </View>

            <Pressable onPress={submit} style={styles.button}>
                <Text style={{ fontWeight: 'bold', fontSize: 25, color: 'white' }}>Submit</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

        </SafeAreaView>
    );
};

export default AddScreenBus;