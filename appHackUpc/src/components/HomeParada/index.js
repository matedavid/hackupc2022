import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { View, ScrollView, Text } from 'react-native';

import CardFGC from './cardFGC'
import CardBUS from './cardBUS';
import CardMET from './cardMET';

const HomeParada = (props) => {
    const [dataLoaded, setDataLoaded] = useState(false);

    const [fgc, setFGC] = useState([]);
    const [bus, setBUS] = useState([]);
    const [metro, setMetro] = useState([]);

    const getData = () => {
        setDataLoaded(false);
        const sessionToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZW1haWwiOiJleGFtcGxlQGdtYWlsLmNvbSIsImNyZWF0aW9uVGltZSI6MTY1MTM3NjAzMCwiZXhwaXJhdGlvblRpbWUiOjE2NTEzNzk2MzB9.YOAXUDkkclhHlD1xM_yqFe_StsdM3aXeQWPr9SOktKI";
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
                setDataLoaded(true);
            });
    }

    useEffect(() => {
        getData();
    }, []);

    return (
        <ScrollView>
            <Text style={{fontSize: 40, fontWeight: 'bold', color: 'black', marginBottom: 20}}>Welcome back!</Text>
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