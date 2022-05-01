import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from "../screens/HomeScreen";
import AddScreenFGC from "../screens/AddScreenFGC";
import AddScreenMetro from "../screens/AddScreenMetro";
import AddScreenBus from "../screens/AddScreenBus";

const Stack = createStackNavigator();

const RootNavigator = (props) => {
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false,}}
            >
                <Stack.Screen name={"Home"} component={HomeScreen} />
                <Stack.Screen name={"FGC"} component={AddScreenFGC} />
                <Stack.Screen name={"Bus"} component={AddScreenBus} />
                <Stack.Screen name={"Metro"} component={AddScreenMetro} />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default RootNavigator;