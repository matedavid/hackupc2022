import React, {useState} from 'react';
import {View, TextInput, SafeAreaView, Text} from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';
import { ImageBackground } from "react-native";

const Inicio = (props) => {
    const [metroLineText, setMetroLineText] = useState('');

    const navigation = useNavigation();
    const goToLogin = () => {
        navigation.navigate('Login')
    }
    const goToRegister = () => {
        navigation.navigate('Register')
    }

    return (
        <SafeAreaView>
            <ImageBackground style={styles.image} source={require('../../assets/metro.png')} />

            <View style={styles.container}>
                
            <Pressable onPress={goToLogin} style={styles.button1}>
                <Text style={{fontWeight: 'bold', fontSize: 20, color: 'white'}}>LOGIN</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

            <Pressable onPress={goToRegister} style={styles.button2}>
                <Text style={{fontWeight: 'bold', fontSize: 20, color: 'white'}}>REGISTER</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

            </View>
             
        </SafeAreaView>
    );
};

export default Inicio;