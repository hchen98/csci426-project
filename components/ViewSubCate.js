import * as React from 'react';
import { StyleSheet, Text, View, Alert } from 'react-native';

function test(props){
  Alert.alert(props);
}

export default function ViewSubCate(props){
  // navigation.setOptions({ title: 'Search Screen' })

  return (
    <View style={styles.buttonBar_itme}>
        {test(props)}
    </View>
  );
}

const styles = StyleSheet.create({
  buttonBar_itme: {
    flex: 1, 
    justifyContent: 'center', 
    alignItems: 'center',
  },
});