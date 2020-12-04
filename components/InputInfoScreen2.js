import React, { Component } from "react";
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Dimensions,
  Alert,
} from "react-native";
import { KeyboardAwareScrollView } from "react-native-keyboard-aware-scroll-view";
import { act } from "react-test-renderer";

export default class InputScreen2 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      profile_required: this.props.route.params.requiredInfo,
      profile_opt: {
        major: "",
        race: "",
        religion: "",
        Disabilities: "",
        Sat: "",
        Act: "",
        address01: "",
        address02: "",
        address03: "",
      },
    };
    this.handleAcamajor = this.handleAcamajor.bind(this);
    this.handleRace = this.handleRace.bind(this);
    this.handleReligion = this.handleReligion.bind(this);
    this.handleDisability = this.handleDisability.bind(this);
    this.handleSAT = this.handleSAT.bind(this);
    this.handleACT = this.handleACT.bind(this);
    this.handleAdd01 = this.handleAdd01.bind(this);
    this.handleAdd02 = this.handleAdd02.bind(this);
    this.handleAdd03 = this.handleAdd03.bind(this);
  }

  handleAcamajor(text) {
    this.setState({
      profile_opt: {
        major: text,
      },
    });
  }

  handleRace(text) {
    this.setState({
      profile_opt: {
        race: text,
      },
    });
  }

  handleReligion(text) {
    this.setState({
      profile_opt: {
        religion: text,
      },
    });
  }

  handleDisability(text) {
    this.setState({
      profile_opt: {
        Disabilities: text,
      },
    });
  }

  handleSAT(text) {
    this.setState({
      profile_opt: {
        Sat: text,
      },
    });
  }

  handleACT(text) {
    this.setState({
      profile_opt: {
        Act: text,
      },
    });
  }

  handleAdd01(text) {
    this.setState({
      profile_opt: {
        address01: text,
      },
    });
  }

  handleAdd02(text) {
    this.setState({
      profile_opt: {
        address02: text,
      },
    });
  }

  handleAdd03(text) {
    this.setState({
      profile_opt: {
        address03: text,
      },
    });
  }

  upload2sever = () => {
    fetch("https://879099766.pythonanywhere.com/api/v1/csci426", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        signedIn: usr_obj.signedIn,
        full_name: usr_obj.full_name,
        last_name: usr_obj.last_name,
        first_name: usr_obj.first_name,
        photoUrl: usr_obj.photoUrl,
        email: usr_obj.email,
      }),

      // bodu: usr_obj
    })
      .then((response) => {
        if(response.status == 202){
          Alert.alert("Status Code: " + response.text() 
                      + "\n" + 
                      "Your data have been successfully inserted!");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
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
                  onChangeText={this.handleAcamajor}
                  placeholder="placeholder"
                  style={styles.input1}
                ></TextInput>
              </View>
              <View style={styles.grp2}>
                <Text style={styles.txt_race}>Race</Text>
                <TextInput
                  onChangeText={this.handleRace}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input2}
                ></TextInput>
              </View>
              <View style={styles.grp3}>
                <Text style={styles.txt_religion}>Religion</Text>
                <TextInput
                  onChangeText={this.handleReligion}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input3}
                ></TextInput>
              </View>
              <View style={styles.grp4}>
                <Text style={styles.txt_disability}>Disabilities</Text>
                <TextInput
                  onChangeText={this.handleDisability}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input5}
                ></TextInput>
              </View>
              <View style={styles.grp5}>
                <Text style={styles.txt_testScore}>Test Score(s)</Text>
                <TextInput
                  onChangeText={this.handleSAT}
                  placeholder="SAT"
                  keyboardType="numeric"
                  style={styles.input6}
                ></TextInput>
                <TextInput
                  onChangeText={this.handleACT}
                  placeholder="ACT"
                  keyboardType="numeric"
                  style={styles.input7}
                ></TextInput>
              </View>
              <View style={styles.grp6}>
                <Text style={styles.txt_adres}>Residential Address</Text>
                <TextInput
                  onChangeText={this.handleAdd01}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input8}
                ></TextInput>
                <TextInput
                  onChangeText={this.handleAdd02}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input9}
                ></TextInput>
                <TextInput
                  onChangeText={this.handleAdd03}
                  placeholder="placeholder"
                  keyboardType="default"
                  style={styles.input10}
                ></TextInput>
              </View>
              <View style={styles.submit_grp}>
                <TouchableOpacity
                  onPress={() =>
                    this.p2info(
                      this.state.major,
                      this.state.race,
                      this.state.religion,
                      this.state.disability,
                      this.state.Sat,
                      this.state.Act,
                      this.state.address01,
                      this.state.address02,
                      this.state.address03
                    )
                  }
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
}

const styles = StyleSheet.create({
  AwardView: {
    flex: 1,
    minHeight: Dimensions.get("window").height - 220,
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
