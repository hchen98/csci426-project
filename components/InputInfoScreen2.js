import React, { Component } from "react";
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Dimensions,
} from "react-native";
import { KeyboardAwareScrollView } from "react-native-keyboard-aware-scroll-view";

export default function InputScreen2({ navigation }) {
  return (
    <View style={styles.container}>
      <KeyboardAwareScrollView
        enableOnAndroid
        enableAutomaticScroll
        keyboardOpeningTime={0}
        // extraHeight={Platform.select({ android: (Dimensions.get('window').height - 150 ) })}
        style={styles.AwardView}
      >
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
                onPress={() => navigation.navigate("")}
                style={styles.txt_submit}
              >
                <Text style={styles.btn_submit}>Submit</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </KeyboardAwareScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  AwardView: {
    flex: 1,
    minHeight: (Dimensions.get('window').height - 220)
  },
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
    fontWeight: "bold",
    color: "#121212",
    fontSize: 20,
    marginTop: 25,
    marginLeft: 20,
  },
  grp1: {
    width: "93%",
    height: 50,
    marginTop: 22,
    marginLeft: 10,
  },
  txt_major: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input1: {
    color: "#121212",
    height: 30,
    width: "95%",
    marginTop: 2,
    marginLeft: 9,
  },
  grp2: {
    width: "95%",
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_race: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input2: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 2,
    marginLeft: 9,
  },
  grp3: {
    width: "95%",
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_religion: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input3: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 2,
    marginLeft: 9,
  },
  grp4: {
    width: "95%",
    height: 50,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_disability: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input5: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 2,
    marginLeft: 9,
  },
  grp5: {
    width: "95%",
    height: 85,
    marginTop: 19,
    marginLeft: 10,
  },
  txt_testScore: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input6: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 2,
    marginLeft: 9,
  },
  input7: {
    color: "#121212",
    height: 30,
    width: "95%",
    marginTop: 5,
    marginLeft: 9,
  },
  grp6: {
    width: "93%",
    height: 120,
    marginTop: 20,
    marginLeft: 10,
  },
  txt_adres: {
    fontWeight: "bold",
    color: "#121212",
    fontSize: 15,
    marginLeft: 9,
  },
  input8: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 2,
    marginLeft: 9,
  },
  input9: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 5,
    marginLeft: 9,
  },
  input10: {
    color: "#121212",
    height: 30,
    width: "93%",
    marginTop: 5,
    marginLeft: 9,
  },
  submit_grp: {
    width: "93%",
    height: 40,
    marginTop: 16,
    marginLeft: 15,
  },
  txt_submit: {
    width: "100%",
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
