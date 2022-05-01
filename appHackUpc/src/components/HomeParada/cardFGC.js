import React from 'react';
import { View, Text } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';

const CardFGC = (props) => {

  const routeColor = (route) => {
    if (route == "S1") {
      return "orange"
    } else if (route == "S2") {
      return "green"
    } else if (route == "S5") {
      return "blue"
    } else if (route == "S6") {
      return "red"
    } else if (route == "S7") {
      return "crimson"
    }
  }

  return (
    <View style={{
      margin: 10,
      padding: 5,
      height: 50,
      borderRadius: 15,
      flexDirection: 'row',
      backgroundColor: "#c4c4c4",
      borderRadius: 5,
      display: 'flex',
    }}>
      <Text style={{
        fontSize: 30,
        marginLeft: 10,
        paddingRight: 10,
        paddingLeft: 10,
        fontWeight: 'bold',
        backgroundColor: routeColor(props.data.times[0].route),
        borderRadius: 5,
      }}>{props.data.times[0].route}</Text>

      <View style={{ marginTop: 4, padding: 5, marginLeft: 4, borderRadius: 15, flexDirection: 'row', borderRadius: 5 }}>
        <Text style={{ fontWeight: 'bold' }}>{props.data.origin}</Text>
        <Text style={{ fontWeight: 'bold' }}> - </Text>
        <Text style={{ fontWeight: 'bold' }}>{props.data.destination}</Text>
      </View>

      <View style={{ marginLeft: 10, flexDirection: 'row', gridArea: "button" }}>
        <Text style={{ fontSize: 20, marginTop: 5 }}>{props.data.times[0].arrival}</Text>
      </View>

      <Icon name={"info"} size={25} color={'white'} style={{ marginLeft: 15, marginTop: 8 }} />
    </View>
  )
}

export default CardFGC;