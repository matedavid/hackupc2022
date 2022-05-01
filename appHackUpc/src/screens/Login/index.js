import React, {useState} from 'react';
import {View, TextInput, SafeAreaView, Text, ImageBackground} from 'react-native';
import Pressable from 'react-native/Libraries/Components/Pressable/Pressable';
import Icon from 'react-native-vector-icons/AntDesign';
import { useNavigation } from '@react-navigation/native';
import styles from './styles.js';

const Login = (props) => {
    const [metroLineText, setMetroLineText] = useState('');

    const navigation = useNavigation();
    const goToHome = () => {
        navigation.navigate('Home')
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

            <Pressable onPress={goToHome} style={styles.button}>
                <Text style={{fontWeight: 'bold', fontSize: 25, color: 'white'}}>Login</Text>
                <Icon name={"right"} size={25} color={"white"} />
            </Pressable>

        </SafeAreaView>
    );
};

export default Login;