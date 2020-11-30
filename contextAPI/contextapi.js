import React, { createContext } from "react";

const UserContext = createContext({
  usr_profile: {
    signedIn: false,
    full_name: "",
    last_name: "",
    first_name: "",
    email: "",
    photoUrl: "",
  },
  updateProfile: () => {},
});

export default class UserProvider extends React.Component{
  updateProfile = newProfileInfo => {
    this.setState({ usr_profile: newProfileInfo });
  };

  state = {
    usr_profile: {
      signedIn: false,
      full_name: "",
      last_name: "",
      first_name: "",
      email: "",
      photoUrl: "",
    },
    updateProfile: this.updateProfile,
  };

  render(){
    return(
      <UserContext.Provider value={this.state}>
        {this.props.children}
      </UserContext.Provider>
    );
  }
}