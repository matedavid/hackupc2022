import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Inicio from "../screens/Inicio";
import HomeScreen from "../screens/HomeScreen";
import AddScreenFGC from "../screens/AddScreenFGC";
import AddScreenMetro from "../screens/AddScreenMetro";
import AddScreenBus from "../screens/AddScreenBus";
import Login from "../screens/Login";
import Register from "../screens/Register";

const Stack = createStackNavigator();

const RootNavigator = (props) => {
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false,}} initialRouteName={"Inicio"}>
                <Stack.Screen name={"Inicio"} component={Inicio} />
                <Stack.Screen name={"Login"} component={Login} />
                <Stack.Screen name={"Register"} component={Register} />
                <Stack.Screen name={"Home"} component={HomeScreen} />
                <Stack.Screen name={"FGC"} component={AddScreenFGC} />
                <Stack.Screen name={"Bus"} component={AddScreenBus} />
                <Stack.Screen name={"Metro"} component={AddScreenMetro} />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default RootNavigator;