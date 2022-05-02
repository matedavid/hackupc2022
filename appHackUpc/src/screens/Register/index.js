import React, { useState } from 'react';
import { View, TextInput, SafeAreaView, Text, ImageBackground, Alert } from 'react-native';

import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';

import axios from "axios";

const Register = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordConfirmation, setPasswordConfirmation] = useState('');

    const navigation = useNavigation();
    const goToLogin = () => {
        navigation.navigate('Login')
    }

    const register = () => {
        if (email.length == 0) {
            Alert.alert("Email can't be empty");
            return 
        }
        if (password.length == 0) {
            Alert.alert("Password can't be empty");
            return 
        }
        if (passwordConfirmation.length == 0) {
            Alert.alert("Password confirmation can't be empty");
            return 
        }
        if (password != passwordConfirmation) {
            Alert.alert("Passwords must match");
            return 
        }

        axios.post("http://10.0.2.2:5000/api/user/create", {
            "email": email,
            "password": password
        }).then((res) => {
            if (res.data.status) {
                goToLogin();
            } else {
                Alert.alert(res.data.data);
            }
        }).catch((err) => {
            console.log(err)
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

                <TextInput secureTextEntry={true} value={passwordConfirmation} onChangeText={setPasswordConfirmation}
                    style={styles.textInput} placeholder="Confirm your password" />
            </View>

            <Pressable onPress={register} style={styles.button}>
                <Text style={{ fontWeight: 'bold', fontSize: 25, color: 'white' }}>Register</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

        </SafeAreaView>
    );
};

export default Register;