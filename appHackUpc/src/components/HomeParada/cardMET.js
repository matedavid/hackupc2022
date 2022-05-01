import React from 'react';
import { View, Text } from 'react-native';

const CardMET = (props) => {
  return (
    <View style={{ margin: 10, padding: 5, height: 50, borderRadius: 15, flexDirection: 'row', backgroundColor: 'grey', borderRadius: 5 }}>
      <Text style={{ fontSize: 30, marginLeft: 30, fontWeight: 'bold', backgroundColor: 'orange', borderRadius: 5 }}>  L1  </Text>
      <View style={{ marginLeft: 170, flexDirection: 'row' }}>
        <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>25</Text>
        <Text style={{ fontWeight: 'bold', fontSize: 20, marginTop: 5 }}>min</Text>
      </View>
    </View>
  )
}

export default CardMET;