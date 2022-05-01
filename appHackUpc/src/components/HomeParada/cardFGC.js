import React from 'react';
import { View, Text } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';

const CardFGC = (props) => {
  return (
    <View style={{ margin: 10, padding: 5, height: 50, borderRadius: 15, flexDirection: 'row', backgroundColor: 'grey', borderRadius: 5 }}>
      <Text style={{ fontSize: 30, marginLeft: 10, paddingRight: 10, paddingLeft: 10, fontWeight: 'bold', backgroundColor: 'green', borderRadius: 5 }}>{ props.data.times[0].route }</Text>

      <View style={{ marginTop: 4, padding: 5, borderRadius: 15, flexDirection: 'row', backgroundColor: 'grey', borderRadius: 5 }}>
        <Text>{props.data.origin}</Text>
        <Text> - </Text>
        <Text>{ props.data.destination}</Text>
      </View>

      <View style={{ marginLeft: 10, flexDirection: 'row' }}>
        <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>25</Text>
        <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>min</Text>
      </View>

      <Icon name={"info"} size={25} color={'white'} style={{ marginLeft:15, marginTop: 8 }}/>
    </View>
  )
}

export default CardFGC;