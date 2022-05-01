import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';

const HomeParada = (props) => {
    const [dataLoaded, setDataLoaded] = useState(false);

    const [fgc, setFGC] = useState([]);
    const [bus, setBUS] = useState({ 'horas_proximas': [], 'minutos_restantes': '' });
    const [metro, setMetro] = useState({ 'darrera_sortida': null, 'primera_sortida': '' });

    const getData = () => {
        setDataLoaded(false);
        const sessionToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJleGFtcGxlQGdtYWlsLmNvbSIsImNyZWF0aW9uVGltZSI6MTY1MTM3MjQwMSwiZXhwaXJhdGlvblRpbWUiOjE2NTEzNzYwMDF9.g1sl7CWdGW8v70q_ftQPMkfID1czNNpZJ7n7dmYTSIc";
        axios.get(`http://10.0.2.2:5000/api/overview/${sessionToken}`)
            .then((res) => {
                if (res.data.status == false) {
                    console.log(res.data.data)
                    return
                }
                const fgcData = res.data.data.FGC[0];
                const busData = res.data.data.BUS[0];
                const metroData = res.data.data.MET[0];

                if (fgcData) {
                    setFGC(fgcData);
                }
                if (busData) {
                    setBUS(busData);
                }
                if (metroData) {
                    setMetro(metroData);
                }

                setDataLoaded(true);
            })
            .catch((err) => {
                console.log(err);
            });

    }

    useEffect(() => {
        getData();
    });

    return (
        <View style={{ backgroundColor: "#a0abff" }}>
            <Text style={{ fontSize: 40 }}>{!dataLoaded ? "Loading..." : ""}</Text>
            <View style={{ marginTop: 100 }}>
                <Text style={{ fontSize: 20 }}>FGC:</Text>
                {
                    fgc.map((trip, idx) => {
                        return <Text key={idx}>{trip.route} - {trip.departure}:{trip.arrival}</Text>
                    })
                }
                <Text style={{ fontSize: 20 }}>BUS:</Text>
                <Text>Minutos restantes: {bus.minutos_restantes}</Text>
                {
                    bus.horas_proximas.map((hp, idx) => {
                        return <Text key={idx}>{hp}</Text>
                    })
                }
                <Text style={{ fontSize: 20 }}>METRO:</Text>
                <Text>Primera sortida: {metro.primera_sortida}</Text>
                <Text>Darrera sortida: {metro.darrera_sortida}</Text>
            </View>
        </View>
    );
};

export default HomeParada;