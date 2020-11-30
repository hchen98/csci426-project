import React from "react";
// import { StyleSheet, Text, View } from "react-native";
import { AppRegistry } from "react-native";
import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import { Ionicons } from "@expo/vector-icons";
import FeatherIcon from "react-native-vector-icons/Feather";
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";

import HomeNoSignScreen from "./components/HomeNoSignScreen";
import SearchScreen from "./components/SearchScreen";
import AccScreen from "./components/AccScreen";
import InputScreen1 from "./components/InputInfoScreen1";
import InputScreen2 from "./components/InputInfoScreen2";

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

function TabScreens() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          if (route.name === "Home") {
            iconName = focused ? "home" : "home";
            return <FeatherIcon name="home" size={size} color={color} />;
          } else if (route.name === "Account") {
            iconName = focused ? "account-outline" : "account-outline";
            return (
              <MaterialCommunityIconsIcon
                name={iconName}
                size={size}
                color={color}
              />
            );
          } else if (route.name === "Search") {
            iconName = focused ? "ios-search" : "ios-search";
            return <Ionicons name={iconName} size={size} color={color} />;
          }
        },
      })}
    >
      <Tab.Screen
        name="Home"
        options={{ title: "Home Screen" }}
        component={HomeNoSignScreen}
      />
      <Tab.Screen
        name="Search"
        component={SearchScreen}
        options={{ title: "Search Screen" }}
      />
      <Tab.Screen
        name="Account"
        options={{ title: "Account Screen" }}
        component={AccScreen}
      />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name={"Home"} component={TabScreens} />
          <Stack.Screen name={"InputScreen1"} component={InputScreen1} />
          <Stack.Screen name={"InputScreen2"} component={InputScreen2} />
        </Stack.Navigator>
      </NavigationContainer>
  );
}

// AppRegistry.registerComponent("App", () => App);
