import * as React from "react";
import { Text, View } from "react-native";

export default class GlobalState extends React.Component {
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

  render() {
    return (
      <View>  </View>
    );
  }
}
