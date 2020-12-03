import React, { Component } from "react";
import { StyleSheet, Text, View, Alert } from "react-native";

export default class ViewSubCate extends React.Component {
  // navigation.setOptions({ headerTitle: 'Search Screen' })

  render() {
    return (
      <View style={styles.buttonBar_itme}>
        <Text>{this.props.route.params.userkey}</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  buttonBar_itme: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
