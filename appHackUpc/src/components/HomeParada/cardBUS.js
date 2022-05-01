import React from 'react';
import { View, Text } from 'react-native';
import { managePanProps } from 'react-native-gesture-handler/lib/typescript/handlers/PanGestureHandler';
import Icon from 'react-native-vector-icons/Feather';

const CardBUS = (props) => {
  return (
    <View style={{ alignItems: 'center', margin: 10, padding: 5, height: 50, borderRadius: 15, flexDirection: 'row', backgroundColor: 'grey', borderRadius: 5 }}>
      <Text style={{ fontSize: 30, marginLeft: 10, marginRight: 10, paddingRight: 5, paddingLeft: 5, fontWeight: 'bold', backgroundColor: 'blue', borderRadius: 5 }}>{props.data.lineName}</Text>

      <Text style={{ fontSize: 15, fontWeight: 'bold', borderRadius: 5 }}>{props.data.stopName}</Text>
      <View style={{ marginLeft: 10, flexDirection: 'row' }}>
        {
          props.data.times.minutos_restantes != null ?
            <Text style={{ fontWeight: 'bold', fontSize: 20, }}>{props.data.times.minutos_restantes} min</Text>
            : <Text style={{ fontWeight: 'bold', fontSize: 20, }}>{props.data.times.horas_proximas[0]}</Text>
        }
      </View>
      <Icon name={"info"} size={25} color={'white'} style={{ marginLeft: 10 }} />
    </View>
  )
}

export default CardBUS;