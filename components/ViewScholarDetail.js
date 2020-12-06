import React, { Component } from "react";
import { StyleSheet, ScrollView, View, Text } from "react-native";

export default function ViewScholarDetail(props) {
  return (
    <ScrollView horizontal={false} style={styles.container}>
      <View style={styles.card_grp1}>
        <View style={styles.title_grp}>
          <Text style={styles.title}>ScholarShip Title .......</Text>
        </View>
        <View style={styles.amount_grpStack}>
          <View style={styles.amount_grp}>
            <Text style={styles.txt_amount}>Amount:</Text>
            <Text style={styles.amount}>$ 99999.99</Text>
          </View>
          <View style={styles.deadline_grp}>
            <Text style={styles.txt_deadline}>Deadline:</Text>
            <Text style={styles.deadline}>mm/dd/yyyy</Text>
          </View>
          <View style={styles.ava_group}>
            <Text style={styles.txt_ava}>Awards Available:</Text>
            <Text style={styles.ava}>See Description</Text>
          </View>
        </View>
      </View>
      <View style={styles.card_grp2}>
        <View style={styles.apply_grp}>
          <Text style={styles.txt_apply}>Apply Link:</Text>
          <Text style={styles.apply}>Here</Text>
        </View>
        <View style={styles.description_grp}>
          <Text style={styles.description2}>Description:</Text>
          <View style={styles.description}>
            <Text style={styles.xtxt}>xtxt</Text>
          </View>
        </View>
        <View style={styles.contact_grp}>
          <Text style={styles.txt_contact}>Contact:</Text>
          <View style={styles.rect}>
            <Text style={styles.contact}>Here</Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#E6E6E6",
    width: 360,
    height: 750
  },
  card_grp1: {
    width: 336,
    height: 229,
    backgroundColor: "rgba(255,255,255,1)",
    borderWidth: 0,
    borderColor: "#000000",
    borderRadius: 5,
    overflow: "hidden",
    alignSelf: "center"
  },
  title_grp: {
    flex: 0.6,
    backgroundColor: "rgba(255,255,255,1)",
    height: 97,
    justifyContent: "center"
  },
  title: {
    color: "#121212",
    fontSize: 16,
    height: 52,
    width: 311,
    textAlign: "left",
    alignSelf: "center"
  },
  amount_grp: {
    flex: 0.4,
    backgroundColor: "rgba(255,255,255,1)",
    left: 0,
    top: 0,
    height: 45,
    position: "absolute",
    right: 0
  },
  txt_amount: {
    color: "#121212",
    fontSize: 14,
    marginLeft: 18,
    marginTop: 22
  },
  amount: {
    color: "#121212",
    marginLeft: 82,
    marginTop: 22
  },
  deadline_grp: {
    flex: 0.4,
    backgroundColor: "rgba(255,255,255,1)",
    left: 0,
    top: 44,
    height: 45,
    position: "absolute",
    right: 0
  },
  txt_deadline: {
    color: "#121212",
    fontSize: 14,
    marginLeft: 18,
    marginTop: 22
  },
  deadline: {
    color: "#121212",
    marginLeft: 82,
    marginTop: 22
  },
  ava_group: {
    flex: 0.4,
    backgroundColor: "rgba(255,255,255,1)",
    left: 0,
    top: 87,
    height: 45,
    position: "absolute",
    right: 0
  },
  txt_ava: {
    color: "#121212",
    fontSize: 14,
    marginLeft: 18,
    marginTop: 22
  },
  ava: {
    color: "#121212",
    marginLeft: 137,
    marginTop: 22
  },
  amount_grpStack: {
    height: 132
  },
  card_grp2: {
    width: 336,
    height: 502,
    backgroundColor: "rgba(255,255,255,1)",
    borderWidth: 0,
    borderColor: "#000000",
    borderRadius: 5,
    marginTop: 18,
    marginLeft: 12
  },
  apply_grp: {
    backgroundColor: "rgba(255,255,255,1)",
    height: 45,
    borderWidth: 0,
    borderColor: "#000000",
    borderRadius: 5,
    alignSelf: "stretch"
  },
  txt_apply: {
    color: "#121212",
    marginTop: 15,
    marginLeft: 18
  },
  apply: {
    color: "#121212",
    marginLeft: 98,
    marginTop: 23
  },
  description_grp: {
    backgroundColor: "rgba(255,255,255,1)",
    alignSelf: "stretch",
    height: 330
  },
  description2: {
    color: "#121212",
    marginTop: 13,
    marginLeft: 18
  },
  description: {
    width: 300,
    height: 281,
    backgroundColor: "rgba(255,255,255,1)",
    marginTop: 25,
    alignSelf: "center"
  },
  xtxt: {
    color: "#121212",
    flex: 1
  },
  contact_grp: {
    backgroundColor: "rgba(255,255,255,1)",
    height: 127,
    borderWidth: 0,
    borderColor: "#000000",
    borderRadius: 5,
    alignSelf: "stretch"
  },
  txt_contact: {
    color: "#121212",
    marginTop: 15,
    marginLeft: 18
  },
  rect: {
    width: 300,
    height: 90,
    backgroundColor: "rgba(255,255,255,1)",
    marginTop: 22,
    marginLeft: 18
  },
  contact: {
    color: "#121212",
    flex: 1
  }
});

