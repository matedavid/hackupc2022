import React from 'react'; import { View, Text } from 'react-native';

const CardMET = (props) => {
  return (
    <View style={{ margin: 10, padding: 5, height: 50, borderRadius: 15, flexDirection: 'row', backgroundColor: '#c4c4c4', borderRadius: 5 }}>
      <Text style={{ fontSize: 30, marginLeft: 30, fontWeight: 'bold', backgroundColor: 'orange', borderRadius: 5 }}>{props.data.lineName}</Text>
      <View style={{ marginLeft: 170, flexDirection: 'row' }}>
        {
          props.data.times.primera_sortida != null ?
            <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>Primera: {props.data.times.primera_sortida}</Text>
            : <></>
        }
        {
          props.data.times.darrera_sortida != null ?
            <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>Darrera: {props.data.times.darrera_sortida}</Text>
            : <></>
        }
      </View>
    </View>
  )
}

export default CardMET;