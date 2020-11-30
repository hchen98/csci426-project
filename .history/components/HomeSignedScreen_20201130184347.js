import React from "react";
import {
    StyleSheet,
    Text,
    FlatList,
    View,
    Alert,
    TouchableOpacity // for component navigate
} from "react-native";
import { ScrollView } from "react-native-gesture-handler";
// import { StackNavigator } from "react-native"; // for component navigate




export default class HomeSignedScreen extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      FlatListItems: [
        { key: "Academic Major" },
        { key: "ACT Score" },
        { key: "Age" },
        { key: "Artistic Ability" },
        { key: "Athletic Ability" },
        { key: "Deadline" },
        { key: "Employer" },
        { key: "Ethnicity" },
        { key: "Financial Need" },
        { key: "Gender" },
        { key: "Grade Point Average" },
        { key: "Honors Organization" },
        { key: "Military Affiliation" },
        { key: "Number of Scholarships Available" },
        { key: "Physical Disabilities" },
        { key: "Race" },
        { key: "Religion" },
        { key: "Residence State" },
        { key: "SAT Score" },
        { key: "Scholarship Amount" },
        { key: "School Attendance State" },
        { key: "School Year" },
        { key: "Speical Attributes" },
        { key: "Student Organization" }
      ]
    };
  }
  
  GetItem(item) {
    Alert.alert(item);
  }

  render() {
    return (
      <ScrollView>
        <View style={{flex:1, backgroundColor: 'light-dark', paddingTop: 20}}>
          
          <Text style={{ fontSize:24, fontWeight: '700'}}>
            Catagory
          </Text>

          <View style={{ height: 60, marginTop: 20}}>
            <ScrollView 
                horizontal={true}
                showsHorizontalScrollIndicator={false}>
                <FlatList
                  horizontal
                  data={ this.state.FlatListItems}
                  renderItem={({item}) => <Text style={styles.item} onPress={this.GetItem.bind(this, item.key)} > {item.key} </Text>}
                  />
            </ScrollView>
          </View>
        </View>

        <View style={{flex:2, backgroundColor: 'gray', paddingTop: 20}}>
          <Text style={{ fontSize:24, fontWeight: '700'}}>
            Recommended Scholarship
          </Text>
          <View style={{ height:60, marginTop: 20}}> 
            <ScrollView
                horizontal={true}
                showsHorizontalScrollIndicator={false}>
                <FlatList
                  horizontal
                  data={ this.state.FlatListItems}
                  renderItem={({item}) => <Text style={styles.item} onPress={this.GetItem.bind(this, item.key)} > {item.key} </Text>}
                  />
            </ScrollView>
          </View>
        </View>
      </ScrollView>
    )
  }

}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: "gray"
  },
  headerText: {
    fontSize: 20,
    textAlign: "center",
    margin: 10,
    fontWeight: "bold"
  },
  item: {
    padding: 10,
    fontSize: 20,
    height: 45,
  }
});