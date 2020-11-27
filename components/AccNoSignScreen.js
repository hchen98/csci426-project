// user did not sign in yet

import * as React from "react";
import { Button, View, Text, StyleSheet } from "react-native";
import * as Google from "expo-google-app-auth";
import AccsignedScreen from "./AccSignedScreen";

function LoginPage(props) {
  // init landing page for the Google Signin
  return (
    <View>
      <Text style={styles.header}>Sign In With Your Credentials</Text>
      <Button title="Sign in" onPress={() => props.signIn()} />
    </View>
  );
}

export default class signInPage extends React.Component {
  // init things for the log in
  constructor(props) {
    super(props);
    this.state = {
      usr_obj: {
        signedIn: false,
        full_name: "",
        last_name: "",
        first_name: "",
        email: "",
        photoUrl: "",
      },
    };
  }

  signIn = async () => {
    try {
      const result = await Google.logInAsync({
        androidClientId: "117030962609-9mblopptuccmm9fqhi2uv7eeea9bk1vh.apps.googleusercontent.com",
        // iosClientId: "<YOUR_CLIENT_ID_HERE>",
        scopes: ["profile", "email"],
      });

      if (result.type === "success") {
        this.setState({
          usr_obj: {
            signedIn: true,
            full_name: result.user.name,
            last_name: result.user.familyName,
            first_name: result.user.givenName,
            photoUrl: result.user.photoUrl,
            email: result.user.email,
          },
        });
      } else {
        console.log("\nLog failed due to: \n", result);
      }
    } catch (e) {
      console.log("\nError due to: \n", e);
      // console.log(type(value));
    }
  };

  render(){
    if (this.state.usr_obj.signedIn){
      // return signed in acc screen
      return(
        <AccsignedScreen usrinfo={this.state.usr_obj}/>
      );
    } else {
      // return default acc screen
      return(
        <View style={styles.container}>
          <LoginPage signIn={this.signIn}/>
        </View>
      );
    }
  }

}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  header: {
    fontSize: 20,
  },
});
