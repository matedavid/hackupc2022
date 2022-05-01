import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
    container: {
        marginTop: 50,
        padding: 10,

    },
    textInput: {    
        padding: 10,
        backgroundColor: "grey",
        marginVertical: 5,
    },
    button: {

        marginHorizontal:65,
        justifyContent: 'center',
        alignItems: 'center',
        width: 250,
        height: 50 ,
        flexDirection: 'row',
        borderRadius: 25,
        backgroundColor: "#32427a",

    },
    image: {
        flex: 1,
        height: 900,
        width: 500,
    },
});

export default styles;