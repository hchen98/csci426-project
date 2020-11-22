// this use did not sign in
// therefore, just display the option to 
// play around the scholarships that in category

import * as React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function HomeNoSignScreen({navigation}){
  // navigation.setOptions({ title: 'Search Screen' })
  return (
    <View style={styles.buttonBar_itme}>
        <Text>This is Home no sign panel!</Text>
        <Text>Coming soon!</Text>
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