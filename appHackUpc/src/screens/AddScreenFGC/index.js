import React, { useState } from 'react';
import { View, TextInput, SafeAreaView, Text } from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';

import axios from 'axios';

const AddScreenFGC = (props) => {
    const [fromText, setFromText] = useState('');
    const [destinationText, setDestinationText] = useState('');
    const [departureTime, setDepartureTime] = useState('');

    const navigation = useNavigation();
    const goToHome = () => {
        navigation.navigate('Home')
    }

    const submit = () => {
        axios.post("http://10.0.2.2:5000/api/fgc/add", {
            'user': 1,
            "origin": fromText,
            "destination": destinationText,
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

                <TextInput value={fromText} onChangeText={setFromText}
                    style={styles.textInput} placeholder="Origin station" />

                <TextInput value={destinationText} onChangeText={setDestinationText}
                    style={styles.textInput} placeholder="Destination station" />

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

export default AddScreenFGC;