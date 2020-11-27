import React, { Component } from "react";
import {
  StyleSheet,
  View,
  StatusBar,
  Text,
  TextInput,
  TouchableOpacity,
} from "react-native";
import { useNavigation } from '@react-navigation/native';

function InputInfoScreen2(props) {
  const navigation = useNavigation();

  return (
    <View style={styles.container}>
      <StatusBar hidden />
      <View style={styles.containerGrp1}>
        <View style={styles.containerBkground1}>
          <Text style={styles.optionalDetails}>Optional Details</Text>
          <View style={styles.grp1}>
            <Text style={styles.txt_major}>Academic Major</Text>
            <TextInput
              placeholder="placeholder"
              style={styles.input1}
            ></TextInput>
          </View>
          <View style={styles.grp2}>
            <Text style={styles.txt_race}>Race</Text>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input2}
            ></TextInput>
          </View>
          <View style={styles.grp3}>
            <Text style={styles.txt_religion}>Religion</Text>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input3}
            ></TextInput>
          </View>
          <View style={styles.grp4}>
            <Text style={styles.txt_disability}>Disabilities</Text>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input5}
            ></TextInput>
          </View>
          <View style={styles.grp5}>
            <Text style={styles.txt_testScore}>Test Score(s)</Text>
            <TextInput
              placeholder="SAT"
              keyboardType="numeric"
              style={styles.input6}
            ></TextInput>
            <TextInput
              placeholder="ACT"
              keyboardType="numeric"
              style={styles.input7}
            ></TextInput>
          </View>
          <View style={styles.grp6}>
            <Text style={styles.txt_adres}>Residential Address</Text>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input8}
            ></TextInput>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input9}
            ></TextInput>
            <TextInput
              placeholder="placeholder"
              keyboardType="default"
              style={styles.input10}
            ></TextInput>
          </View>
          <View style={styles.submit_grp}>
            <TouchableOpacity
              onPress={() => navigation.navigate("Untitled")}
              style={styles.txt_submit}
            >
              <Text style={styles.btn_submit}>Submit</Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  containerGrp1: {
    backgroundColor: "rgba(230, 230, 230,1)",
    flex: 1,
  },
  containerBkground1: {
    height: 656,
    backgroundColor: "rgba(255,255,255,1)",
    marginTop: 62,
  },
  optionalDetails: {
    
    color: "#121212",
    fontSize: 20,
    marginTop: 25,
    marginLeft: 20,
  },
  grp1: {
    width: 340,
    height: 50,
    marginTop: 22,
    marginLeft: 10,
  },
  txt_major: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input1: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  grp2: {
    width: 340,
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_race: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input2: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  grp3: {
    width: 340,
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_religion: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input3: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  grp4: {
    width: 340,
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_disability: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input5: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  grp5: {
    width: 340,
    height: 85,
    marginTop: 19,
    marginLeft: 10,
  },
  txt_testScore: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input6: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  input7: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 5,
    marginLeft: 9,
  },
  grp6: {
    width: 340,
    height: 120,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_adres: {
    
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input8: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 2,
    marginLeft: 9,
  },
  input9: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 5,
    marginLeft: 9,
  },
  input10: {
    
    color: "#121212",
    height: 30,
    width: 323,
    marginTop: 5,
    marginLeft: 9,
  },
  submit_grp: {
    width: 330,
    height: 40,
    marginTop: 16,
    marginLeft: 15,
  },
  txt_submit: {
    width: 330,
    height: 40,
    backgroundColor: "rgba(0,149,47,1)",
    alignSelf: "center",
  },
  btn_submit: {
    
    color: "rgba(255,255,255,1)",
    fontSize: 16,
    marginTop: 10,
    alignSelf: "center",
  },
});

export default Inputn2;
