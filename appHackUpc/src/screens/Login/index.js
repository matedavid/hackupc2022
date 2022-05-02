import React, { useState } from 'react';
import { View, TextInput, SafeAreaView, Text, ImageBackground, Alert } from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';

import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const Login = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const navigation = useNavigation();
    const goToHome = () => {
        navigation.navigate('Home');
    }

    const removeSessionToken = async () => {
        await AsyncStorage.removeItem("sessionToken");
    }

    const login = async () => {
        if (email.length == 0) {
            Alert.alert("Email can't be empty");
            return
        }
        if (password.length == 0) {
            Alert.alert("Password can't be empty");
            return
        }

        axios.post("http://10.0.2.2:5000/api/user/login", {
            "email": email,
            "password": password
        }).then(async (res) => {
            if (res.data.status) {
                await AsyncStorage.setItem('sessionToken', res.data.data);
                goToHome();
            } else {
                Alert.alert(res.data.data);
            }
        }).catch((err) => {
            removeSessionToken();
        });
    }

    return (
        <SafeAreaView>
            <ImageBackground style={styles.image} source={require('../../assets/metro.png')} />
            <View style={styles.container}>
                <TextInput value={email} onChangeText={setEmail}
                    style={styles.textInput} placeholder="Introduce email" />

                <TextInput secureTextEntry={true} value={password} onChangeText={setPassword}
                    style={styles.textInput} placeholder="Introduce password" />
            </View>

            <Pressable onPress={login} style={styles.button}>
                <Text style={{ fontWeight: 'bold', fontSize: 25, color: 'white' }}>Login</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

        </SafeAreaView>
    );
};

export default Login;