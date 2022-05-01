import React from 'react';
import {View, Text, Pressable} from 'react-native';
import Icon from 'react-native-vector-icons/AntDesign';
import styles from './styles';
import { useNavigation } from '@react-navigation/native';

const HomeAdd = (props) => {
    const navigation = useNavigation();
    const goToFGC = () => {
        navigation.navigate('FGC')
    }
    const goToBus = () => {
        navigation.navigate('Bus')
    }
    const goToMetro = () => {
        navigation.navigate('Metro')
    }
    return (
        <View style={styles.container}>
            <Pressable onPress={goToFGC} style={styles.bot1}> 
                <Icon name={"pluscircleo"} size={50} color={"#0e5904"} />
                <Text style={{fontWeight: 'bold', marginTop: 10, fontSize: 20, color: 'white'}}> FGC  </Text>
            </Pressable>

            <Pressable onPress={goToBus} style={styles.bot2}> 
                <Icon name={"pluscircleo"} size={50} color={"#ab1805"} />
                <Text style={{fontWeight: 'bold', marginTop: 10, fontSize: 20, color: 'white'}}> BUS  </Text>
                
            </Pressable>

            <Pressable onPress={goToMetro} style={styles.bot3}> 
                <Icon name={"pluscircleo"} size={50} color={"#ba7007"} />
                <Text style={{fontWeight: 'bold', marginTop: 10, fontSize: 20, color: 'white'}}> METRO  </Text>
            </Pressable>      
        </View>
    );
};

export default HomeAdd;
