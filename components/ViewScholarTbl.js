// DO NOT USE THIS FILE UNLESS OTHERWISE 
// THIS MESSAGE IS REMOVED!!!

import React from "react";
import { StyleSheet, Text, View, ActivityIndicator } from "react-native";
import { FlatList } from "react-native-gesture-handler";
import firebase from "../db/firebaseDB";

// disable the yellow warning message box
console.disableYellowBox = true;

export default class ViewScholarTbl extends React.Component {
  // navigation.setOptions({ headerTitle: 'Search Screen' })
  constructor(props) {
    super(props);
    this.firestoreRef = firebase
      .firestore()
      .collection("scholar_dir")
      // .where("Terms", "==", this.props.route.params.itemKey);
      // since "Terms" attribute is a dict, we have to use 'in'
      .where("Terms", "in", this.props.route.params.itemKey);

    this.state = {
      isLoading: true,
      scholarArr: [],
      subCate: this.props.route.params.itemKey,
    };
  }

  componentDidMount(){
    this.unsubscribe = this.firestoreRef.onSnapshot(this.getDoc)
  }

  componentWillUnmount(){
    this.unsubscribe();
  }

  getDoc = (querySnapshot) => {
    const temp = querySnapshot.data();
    // now the temp is key val pair
    // temp => ("sub category title", ["i", "j", "k"])
    const valArr = temp[this.state.subCate];
    this.setState({
      scholarArr: valArr, 
      isLoading: false,
    });
    console.info("Data retrived from FireStore!");
  }

  FlatListItemSeparator = () => {
    return <View style={styles.ItemSeparator} />;
  };

  render() {
    if(this.state.isLoading){
      return(
        <View style={styles.preloader}>
          <ActivityIndicator size="large" color="#9E9E9E" />
        </View>
      );
    }
    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.scholarArr}
          ItemSeparatorComponent={this.FlatListItemSeparator}
          renderItem={({ item }) => (
            <Text
              style={styles.item}
              onPress={() => {
                // we are able to navigate to "ViewSubCate"
                // since it is one of the stack screens in App.js
                // therefore, no need to import in this screen
                this.props.navigation.navigate('ViewSubCate', {
                  title: (item + " List"),
                  itemKey: item,
                });
              }}
            > {item} </Text>
          )}
        >
        </FlatList>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "white",
  },
  preloader: {
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    position: "absolute",
    alignItems: "center",
    justifyContent: "center",
  },
  ItemSeparator: {
    height: 1,
    width: "100%",
    backgroundColor: "black",
  },
  item: {
    padding: 10,
    margin: 10,
    fontSize: 18,
    height: 45,
  },
});
