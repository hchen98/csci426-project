// this use did not sign in
// therefore, just display the option to
// play around the scholarships that in category

import * as React from "react";
import { StyleSheet, Text, View } from "react-native";

export default function HomeNoSignScreen( props ) {
  // navigation.setOptions({ title: 'Search Screen' })

  getAPIINFO = () => {
    fetch("https://879099766.pythonanywhere.com/api/v1/resources/books/all", {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <View style={styles.buttonBar_itme}>
      <Text>This is Home no sign panel!</Text>
      <Text>Coming soon!</Text>
      {/* {getAPIINFO} */}
    </View>
  );
}

const styles = StyleSheet.create({
  buttonBar_itme: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
