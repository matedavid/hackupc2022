import React, {useState} from 'react';
import {View, TextInput, SafeAreaView, Text, ImageBackground} from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';

const Register = (props) => {
    const [metroLineText, setMetroLineText] = useState('');

    const navigation = useNavigation();
    const goToLogin = () => {
        navigation.navigate('Login')
    }

    return (
        <SafeAreaView>
            <ImageBackground style={styles.image} source={require('../../assets/metro.png')} />
            
            <View style={styles.container}>
                
            <TextInput  value={metroLineText} onChangeText={setMetroLineText}
            style={styles.textInput} placeholder="Introduce email" />

            <TextInput  value={metroLineText} onChangeText={setMetroLineText}
            style={styles.textInput} placeholder="Introduce password" />   

            </View>

            <Pressable onPress={goToLogin} style={styles.button}>
                <Text style={{fontWeight: 'bold', fontSize: 25, color: 'white'}}>Register</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

        </SafeAreaView>
    );
};

export default Register;