import React, { useEffect } from 'react';
import { View, TextInput, SafeAreaView, Text } from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';
import { ImageBackground } from "react-native";

import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

const Inicio = (props) => {
    const navigation = useNavigation();

    const goToLogin = () => {
        navigation.navigate('Login')
    }
    const goToRegister = () => {
        navigation.navigate('Register')
    }
    const goToHome = () => {
        navigation.navigate("Home");
    }

    const checkToken = async () => {
        const sessionToken = await AsyncStorage.getItem('sessionToken');
        axios.get(`http://192.168.43.59:5000/api/user/validateToken/${sessionToken}`)
            .then((res) => {
                if (res.data.status) {
                    goToHome();
                }
            }).catch((err) => {
                console.log(err)
            });
    }

    useEffect(() => {
        checkToken();
    }, []);

    return (
        <SafeAreaView>
            <ImageBackground style={styles.image} source={require('../../assets/metro.png')} />

            <View style={styles.container}>
                <Text style={{ fontSize: 40, position: 'relative', bottom: 100,fontWeight: 'bold',color: 'black'}}>Moveefy</Text>
                <Pressable onPress={goToLogin} style={styles.button1}>
                    <Text style={{ fontWeight: 'bold', fontSize: 20, color: 'white' }}>LOGIN</Text>
                    <Icon name={"right"} size={25} color={"white"} />
                </Pressable>

                <Pressable onPress={goToRegister} style={styles.button2}>
                    <Text style={{ fontWeight: 'bold', fontSize: 20, color: 'white' }}>REGISTER</Text>
                    <Icon name={"right"} size={25} color={"white"} />
                </Pressable>
            </View>

        </SafeAreaView>
    );
};

export default Inicio;