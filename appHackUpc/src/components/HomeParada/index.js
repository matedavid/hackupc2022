import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { ScrollView, Text } from 'react-native';
import { useIsFocused } from "@react-navigation/native";
import { useNavigation } from '@react-navigation/native';

import AsyncStorage from '@react-native-async-storage/async-storage';

import CardFGC from './cardFGC'
import CardBUS from './cardBUS';
import CardMET from './cardMET';

const HomeParada = (props) => {
    const isFocused = useIsFocused();
    const navigation = useNavigation();

    const [dataLoaded, setDataLoaded] = useState(false);

    const [fgc, setFGC] = useState([]);
    const [bus, setBUS] = useState([]);
    const [metro, setMetro] = useState([]);

    const removeSessionToken = async () => {
        await AsyncStorage.removeItem("sessionToken");
    }

    const getData = async () => {
        setDataLoaded(false);
        const sessionToken = await AsyncStorage.getItem('sessionToken');
        console.log(sessionToken)
        axios.get(`http://10.0.2.2:5000/api/overview/${sessionToken}`)
            .then((res) => {
                if (res.data.status == false) {
                    console.log(res.data.data)
                    return
                }

                const fgcData = res.data.data.FGC;
                const busData = res.data.data.BUS;
                const metroData = res.data.data.MET;

                if (fgcData != undefined) {
                    setFGC(fgcData);
                }
                if (busData != undefined) {
                    setBUS(busData);
                }
                if (metroData != undefined) {
                    setMetro(metroData);
                }

                setDataLoaded(true);
            })
            .catch((err) => {
                console.log(err);
                if (err == "User token has expired") {
                    removeSessionToken();
                    navigation.navigate('Login');
                }
            });
    }

    useEffect(() => {
        if (isFocused) {
            getData();
        }
    }, [isFocused]);

    return (
        <ScrollView>
            <Text style={{ fontSize: 40, fontWeight: 'bold', color: 'black', marginBottom: 20 }}>Welcome back!</Text>
            {
                !dataLoaded ?
                    <Text style={{ fontSize: 20 }}>Loading...</Text>
                    : <></>
            }
            {
                fgc.map((data, idx) => {
                    return <CardFGC key={idx} />
                })
            }

            {
                bus.map((data, idx) => {
                    return <CardBUS key={idx} />
                })
            }

            {
                metro.map((data, idx) => {
                    return <CardMET key={idx} />
                })
            }
        </ScrollView>
    );
};

export default HomeParada;